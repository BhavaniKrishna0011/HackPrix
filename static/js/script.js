document.getElementById('theme-toggle').addEventListener('click', function() {
  document.body.classList.toggle('light-mode');
  document.querySelector('nav').classList.toggle('light-mode');
  document.querySelectorAll('.nav-links a').forEach(link => {
      link.classList.toggle('light-mode');
  });
  document.querySelectorAll('.nav-icons a').forEach(icon => {
      icon.classList.toggle('light-mode');
  });
  // Toggle the icon between moon and sun
  const icon = this.querySelector('i');
  if (icon.classList.contains('fa-moon')) {
      icon.classList.remove('fa-moon');
      icon.classList.add('fa-sun');
  } else {
      icon.classList.remove('fa-sun');
      icon.classList.add('fa-moon');
  }
});
