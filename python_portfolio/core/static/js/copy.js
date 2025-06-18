document.addEventListener("DOMContentLoaded", function () {
  const copyButtons = document.querySelectorAll('.copy-btn');

  copyButtons.forEach((button) => {
    button.addEventListener('click', () => {
      // Find the closest <pre><code> block inside the same card
      const card = button.closest('.card-body');
      const codeBlock = card.querySelector('pre code');

      if (codeBlock) {
        const text = codeBlock.innerText;
        navigator.clipboard.writeText(text).then(() => {
          button.innerHTML = '✅ Copied';
          setTimeout(() => (button.innerHTML = '📋 Copy'), 1500);
        });
      }
    });
  });
});
