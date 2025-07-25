import os
import re

# 표준 파일명 정규식: 2023-10-04-singular-value-decomposition.md
filename_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9\-]+\.md$")

# 예시: Over_Under_Fitting → over-under-fitting
def standardize_slug(slug):
    return slug.lower().replace("_", "-")

# 링크 패턴: [text]({{site.url}}/machine_learning/Over_Under_Fitting)
link_pattern = re.compile(r"\[([^\]]+)\]\(\{\{site\.url\}\}(/[a-zA-Z0-9_/-]+)\)")

root_dir = '.'

for dirpath, dirnames, filenames in os.walk(root_dir):
    for fname in filenames:
        if fname.endswith('.md'):
            full_path = os.path.join(dirpath, fname)

            # 파일명 표준 체크
            if not filename_pattern.match(fname):
                print(f"비표준 파일명: {full_path}")

            # 파일 읽기
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 링크 주소 변환
            def replace_link(match):
                text = match.group(1)
                path = match.group(2)
                # 디렉토리와 파일명 분리
                parts = path.strip('/').split('/')
                # 마지막 부분을 변환
                parts = [standardize_slug(p) for p in parts]
                new_path = '/' + '/'.join(parts)
                return f"[{text}]({{{{site.url}}}}{new_path})"

            new_content = link_pattern.sub(replace_link, content)

            # 수정이 있으면 파일에 덮어쓰기
            if new_content != content:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"링크 수정됨: {full_path}")
