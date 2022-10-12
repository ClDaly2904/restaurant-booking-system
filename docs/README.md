# Sushi & Sake | Japanese Kitchen

### Website for a fictional Japanese restaurant complete with booking system and account functionality

## Contents
- [About](#about)
- [User Experience](#user-experience)
    - [Target audiences](#target-audiences)
    - [User Stories](#user-stories)
    - [Sushi & Sake's Aims](#contact-book-aims)
    - [First Time Visitors](#first-time-visitors)
    - [Returning Visitors](#returning-visitors)
    - [User Journey](#user-journey)
- [Features](#features)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-tested)
    - [Fixed bugs](#fixed-bugs)
    - [Validators](#validators)
- [Deployment](#deployment)
- [Credits](#credits)

## About

![Am I responsive screenshot](images/am-i-responsive.png)

Sushi & Sake Japanese Kitchen is a website for a fictional Japanese restaurant. The code was written in Gitpod, with the repository stored in GitHub and hosted on Heroku with a PostGres SQL database.

Potential customers can explore the website to find out more about the restaurant, create or login to their account, and book a table if required. Customers can also login to manage their bookings or send a message to the restaurant.

The website also contains an admin panel where restaurant staff can view and manage all of the restaurants bookings in addition to any messages left for the restaurant.

A link to the live site can be found here. *************

## User Experience

### Target Audiences

- For users that already love Japanese cuisine, and are looking to find out more about Sushi & Sake as a new Japanese Kitchen to try
- For users that enjoy dining out
- For users that have enjoyed the Sushi & Sake experience before
- For users looking for inspiration to find out more about and to try Japanese cuisine
- For users that wish to book a table and manage their bookings
- For users wanting to find or contact the restaurant


### User Stories

Before writing any of the actual code for the Sushi & Sake website, I took some time to evalaute what users would typically expect from a restaurant website. I used GitHub's Project's feature to create a User Stories board that I updated as I went along to keep track of the User Goals that I had decided upon.

**************![Screenshot of user stories board]()*************

1. As a user, I need to be able to navigate around the site
2. As a user, I need to be able to book a table for a specific time and amount of people
3. As a user, I need to be able to edit my booking
4. As a user, I need the option to delete my booking
5. As a user, I need to be able to create an account
6. As a user, I need to be able to log in to my account
7. As a user, I need to book tables that are actually available to avoid disappointment
8. As a user, I want to be able to see what experiences other people have had at Sushi & Sake restaurant
9. As a user, I want to be able to see pictures of the food to help me understand what to expect
10. As a user, I want to be able to view an up-to-date menu so that I can see what food I can expect at Sushi & Sake, with the relevant food items, prices and all-important dietary information
11. As a user, I want ways to communicate with the restaurant by contacting them directly through contact information or by leaving a message for the restaurant

### Sushi & Sake's Aims

- To create a website that echoes the vibrant atmosphere of the Sushi & Sake Japanese Kitchen and draw in new customers
- To create a website that showcases and promotes the exciting cuisine to encourage users to make bookings
- Provide guests with a way to book a table at the restaurant
- Provde the restaurant staff with the means to be able to view any bookings made
- Provide the restaurant staff with the means to be able to manage bookings
- Provide the restaurant staff with the means to be able to view any messages sent to the restaurant
- To have the use of a booking system that prevents double bookings to avoid poor experiences for customers
- The restaurant would like a way to easily manage and update their menus with the revelevant food items, prices and dietary information

### First Time Visitors

- Visitors are greeted by an eyecatching landing page when they first visit the site, with clear brand prescence and 'Sushi & Sake Japanese Kitchen' message so that the purpose of the site is clear
- The landing page provides contains 'About us', 'Gallery' and a 'What our customers say' sections to give first time visitors a real feel for what Sushi & Sake is about and what they might expect from a dining experience at the restaurant
- The menu bar at the top gives a clear way for users to navigate between the pages of the site
- First time visitors can view the restaurant's menu so they can see what food is served and decide if they might like to eat there
- The page to book a table is clearly visible for those that decide they want to book a table
- If a user does not have an account, they are redirected to the page to sign up for an account
- The booking form is simple, with helper text and a guide to booking rules at the top of the page
- Flash messages provide feedback for confirming logins and bookings
- If new users wish to make an enquiry to the restaurant, there is a contact page that displays contact information and a clear contact form for the restaurant


### Returning Visitors

- Returning visitors can see the most up-to-date menu
- Returning visitors are most likely to utilise the booking system, as they will be the most likely to be visiting the site in order to book a table or manage their bookings
- The eyecatching design of the Suhsi & Sake website is pleasing to both new and returning visitors
- The contact form is clear for those returning visitors wishing to leave feedback about their experience


### User Journey

1. As a user, I arrive on the land page where a title immediately confirms that I am on the website for the Sushi & Sake Japanese Kitchen
2. As I scroll through the Sushi & Sake home page, there is a section where I can read about the restaurant, further down is a gallery that shows images of the delicious food and the restaurant, and finally some reviews from people that have been there
3. The navigation page at the top has a logo that I can recognise across the site
4. On the navigation bar I can see a large button encouraging me to book a table, along with options to view the menu, contact the restaurant, and to sign in or register for an account
5. I want to find out more about what food I can try before I decide to book a table, so I select the menu page where I am provided with a clearly separated and laid out menu with headings, prices, dietary information and descriptions so I know what the dishes are
6. Having found some dishes I would like I try, I decide to book a table so press on the large 'book now' button. The page tells me that I have to create an account to book a table and redirects me to a page where I can do so. After a quick sign-up process, I log in and  I can return to the page to book a table. Flash messages confirm when I have created an account and have signed in.
7. There is a help box at the top of the page followed by a labelled up form. If I input something wrong, the form comes up with an error message. When all the information is correct, I can press the 'book now' button and a message flashes at the top to confirm that my table has been booked, and the details.
8. The navigation bar now includes a 'My Bookings' tab, when I click on this I can see the booking I have made and that I have the option to edit or cancel my booking.

Whilst planning the functionality for the Sushi & Sake website, I had to consider how I was going to achieve both the aims for the user and the restaurant. This led to the creation of the features found in the Features section.


## Features

## Credits

### Form validation and inputs
- Form validation [mdn web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
- Form validation, setting aware datetime/time objects - this [article by Adam Smith](https://www.adamsmith.haus/python/answers/how-to-set-the-timezone-of-a-datetime-in-python)
- Form validation, using date util by [Bloomberg](https://www.bloomberg.com/company/stories/work-dates-time-python/)
- Form validation, using date util [Programiz](https://www.programiz.com/python-programming/examples/string-to-datetime)
- Form validation, extracting time from datetime object [Geeks for Geeks](https://www.geeksforgeeks.org/extract-time-from-datetime-in-python/)
- Form validation, calculating the time difference between two datetime objects [GeekFlare](https://geekflare.com/calculate-time-difference-in-python/)
- Implementing widgets for form inputs [Django Project](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/)

### Other
- Although I ended up greatly varying the booking logic from my inital code (see bugs in testing), I watched a couple of videos from [DarshanDev on YouTube](https://www.youtube.com/watch?v=-9dhCQ7FdD0&ab_channel=DarshanDev). His tutorials helped me to set up my booking model, my BookingView and the initial availability logic
- Updating URLS with ids [Open Classrooms](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform)
- Managing users with different access levels [Real Python](https://realpython.com/manage-users-in-django-admin/)
- For setting up the project shell and database, I used the [Code Institute's](https://codeinstitute.net/) CodeStar Django Blog project
- Koi karp background used for theme throughout website found on [Pixabay](https://pixabay.com/vectors/koi-carp-pattern-japanese-3338735/)
- All of the images used on the site were found on [Pixabay](https://pixabay.com/) or [Unsplash](https://unsplash.com/) and then hosted on Cloudinary

### General
- [Django documentation](https://docs.djangoproject.com/en/4.1/)
- [Python3 documentation](https://docs.python.org/3/)
- [W3 Schools](https://www.w3schools.com/python/)
- As always, [Stack Overflow](https://stackoverflow.com/questions/36432954/ was a great resource for troubleshooting

### Inspiration
For the design on Sushi & Sake's website, I took inspiration from other Japanese restaurants. One of my favourite local restaurants, [Kibou](https://kibou.co.uk/) not only has delicious food but also a visually stunning website that helped me cultivate the elevated feel of the Sushi & Sake website. I also browsed the [Yo! Sushi website](https://yosushi.com/) for menu ideas.