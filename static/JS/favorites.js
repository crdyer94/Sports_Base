// // get favorites from local storage or empty array
// var favorites = JSON.parse(localStorage.getItem('favorites')) || [];
// // add class 'fav' to each favorite
// favorites.forEach(function(favorite) {
//   document.getElementById(favorite).className = 'fav';
// });
// // register click event listener
// document.querySelector('.list').addEventListener('click', function(e) {
//   var id = e.target.id,
//       item = e.target,
//       index = favorites.indexOf(id);
//   // return if target doesn't have an id (shouldn't happen)
//   if (!id) return;
//   // item is not favorite
//   if (index == -1) {
//     favorites.push(id);
//     item.className = 'fav';
//   // item is already favorite
//   } else {
//     favorites.splice(index, 1);
//     item.className = '';
//   }
//   // store array in local storage
//   localStorage.setItem('favorites', JSON.stringify(favorites));
// });

// // local storage stores strings so we use JSON to stringify for storage and parse to get out of storage





// // TODO: this is to display the favorite players. I should use this on the homepage
// function displayUpdatedFavorites(results){
//     return $('#user-favorite-doctors-list').html(results.user_favorite_doctors.map((docs)=> {return `<ul><li>${docs}</li></ul>`;
//         }));

// }


// function updateFavoriteDoctors(event){
//     event.preventDefault();

//     let url = "/update-favorite-doctors"; //TODO: Merge Set favorite and Remove favorite into one route to handle this

//     $.get(url, displayUpdatedFavorites);
// }

// $("#button-favorite-current-doctor").on('click', updateFavoriteDoctors);



// $("#button-favorite-current-doctor").click(function(){
//         $(this).text($(this).text() == 'Favorite This Doctor!' ? 'Unfavorite This Doctor' : 'Favorite This Doctor!');
//     });