document.addEventListener("DOMContentLoaded", function () {
  // ✅ Sidebar collapse toggle (for mobile)
  const toggleBtn = document.getElementById("sidebarToggle");
  const sidebar = document.querySelector(".sidebar");

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener("click", function () {
      sidebar.classList.toggle("collapsed");
    });
  }

  // ✅ Collapse other sections when one is opened
  document.querySelectorAll('.sidebar h5[data-toggle="collapse"]').forEach(header => {
    const targetId = header.getAttribute('data-target');
    const collapseTarget = document.querySelector(targetId);

    header.addEventListener('click', function () {
      document.querySelectorAll('.sidebar .collapse').forEach(div => {
        if (div !== collapseTarget) {
          $(div).collapse('hide'); // Bootstrap’s collapse
        }
      });
    });

    // ✅ Rotate the chevron on expand/collapse
    const chevron = header.querySelector('.chevron');
    if (chevron && collapseTarget) {
      collapseTarget.addEventListener('show.bs.collapse', () => {
        chevron.classList.add('rotate');
      });

      collapseTarget.addEventListener('hide.bs.collapse', () => {
        chevron.classList.remove('rotate');
      });
    }
  });

  // ✅ Optional: Automatically highlight current section
  document.querySelectorAll('.nav-link.active').forEach(link => {
    const parentCollapse = link.closest('.collapse');
    if (parentCollapse) {
      parentCollapse.classList.add('show');
      const header = parentCollapse.previousElementSibling;
      if (header && header.tagName === 'H5') {
        header.style.fontWeight = 'bold';
        header.style.color = '#0d6efd';
      }
    }
  });
});
