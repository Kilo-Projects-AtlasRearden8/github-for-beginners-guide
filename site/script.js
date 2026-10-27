/* Chapter list search filter */
document.addEventListener("DOMContentLoaded", function () {
  var input = document.getElementById("chapterSearch");
  var list = document.getElementById("chapterList");
  if (!input || !list) return;

  input.addEventListener("input", function () {
    var term = input.value.toLowerCase();
    var items = list.getElementsByTagName("li");
    for (var i = 0; i < items.length; i++) {
      var a = items[i].getElementsByTagName("a")[0];
      var txt = a.textContent || a.innerText || "";
      items[i].style.display = txt.toLowerCase().indexOf(term) > -1 ? "" : "none";
    }
  });

  // Highlight the current page in the nav based on filename
  var path = window.location.pathname;
  var file = path.substring(path.lastIndexOf("/") + 1);
  var links = list.getElementsByTagName("a");
  for (var j = 0; j < links.length; j++) {
    if (links[j].getAttribute("href") === file) {
      links[j].classList.add("active");
    }
  }
});
