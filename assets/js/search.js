document.addEventListener("DOMContentLoaded", function() {
  var input = document.getElementById('search');
  var results = document.getElementById('results');
  if (!input || !results) return;

  fetch('/search.json')
    .then(response => response.json())
    .then(data => {
      var idx = lunr(function () {
        this.ref('url');
        this.field('title');
        this.field('content');
        data.forEach(function (doc) {
          this.add(doc);
        }, this);
      });

      input.addEventListener('input', function () {
        var query = this.value;
        var found = idx.search(query);

        results.innerHTML = '';
        found.forEach(function (result) {
          var item = data.find(doc => doc.url === result.ref);
          if (item) {
            var div = document.createElement('div');
            div.innerHTML = '<a href="' + item.url + '">' + item.title + '</a>';
            results.appendChild(div);
          }
        });
      });
    });
});
