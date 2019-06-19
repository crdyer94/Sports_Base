# Sports Base

Sports Base is an app that lets users search and favorite athletes in the National Football league. Each player has his own profile that shows his general bio information, recent career stats, recent tweets, and his arrest records. The data displayed on the athlete's profile is pulled from the mysportsfeed API, NFL Arrests API and the Twitter API. When an athlete is favorited, a shortcut to that athlete's profile is displayed on the user's homepage.  

## Contents
* [Tech Stack](#technologies)
* [Features](#features)
* [Installation](#install)
* [About Me](#aboutme)

## <a name="technologies"></a>Technologies
Backend: Python, Flask, PostgreSQL, SQLAlchemy<br/>
Frontend: JavaScript, Jinja2, Bootstrap, HTML, CSS<br/>
APIs: mysportsfeed, NFL Arrests, Twitter<br/>

## <a name="features"></a>Features

###Login 
The users can register or login from the login page. Signing up allows the user's information to be saved in the database.

![Login](/Screenshots/loginpage.jpg)

###Homepage
The user is forwarded to the homepage. The homepage displays that user's favorited players. Clicking one of these players will directly route the user to that athlete's profile.

![Homepage](/Screenshots/homepage.jpg)

As the profile loads, a graphic displays

![Loading](/Screenshots/loading.jpg)

###Athlete Profile
The athlete profile page shows the bio information, recent career stats, recent tweets, and any arrest records. The athlete bio info and the career stats are pulled from the mysportsfeed API.

![Profile](/Screenshots/athleteprofile.jpg)

The buttons on the profile allow users to choose to either display or not display certain information. The tweets are pulled from the Twitter API.

![Tweets](/Screenshots/showtweets.jpg)

The arrest records are pulled from the NFL Arrests API. 

![Arrests](/Screenshots/showarrests.jpg)


###Player Search
The search bar to search for players is available on every page of Sports Base. The search results shows the direct routes to the athlete's profile. All the data shown is pulled from the mysportsfeed API.

![Player Search](/Screenshots/searchresults.jpg)




## <a name="install"></a>Installation

To run Sportsbase:

Install PostgreSQL (Mac OSX)

Clone or fork this repo:

```
https://github.com/crdyer94/Sports_Base
```

Create and activate a virtual environment inside your Sports Base directory:

```
virtualenv env
source env/bin/activate
```

Install the dependencies:

```
pip install -r requirements.txt
```


## <a name="aboutme"></a>About Me
Camille Dyer is a Software Engineer in the Bay Area; this is her first project.
Visit her on [LinkedIn](http://www.linkedin.com/in/crdyer94).

