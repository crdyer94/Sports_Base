function hideLoader() {
    $('#loading').hide();
}

$(window).ready(hideLoader);


setTimeout(hideLoader, 20 * 1000);

function showLoader() {
  var x = document.getElementById("searchresultcards");
  x.innerHTML="<img class = 'loading'; src= '/static/nfl.gif'>";

}

function showStats() {
  var x = document.getElementById("athletestats");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function showTweets() {
  var x = document.getElementById("athletetweets");
   if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function showArrests() {
  var x = document.getElementById("athletearrests");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
