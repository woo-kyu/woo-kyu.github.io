document.querySelectorAll('.big-cube').forEach(cube => {
  cube.addEventListener('click', () => {
    cube.classList.toggle('expanded');
  });
});
