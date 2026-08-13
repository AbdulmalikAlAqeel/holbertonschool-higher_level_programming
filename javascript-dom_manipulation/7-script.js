#!/usr/bin/node
const moviesList = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      moviesList.appendChild(listItem);
    });
  });
