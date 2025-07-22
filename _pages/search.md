---
layout: default
title: "Search"
permalink: /search/
---

<h1>Search</h1>

<p>Enter a search term to find relevant posts:</p>

<input type="text" id="search" placeholder="Enter your search term..." />
<ul id="results"></ul>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"></script>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    fetch('{{ site.baseurl }}/search.json')
      .then(response => response.json())
      .then(data => {
        var idx = lunr(function () {
          this.ref('id');
          this.field('title');
          this.field('content');

          data.forEach(function (doc) {
            this.add(doc);
          }, this);
        });

        document.getElementById('search').addEventListener('input', function () {
          var query = this.value;
          var results = idx.search(query);

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


<!-- ---
layout: default  # 기본 레이아웃 사용
title: "Search"  # 페이지 제목
permalink: /search/  # URL 설정
---

[//]: # ()
[//]: # (<h1>{{ Search }}</h1>)

[//]: # ()
[//]: # (<p>Enter a search term to find relevant posts:</p>)

[//]: # ()
[//]: # (<input type="text" id="search" placeholder="Enter your search term..." />)

[//]: # (<ul id="results"></ul>)

[//]: # ()
[//]: # (<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"></script>)

[//]: # (<script>)

[//]: # (  document.addEventListener&#40;"DOMContentLoaded", function&#40;&#41; {)

[//]: # (    // search.json 파일을 로드)

[//]: # (    fetch&#40;'{{ site.baseurl }}/search.json'&#41;)

[//]: # (      .then&#40;response => response.json&#40;&#41;&#41;)

[//]: # (      .then&#40;data => {)

[//]: # (        // Lunr.js 인덱스 생성)

[//]: # (        var idx = lunr&#40;function &#40;&#41; {)

[//]: # (          this.ref&#40;'id'&#41;;)

[//]: # (          this.field&#40;'title'&#41;;)

[//]: # (          this.field&#40;'content'&#41;;)

[//]: # (          )
[//]: # (          data.forEach&#40;function &#40;doc&#41; {)

[//]: # (            this.add&#40;doc&#41;;)

[//]: # (          }, this&#41;;)

[//]: # (        }&#41;;)

[//]: # ()
[//]: # (        // 검색어 입력 시 인덱스에서 검색)

[//]: # (        document.getElementById&#40;'search'&#41;.addEventListener&#40;'input', function &#40;&#41; {)

[//]: # (          var query = this.value;)

[//]: # (          var results = idx.search&#40;query&#41;;)

[//]: # ()
[//]: # (          // 결과 목록 업데이트)

[//]: # (          var resultsList = document.getElementById&#40;'results'&#41;;)

[//]: # (          resultsList.innerHTML = '';)

[//]: # ()
[//]: # (          results.forEach&#40;function &#40;result&#41; {)

[//]: # (            var item = data.find&#40;doc => doc.id === result.ref&#41;;)

[//]: # (            var li = document.createElement&#40;'li'&#41;;)

[//]: # (            var a = document.createElement&#40;'a'&#41;;)

[//]: # (            a.href = item.url;)

[//]: # (            a.textContent = item.title;)

[//]: # (            li.appendChild&#40;a&#41;;)

[//]: # (            resultsList.appendChild&#40;li&#41;;)

[//]: # (          }&#41;;)

[//]: # (        }&#41;;)

[//]: # (      }&#41;;)

[//]: # (  }&#41;;)

[//]: # (</script>) -->
