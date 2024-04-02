# Manual Testing

## Home Page Testing
| Description | Steps | Expected Result | Actual Result |
| -------------|-------|-----------------|---------------|
| Page Load | Navigate to the Home page | Home page loads with header, main content, and footer |  |
| Navigation Bar Links | Verify that 'Home', 'Cosplay Hall of Fame', 'Login' and 'Register' links are present when unauthenticated | All navigation links are correctly displayed |  |
| Navigation Bar Links | Verify that 'Home', 'Cosplay Hall of Fame', 'Cosplay Submissions' and 'Logout' links are present when authenticated | All navigation links are correctly displayed |  |
| Responsive Design Check | Adjust browser size to simulate desktop, tablet, and mobile views | The page adjusts to different screen sizes without breaking the layout |  |
| Image Load Test | Verify that images load correctly | All images display without error |  |
| Footer Content Check | 1. Scroll to the footer 2. Verify that the "About" and "Disclaimer" content is correctly shown | Footer contains expected text  |  |

## Login Page Testing 
| Description | Steps | Expected Result | Actual Result |
|-------------|-------|-----------------|---------------|
| Page Load | Click 'Login' from the navigation bar | Login page loads with username and password fields |  |
| Field Validation | 1. Leave username and/or password empty 2. Submit the form | Error message for empty fields is shown |  |
| Successful Login | 1. Enter valid credentials 2. Submit the form | User is logged in and redirected to the homepage |  |
| Failed Login | 1. Enter invalid credentials 2. Submit the form | User returns to the login page to re-enter credentials |  |
| Sign up Form link | 1. Verify the presence of the Sign up link at the bottom of the login form 2. Click on the Sign up link | User gets redirected to Sign up form |  |

## Register Page Testing
| Description | Steps | Expected Result | Actual Result |
|-------------|-------|-----------------|---------------|
| Page Load | Click 'Register' from the navigation bar | Registration page loads with form fields for new user registration |  |
| Form Validation | Submit form with empty fields | Error message for empty fields is shown |  |
| Successful Registration | 1. Fill in all fields correctly 2. Submit the form 3. Redirect to Homepage | New user is registered, logged in and redirected to the homepage |  |
| Password Mismatch | 1. Enter mismatched passwords in the form 2. Submit the form | Error message for password mismatch is displayed |  |
| Email Format Check | 1. Enter an invalid email format in the email field 2. Submit the form | Error message for invalid email format is displayed |  |

## Cosplay submission (creation)
| Description | Steps | Expected Result | Actual Result |
|-------------|-------|-----------------|---------------|
| Page Load | Whilst authenticated, click 'Cosplay submission' from the navigation bar | Page loads with the submissions form |  |
| Form Validation | Submit form with empty fields | Error message for empty fields is shown |  |
| Successful Registration | 1. Fill in all fields 2. Submit the form | New submission is created and user is redirected to Cosplay Hall of Fame page |  |

## Cosplay submission (update)
| Description | Steps | Expected Result | Actual Result |
|-------------|-------|-----------------|---------------|
| Page Load | Whilst authenticated, click on 'edit' button in one of users' entries on Cosplay Hall of Fame | Cosplay Submission Form page loads with the submissions data populated in the form  |  |
| Form Validation | Submit form with empty fields | Error message for empty fields is shown |  |
| Successful Registration | 1. Fill in all fields correctly 2. Submit the form | New submission is created and user is redirected to Cosplay Hall of Fame page |  |


## Cosplay Hall of Fame (authenticated)
| Description | Steps | Expected Result | Actual Result |
|-------------|-------|-----------------|---------------|
| Page Load | Whilst authenticated, click 'Cosplay Hall of Fame' from the navigation bar | Page loads with list of submissions, users' pending submissions are shown with a semi-transparent overlay on the respective submission, and approved submissions are shown as normal | |
| Edit button | User Clicks on edit button | User gets redirected to the Cosplay Submission page with the form populated with the selected entries' data to edit |  |
| Delete button | User clicks on delete button | Submission is deleted from the entries list |  |

## Cosplay Hall of Fame (unauthenticated)
| Description | Steps | Expected Result | Actual Result |
|-------------|-------|-----------------|---------------|
| Page Load | Whilst unauthenticated, click 'Cosplay Hall of Fame' from the navigation bar | Page loads with list of published submissions | |

### Discovery/ies

During testing I noticed an issue on my mobile, where I was getting a CSRF token error when logging in. I first thought there was an issue with my logic, but it was strange because if I reloaded the page I was there logged in with a welcome message. I realised that when I was selecting the user from my saved name/passwords popup it was prefilling AND logging me in, and then I was hitting login which was essentially causing my login logic to trip up, hence the error. A somewhat edge case issue that unfortunately won't be solved in this iteration, but it feels good to come across strange issues to fix!