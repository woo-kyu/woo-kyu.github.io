---
layout: default  # 기본 레이아웃 사용
title: "Search"  # 페이지 제목
permalink: /search/  # URL 설정
---

<h1>{{ Search }}</h1>

<p>Enter a search term to find relevant posts:</p>

<input type="text" id="search" placeholder="Enter your search term..." />
<ul id="results"></ul>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    // search.json 파일을 로드
    fetch('{{ site.baseurl }}/search.json')
      .then(response => response.json())
      .then(data => {
        // Lunr.js 인덱스 생성
        var idx = lunr(function () {
          this.ref('id');
          this.field('title');
          this.field('content');
          
          data.forEach(function (doc) {
            this.add(doc);
          }, this);
        });

        // 검색어 입력 시 인덱스에서 검색
        document.getElementById('search').addEventListener('input', function () {
          var query = this.value;
          var results = idx.search(query);

          // 결과 목록 업데이트
          var resultsList = document.getElementById('results');
          resultsList.innerHTML = '';

          results.forEach(function (result) {
            var item = data.find(doc => doc.id === result.ref);
            var li = document.createElement('li');
            var a = document.createElement('a');
            a.href = item.url;
            a.textContent = item.title;
            li.appendChild(a);
            resultsList.appendChild(li);
          });
        });
      });
  });
</script>
