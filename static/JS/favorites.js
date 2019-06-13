// function displayUpdatedFavorites(results){
//     return $('.user-favorite-doctors-list').html(results.user_favorite_doctors.map((docs)=> {return `<ul><li>${docs}</li></ul>`;
//         }));

// }


// function updateFavoriteDoctors(event){
//     event.preventDefault();
//     console.log(event);

//     //let favoriteDoctor = {"firstName": $("#doctor_first_name").val(), "lastName": $("#doctor_last_name").val()};
//     let url = "/update-favorite-doctors";

//     $.get(url, displayUpdatedFavorites);
// }

// $(".button-favorite-current-doctor").on('click', updateFavoriteDoctors);

// // TODO: Fix toggle to check if already favorited. Bug fix.
// $(".button-favorite-current-doctor").click(function(){

//         $(this).text($(this).text() == 'Favorite The Doctor Above!' ? 'Unfavorite The Doctor Above' : 'Favorite The Doctor Above!');
//     });





// // TODO: this is to display the favorite players. I should use this on the homepage
// function displayUpdatedFavorites(results){
//     return $('#user-favorite-doctors-list').html(results.user_favorite_doctors.map((docs)=> {return `<ul><li>${docs}</li></ul>`;
//         }));

// }

