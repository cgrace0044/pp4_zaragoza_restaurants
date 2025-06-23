### Lighthouse

Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility and performance. 

| Page           | Performance  | Accessibility | Best Practices  | SEO |
|----------------|:------------:|:-------------:|:---------------:|:---:|
|                |              |               |                 |     |
| Desktop        |              |               |                 |     |
| Home           |           87 |           100 |             100 | 100 |
| Restaurants    |           99 |           100 |             100 | 100 |
| Rest Detail    |           96 |           100 |             100 | 100 |
| About          |           77 |           100 |             100 | 100 |
| Contact        |           99 |           100 |             100 | 100 |
| Favourites     |           85 |           100 |             100 | 100 |
| Login          |           100|           100 |             100 | 100 |
| Logout         |           98 |           100 |             100 | 100 |
| Register       |           98 |           100 |             100 | 100 |
|                |              |               |                 |     |
| Mobile         |              |               |                 |     |
| Home           |           75 |           100 |             100 | 100 |
| Restaurants    |           89 |           100 |             100 | 100 |
| Rest Detail    |           72 |           100 |             100 | 100 |
| About          |           89 |           100 |             100 | 100 |
| Contact        |           93 |           100 |             100 | 100 |
| Favourites     |           84 |           100 |             100 | 100 |
| Login          |           93 |           100 |             100 | 100 |
| Logout         |           94 |           100 |             100 | 100 |
| Register       |           94 |           100 |             100 | 100 |

## Manual Testing

### Home Page
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| G. Started Restaurants Link| Click                                     | Redirect to browse_restaurants page        | Pass      |
| G. Started Contact Link    | Click                                     | Redirect to contact page                   | Pass      |
| G. Started About Link      | Click                                     | Redirect to about page                     | Pass      |
| G. Started Login Link      | Click                                     | Redirect to login page                     | Pass      |
| Login link                 | logged in/ logged out                     | login link only displays when not logged in| Pass      |

### Django All Auth Pages
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Register                   |                                           |                                            |           |
| Log in link                | Click                                     | Redirect to login page                     | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Leave empty                               | Error message displays                     | Pass      |
| Username field             | Insert duplicate username                 | On submit: form won't submit               | Pass      |
| Username field             | Insert duplicate username                 | Error message displays                     | Pass      |
| Email field                | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Email field                | Insert incorrect format                   | Error message displays                     | Pass      |
| Email field                | Insert correct format                     | On submit: form submit                     | Pass      |
| Email field                | Leave empty - email field optional        | On submit: form submit                     | Pass      |
| Email field                | Insert duplicate email                    | On submit: form won't submit               | Pass      |
| Email field                | Insert duplicate email                    | Error message displays                     | Pass      |
| Password field             | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Password field             | Insert incorrect format                   | Error message displays                     | Pass      |
| Password field             | Passwords don't match                     | On submit: form won't submit               | Pass      |
| Password field             | Passwords don't match                     | Error message displays                     | Pass      |
| Password field             | Insert correct format and passwords match | On submit: form submit                     | Pass      |
| Sign Up button(form valid) | Click                                     | Form submit                                | Pass      |
| Sign Up button(form valid) | Click                                     | Redirect to home page                      | Pass      |
| Sign Up button(form valid) | Click                                     | Success message confirming login appears   | Pass      |
| Sign Up button(form valid) | Click                                     | Success message fades after 2 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log in                     |                                           |                                            |           |
| Sign up link               | Click                                     | Redirect to sign up page                   | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Leave empty                               | Error message displays                     | Pass      |
| Username field             | Insert wrong username                     | On submit: form won't submit               | Pass      |
| Username field             | Insert wrong username                     | Error message displays                     | Pass      |
| Password field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Password field             | Leave empty                               | Error message displays                     | Pass      |
| Password field             | Insert wrong password                     | On submit: form won't submit               | Pass      |
| Password field             | Insert wrong password                     | Error message displays                     | Pass      |
| Login button(form valid)   | Click                                     | Form submit                                | Pass      |
| Login button(form valid)   | Click                                     | Redirect to home page                      | Pass      |
| Login button(form valid)   | Click                                     | Success message confirming login appears   | Pass      |
| Login button(form valid)   | Click                                     | Success message fades after 2 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log Out Confirmation       |                                           |                                            |           |
| Logout button              | Click                                     | Redirect to homepage                       | Pass      |
| Logout button              | Click                                     | Success message confirming log out appears | Pass      |
| Logout button              | Click                                     | Success message fades after 2 seconds      | Pass      |

## Bugs 

### Fixed Bugs

- #### Summernote font styling
     - **Bug**: When creating restaurant reviews sometimes summernote would override my custom CSS. 
     - **Fix**: By clicking the button 'remove font style' in the summernote fields on the Django Administration site I solved this issue.

- #### Autofill styling in forms not in line with form styling
     - **Bug**: Having filled out the forms once, the autofill functionality would style the input fields using default styling.
     - **Fix**: By targeting 'input:-webkit-autofill' within my CSS file I was able to resolve this error.

- #### Contact form success message displaying multiple times
     - **Bug**: Within the contact form the success message was showing multiple times.
     - **Fix**: Within the if function in the contact_us view I wasn't resetting the form. Once I added contact_form = ContactForm() following the messages display this resolved this issue.

- #### Having to dismiss multiple Django message alerts
     - **Bug**: The site is very interactive and multiple Django messages are displayed to give feedback to the user. Having to dismiss all these alerts manually makes for a poor user experience.
     - **Fix**: I setup a function within my script.js file to automatically dismiss Django message alerts after two seconds. This really improves the user experience.

- #### Blank line appearing once Django message alerts dismissed
     - **Bug**: Once I added the JS function to automatically dismiss Django message alerts a blank white line was appearing at the top of the page.
     - **Fix**: I added a line to my JS function to remove the alert container if no more alerts were present. This got rid of the blank white line.

- #### Footer not staying at bottom of screen
     - **Bug**: Footer not staying at the bottom of the screen when displaying on pages without fullscreen content and didn't want to use a sticky footer. 
     - **Fix**: Was able to utilise the calc() CSS function and make the page content 100% of the viewport height less the height of the footer and this solved the problem. 

### Unfixed bugs:
There are no known unfixed bugs. 