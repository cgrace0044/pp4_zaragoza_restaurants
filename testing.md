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
| Login link                 | Logged in/ Logged out                     | login link only displays when not logged in| Pass      |

### Restaurants Page
| Element                    | Action                         | Expected Result                                                             | Pass/Fail |
|----------------------------|--------------------------------|-----------------------------------------------------------------------------|-----------|
| Restaurant Card            | Display correct content        | Displays correct title, restaurant name and image                           | Pass      |
| Restaurant Card            | Click                          | Clicking inside restaurant card brings you to correct restaurant detail page| Pass      |
| Restaurant Card            | Pagination                     | 8 restaurant cards will appear per page                                     | Pass      |
| Restaurant Card            | Hover                          | Hovering over a restaurant card creates the desired box shadow effect       | Pass      |
| Restaurant Card            | Media Display                  | 4 restaurants appearing per row on desktop, 3 on tablet and one on mobile   | Pass      |
| Link                       | Pagination link                | Pagination arrow takes you to the next set of restaurant reviews            | Pass      |
| Link                       | Pagination link                | On the second page or more a back arrow pagination button appears           | Pass      |
| Link                       | Pagination Hover               | Hovering over the pagination link creates the desired box shadow effect     | Pass      |

### Restaurant Detail Page

| Element                        | Action              | Expected Result                                                                                                         | Pass/Fail |
|--------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Restaurant Review Content      | Display             | Display correct post title, restaurant name, location, price, description and restaurant image                          | Pass      |
| Add to favourites button       | Display             | Only visible if user is logged in                                                                                       | Pass      |
| Add to favourites button       | Hover               | Hovering over the add to favourites button creates the desired box shadow effect                                        | Pass      |
| Add to favourites button       | Click               | Restaurant is added to user's favourites page                                                                           | Pass      |
| Add to favourites button       | Click               | Success message appears informing the user that the 'restaurant name' has been added to their favourites                | Pass      |
| Add to favourites button       | Click               | Success message fades after 2 seconds                                                                                   | Pass      |
| Remove from favourites button  | Display             | Only visible if user is logged in.                                                                                      | Pass      |
| Remove from favourites button  | Hover               | Hovering over the remove from favourites button creates the desired box shadow effect                                   | Pass      |
| Remove from favourites button  | Click               | Restaurant is removed from user's favourites page                                                                       | Pass      |
| Remove from favourites button  | Click               | Success message appears informing the user that the 'restaurant name' has been removed from their favourites            | Pass      |
| Remove from favourites button  | Click               | Success message fades after 2 seconds                                                                                   | Pass      |
| Like Button                    | Display             | Only visible if user is logged in                                                                                       | Pass      |
| Like Button                    | Hover               | Hovering over the like button creates the desired box shadow effect                                                     | Pass      |
| Like Button                    | Click               | Restaurant is liked by the user                                                                                         | Pass      |
| Like Button                    | Click               | Click the like button a second time and the restaurant is unliked by the user                                           | Pass      |
| Like Button                    | Click               | Like count is incremented by one when a user likes a post                                                               | Pass      |
| Like Button                    | Click               | Like count is decremented by one when a user unlikes a post                                                             | Pass      |
| Like Button                    | Click               | Success message appears informing the user they have liked the restaurant (restaurant is named)                         | Pass      |
| Like Button                    | Click               | Message appears informing the user they have unliked a restaurant (restaurant is named)                                 | Pass      |
| Like Button                    | Click               | Messages fade automatically after 2 seconds                                                                             | Pass      |
| Login to Interact Button       | Display             | Login to Interact Button appears instead of like/favourites button when user is not logged in                           | Pass      |
| Login to Interact Button       | Click               | User is redirected to login page                                                                                        | Pass      |
| Login to Interact Button       | Hover               | Hovering over the Login to Interact button creates the desired box shadow effect                                        | Pass      |
| Write a Comment Button         | Display             | Only displays if user is logged in                                                                                      | Pass      |
| Write a Comment Button         | Click               | Clicking on write a comment opens the 'leave a comment' modal                                                           | Pass      |
| Write a Comment Button         | Hover               | Hovering over the write a comment button creates the desired box shadow effect                                          | Pass      |
| User Comments                  | Display             | Comments are in ascending order                                                                                         | Pass      |


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