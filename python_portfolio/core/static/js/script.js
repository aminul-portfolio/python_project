// Sidebar toggle for mobile
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  if (sidebar) {
    sidebar.classList.toggle('show');
  }
}

// Highlight.js initializer
document.addEventListener("DOMContentLoaded", function () {
  if (typeof hljs !== 'undefined') {
    hljs.highlightAll();
  }
});
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
  localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
}

// Load dark mode on page load if saved
document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("darkMode") === "true") {
    document.body.classList.add("dark-mode");
  }
});
document.addEventListener("DOMContentLoaded", function () {
  const exampleCards = document.querySelectorAll("#exampleCards .col");
  const quizDataKey = "lists";
  fetch("/static/data/quiz_questions.json")
    .then(res => res.json())
    .then(data => {
      const quizCount = data[quizDataKey]?.length || 0;
      document.getElementById("quizCount")?.textContent = quizCount;
      document.getElementById("quizCountText")?.textContent = quizCount;
    });
  if (document.getElementById("exampleCount"))
    document.getElementById("exampleCount").textContent = exampleCards.length;
});
