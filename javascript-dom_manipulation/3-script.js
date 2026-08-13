#!/usr/bin/node
const toggleHeader = document.querySelector('#toggle_header');
const headerElement = document.querySelector('header');

toggleHeader.addEventListener('click', function () {
  if (headerElement.classList.contains('green')) {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  } else {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  }
});
