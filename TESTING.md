# Manual Testing

## Lighthouse results

Lighthouse results were good overall, but I hadn't taken into consideration the size of the image uploads from community members, so without proper functionality on the media uploads, the score is brought down.

![hall_of_fame_mobile](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/983e2084-c1d6-4a90-b6e3-bb565c5c8336)
![home_desktop](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/c9194e39-9f47-456f-a079-eee4b89fabc8)
![home_mobile](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/f3cd54b7-b0f9-4c60-944b-ae34b66738f4)
![blog_post_desktop](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/b5295045-e90c-4645-8c1e-b33de00fe496)
![blog_post_mobile](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/6ce9c8be-23ac-4a0d-bd64-865498e6277d)
![hall_of_fame_desktop](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/cb065cea-c78a-4c70-841f-1a16cfb902a6)

## HTML Validator

There were a couple of errors I would have liked to fix, but I focused on removing the errors (see latest commits for HTML validator fixes) one remained regarding the img tag on my cosplay submissions but by nature this doesn't have a source attribute by default as it's an image upload from the user, so I didn't see a way around that at this time.

![register_report](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/8f62143f-988f-4d87-af0d-c5c4e4988de0)
![submission_report](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/ea09bd33-09da-4a73-8281-c59118921c61)
![blog_post_report](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/9fa9add3-ff63-4ee7-a768-4f8517620913)
![hall_of_fame_report](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/f83aa6da-97d5-4336-894b-7ba5bc89f299)
![home_report](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/f9f67af9-c977-4631-94fa-02c0fc7a5c7a)
![login_report](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/c4afbc5b-8d8e-466c-b5e4-ed39c84749dc)


## Pep8 results

All .py files were run through the CI Linter and any adjustments to curb the 80 character limit were implemented. A couple of # noqa was added to comments or lines I couldn't see a way to split without breaking functionality.

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
