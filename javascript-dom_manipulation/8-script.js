#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  const helloDiv = document.querySelector('#hello');
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  fetch(url)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      helloDiv.textContent = data.hello;
    });
});
