# Testing

- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-tested)
- [Fixed bugs](#fixed-bugs)
- [Validators](#validators)

## Manual Testing

### Validators
#### W3C Html Validator
I ran all of the html templates used through the W3C html validator.
Upon originally running the tests, there were a couple of unclosed divs and a few instances where there was an error from button elements being the child of an anchor tag. I fixed these errors prior to my final deployment and now no errors show.

<details><summary>Homepage HTML Validation</summary>

![Homepage HTML Validation](images/testing/home-html-val.png)

</details>

<br>

<details><summary>Login HTML Validation</summary>

![Login HTML Validation](images/testing/login-html-val.png)

</details>

<br>

<details><summary>Menu HTML Validation</summary>

![Menu HTML Validation](images/testing/menu-val.png)

</details>

<br>

#### W3C CSS Jigsaw Validator
After running my style.css file through the CSS validator, there were no errors or warnings to show.

<details><summary>CSS Validator</summary>

![CSS Validator](images/testing/css-validation.png)

</details>

<br>

#### Pep8 Python Validator
I used GitPod's built in Pep8 Python Validator to check my Python code for errors. After going back and adjusting a lot of lines so that they didn't exceed the acceptable line length, the only supposed 'errors' showing were to do with Django models not having an objects member. Other than this, no actual errors were found.

As Gitpod shows errors in the problems window down by the terminal, I was able to eliminate syntax errors as I was writing my code.

<details><summary>Pep8 Python Validator</summary>

![Python Validator](images/testing/pep8-validator.png)

</details>

<br>

#### Lighthouse SEO
I ran different pages from Sushi & Sake's website through Chrome Dev Tool's Lighthouse validator, which gave high results in the 90s.

<details><summary>Homepage Lighthouse Validator</summary>

![Homepage Ligthouse](images/testing/home-lighthouse.png)

</details>

<br>

<details><summary>Contact Page Lighthouse Validator</summary>

![Contact Ligthouse](images/testing/contact-lighthouse.png)

</details>

<br>

<details><summary>Menu Lighthouse Validator</summary>

![Menu Ligthouse](images/testing/menu-lighthouse.png)

</details>

<br>

<details><summary>Booking Page Lighthouse Validator</summary>

![Book Ligthouse](images/testing/book-lighthouse.png)

</details>

<br>