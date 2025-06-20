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