document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("feedbackForm");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      const formData = new FormData(form);
      const comment = formData.get("comment");

      if (!comment.trim()) {
        alert("💬 Please enter your feedback before submitting.");
        return;
      }

      // Optionally show loading or send via AJAX (future upgrade)
      alert("✅ Thank you for your feedback!");
      form.reset();
    });
  }
});
