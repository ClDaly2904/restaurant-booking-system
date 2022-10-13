# Sushi & Sake | Japanese Kitchen

### Website for a fictional Japanese restaurant complete with booking system and account functionality

## Contents
- [About](#about)
- [User Experience](#user-experience)
    - [Target audiences](#target-audiences)
    - [User Stories](#user-stories)
    - [Sushi & Sake's Aims](#contact-book-aims)
    - [Iterations](#iterations)
    - [First Time Visitors](#first-time-visitors)
    - [Returning Visitors](#returning-visitors)
    - [User Journey](#user-journey)
    - [Colour Scheme and Fonts](#colour-scheme-and-fonts)
    - [Wireframes](#wireframes)
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

Potential customers can explore the website to find out more about the restaurant, create or login to their account, and book a table if required. Customers also have access to full CRUD functionality to manage their bookings or send a message to the restaurant.

The website also contains an admin panel where restaurant staff can view and manage all of the restaurants bookings in addition to any messages left for the restaurant.

A link to the live site can be found here. *************

## User Experience

### Target Audiences

- Adults between the ages of 25-70 who enjoy fine dining
- For users that already love Japanese cuisine, and are looking to find out more about Sushi & Sake as a new Japanese Kitchen to try
- For users that have enjoyed the Sushi & Sake experience before
- For users looking for inspiration to find out more about and to try Japanese cuisine
- For users that wish to book a table and manage their bookings
- For users wanting to find or contact the restaurant


### User Stories

Before writing any of the actual code for the Sushi & Sake website, I took some time to evalaute what users would typically expect from a restaurant website. I used GitHub's Project's feature to create a User Stories board that I updated as I went along to keep track of the User Goals that I had decided upon.

![Screenshot of user stories board](images/user-stories.png)

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
12. As a user, I would like the option to sign up to a newsletter to keep up to date with the latest offers (future implementation)

### Sushi & Sake's Aims

- To create a website that echoes the vibrant atmosphere of the Sushi & Sake Japanese Kitchen and draw in new customers
- To create a website that showcases and promotes the exciting cuisine to encourage users to make bookings
- Provide guests with a way to book a table at the restaurant
- Provde the restaurant staff with the means to be able to view any bookings made
- Provide the restaurant staff with the means to be able to manage bookings
- Provide the restaurant staff with the means to be able to view any messages sent to the restaurant
- To have the use of a booking system that prevents double bookings to avoid poor experiences for customers
- The restaurant would like a way to easily manage and update their menus with the revelevant food items, prices and dietary information
- As a restaurant owner, I would like a space to promote offers and events to encourage people to come to the restaurant (future implementation)

### Iterations

To take an Agile approach to the project, I planned the stages that I would carry out the work. I categorised each User Story into 'must have', 'Could have' and 'Should have'. At this current stage in the Sushi & Sake website, I completed all user stories apart from the two 'could have' items, which I decided early on were outside the scope for this stage as I wanted to concentrate on successfully implementing the booking system, along with messages functionality.

#### Iteration 1
I prioritised the 'Must have' items and, thanks to Django's built-in admin panel and utilising all-auth, the functionality for the restaurant manage bookings and for users to create accounts meant that Iteration 1 managed to include a lot of the 'must have' items in a relatively short amount of time. 

<br>

<details><summary>Iteration 1</summary>

![Iteration 1](images/iteration1.png)

</details>

<br>

#### Iteration 2
With iteration 2, I shifted my focus from completing the work for the restaurant booking management to finishing the CRUD functionality for customer users. I built the pages for customers to view their bookings, then added the functionality for customers to edit and delete their bookings.

I also began to build customer-facing pages such as the Sushi & Sake home page and the functionality to allow customers to view the menu.

In hindsight, this iteration was by far the largest and I would have been better leaving some of this work (such as implementing the home page) to iteration 3 to make each the workload in each stage a bit more even.

<details><summary>Iteration 2</summary>

![Iteration 2](images/iteration2.png)

</details>

<br>

#### Iteration 3
Iteration 3 was implementing the last of the planned functionalitites, the ability for users to leave contact messages for the restaurant. This largely included builing the contact model and validating the contact form. At the suggestion of my mentor, I also added the admin dashboard for restaurant staff to easily see bookings and messages outside of the django admin panel.

<details><summary>Iteration 3</summary>

![Iteration 3](images/iteration3.png)

</details>

<br>

#### Iteration 4
After all of the initially planned user stories were implemented, I spent some time fine-tuning the project to best support a positive user experience for both the restaurant and its customers. This included things like ensuring all of the forms had the correct validations, increasing brand presence through the use of the Sushi & Sake logo and adding a helper box for the booking form.

<details><summary>Iteration 4</summary>

![Iteration 4](images/iteration4.png)

</details>

<br>

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

### Colour Scheme and Fonts

After doing some research and browsing the websites of other Japanese restaurants, I got an idea of the feel I wanted to create for Sushi & Sake's website. For an elegant look, I decided to combine a background of darks and greys against striking yellow and red. Red is a very popular colour in Japan, and the yellow connotes the luxury of gold tones.

For the fonts, I chose Alegreya Sans for the headings and Assistant for the body. I selected these from Google Fonts as they are both simple and easy-to-read fonts, whilst Alegreya is still striking in a bright colour against the dark background

### Wireframes

Before building my site in Gitpod, I took all of the features I thought to be in scope and combined these with my design ideas to create wireframes in Balsamiq. This helped me to implement a consistent design across the Sushi & Sake website to enhance a cohesive feel.

- [Index wireframe](wireframes/index-wireframe.png)
- [Make booking wireframe](wireframes/book-wireframe.png)
- [Contact wireframe](wireframes/contact-wireframe.png)
- [User Bookings wireframe](wireframes/user-bookings-wireframe.png)
- [Admin Dashboard](wireframes/admin-dashboard-wireframe.png)

## Features

### Logo
For the website to have a strong sense of brand, I created a logo for Sushi & Sake, incorporating a piece of sushi in one of the restaurant's theme colours. The logo is most prevalant in the navigation bar but is also incorporated into some of the other pages on the site for continuity.

<details><summary>Sushi & Sake logo</summary>

![Logo](images/logo.png)

</details>

<br>

### Navigation bar
At the top of every page is the fixed navigation bar. It always contains links to the home page, menu, book and contact pages.
The other links in the navigation bar vary depending on what user is logged in to suit their needs and avoid frustration for pages they can't access.
If a user is not logged in, the last two links on the navbar are 'Register' and 'Log In'. If the person logged in is a customer, then the will have the option 'My Bookings' where they can update their bookings and the log out button. Lastly, if a member of staff at the restaurant is logged in, they will have the 'Admin Dashboard' available to them along with the log out button.
<details><summary>Admin navbar</summary>

![Admin navbar](images/admin-navbar.png)

</details>

<details><summary>Guest navbar</summary>

![Guest navbar](images/guest-navbar.png)

</details>

<details><summary>Navbar if user not logged in</summary>

![Navbar if usr not logged in](images/not-logged-in-navbar.png)

</details>

<br>

### Footer
As the website has a busy navbar and background, I decided to keep the design for the footer simple so as not to make the user's screen too complicated. The footer contains links to Sushi & Sake's social media to encourage them to engage with the restaurant.

<details><summary>Footer</summary>

![Footer](images/footer.png)

</details>

<br>

### Background
Whilst searching for a Japanese-themed background for the websit, I came across a koi carp background on [Pixabay](https://pixabay.com/). The dark grey of the background fits in well with the colour scheme of the website, and the koi carp on the pattern incorporates Japan's oriental style.

### About Us Section
After the hero image on the home page, the first thing that users scroll to is the 'About Us' section. This section is at the top of the page as it holds great importance, introducing new users to the restaurant and giving them a sense of what the restaurant is like.

<details><summary>About Us Section</summary>

![About us section](images/about-us.png)

</details>

<br>

### Gallery
Found on the home page, users can view a gallery containing images of the restaurant and the restaurant's food. This is a great feature for first-time users who are not sure what to expect from Sushi & Sake and showcases the elegant dining experience they can expect from the restaurant.

### Reviews
Also found on the home page, there is a section where users can read reviews about the restaurant. This addition helps to promote the restaurant and give users trust in it when they can see the positive experiences other people have had.

### Menu Page
Users can view the menu for Sushi & Sake on their website. Potential customers can read through the tantalising dishes available to see if Sushi & Sake is right for them, including their budgets and all-important dietary requirements. As this page is built using template tags based on the Food Item model objects, the restaurant can easily update the menu themselves from the Django backend administration panel. This benefits the restaurant as they do not have to pay to get the menu updated each time. It also pleases their customers who can see any new and exciting dishes as well as avoiding disappointment hoping for ones no longer on the menu! The menu is split into sections for easy readability and contains a key for allergen information.

### Contact Page
The contact page contains all important information for users of the Sushi & Sake site. It displays the restaurant's opening hours, telephone number, email, and address including a Google maps insertion. The Google map can be viewed in full screen to give the user directions to the restaurant.
At the bottom of the page, there is a contact form where users can leave a message for the restaurant. This message can be viewed by the restaurant in either the Django backend admininstration panel or, more easily, by the admin dashboard. The message form has fields for name, number, email and message so that the restaurant can see who has messaged them and so that they have the information to contact the customer back if necessary.

### Booking Page and Booking Form
The booking page contains two main elements- a help box at the top of the screen and the booking form itself. The help box outlines key information to help users input data such as opening times (the form will not submit if requested time is outside operating hours), and the maximum time they can book. This helps to streamline the booking process to lessen the chance of users getting frustrated and not continuing with the booking process.
The booking form itself contains clearly labelled fields with helper text so that users know what they should enter in each field. Users can pick their chosen table location, the number of guests the booking will be for, and their chosen booking start and end times. Each field has validation so that the form will not submit if the input data is not valid. If the booking is accepted, a flash message will confirm the reservation. If there is no available table for the booking time requested, the message will reflect this.
A successful booking will create a booking object that can be viewed by the guest in their 'my bookings' page, by the restaurant staff in the 'admin dashboard', or in the Django backend administration panel.

### Booking Management (Customer) and My Bookings Page
If a guest user is logged in, they can view a list of their bookings by clicking on the 'My Bookings' page. The page displays the information for each booking (time, date, number of guests) as well as the option to edit or delete each booking.

### Check availability function

### Accounts

### Call to action booking buttons

### Flash messages

### Booking management (Restaurant)

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