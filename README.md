# GeekHaven - Personal Blog

(title image placeholder)

Visit the deployed site:

I plan to create a simple yet rewarding personal blog of my cosplay and gaming adventures.

## CONTENTS

* [User Stories](#user-stories)

* [Design](#design)
	* [Accessibility](#accessibility)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)

* [Technologies Used](#technologies-used)
	* [Languages Used](#languages-used)
	* [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Iteration over starting code](#iteration-over-starting-code)

* [Deployment & Local Development](#deployment--local-development)
	* [Deployment](#deployment)
	* [Local Development](#local-development)
	* [How to Fork](#how-to-fork)
	* [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Bug Fixes](#bug-fixes)

* [Credits](#credits)

* [Code Used](#code-used)

* [Content](#content)

* [Acknowledgments](#acknowledgments)

- - - 

## User Stories

| Epic | User Story  |
|--------------|---|
| Unauthenticated User | As an Unauthenticated User, I want to view the homepage so I can browse the content  |  
|              | As an Unauthenticated User, I want to click on a nav bar so I can navigate to the selected content   |
|              | As an Unauthenticated User, I want to register an account by clicking Login/Register so I can join the community |
|              | As an Unauthenticated User on the Login/Register page, I want to sign in once I have created an account so I can start engaging with the content 
|              | As an Unauthenticated User, I want to click on a blog so I can view the content  | 
|              | As an Unauthenticated User, I want to read comments left by Authenticated Users  |
|              | As an Unauthenticated User on the comments section, I want to log in or register an account via the buttons provided | 
| Authenticated User             | As an Authenticated User I want to comment on a post to engage with the admin/community |  
|              | As an Authenticated User I want to like/unlike posts so I can feel involved  | 
|              | (addon) As an Authenticated User I want to edit/delete my own comments so I can have control over my content  | 
|   Site Admin           | As a Site Admin I want to create, update, upload images and delete my posts so I can control the content of my blog  | 
|              | As a Site Admin I want to approve or disapprove comments so I can ensure a good tone is kept in the comments section   | 
|              | As a Site Admin I want to delete comments that I've previously approved to ensure full control of my blog content  |
|              | (addon) As a Site Admin I want user comments to go through a validation against a set of banned words, so that they can be automatically rejected |
  

- - -

## Design

* Colour palette - My first idea is a palette i found on Coolor, it appeals to me as it's my personal blog, whilst also giving Cyberpunk vibes which adds to its gamification. The very vibrant pink will only be used for a few outlines so as not to give anyone a headache!

![preliminary colour palette](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/0902544c-cf91-473e-ac5f-304ea954586d)

After choosing this colour palette I was introduced t o Tailwind CSS Color Generator and took one of the hexcodes from it, adjusted the hue to a more pastel shade, and exported the hexcodes to my Tailwind config.

![updated colour palette](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/ad83f848-9bd3-4429-97f9-eed7d5db3e1e)


I spent some time researching gaming and cosplay blogs and found that I preferred the more minimalist style. Too much information made it more like a news site (such as [Kotaku.com](https://kotaku.com/) ) but sites like [The Gaming Blog](https://thegamingblog.co.uk/) were more clear and concise, and more blog-like to me.

I liked the enlarged header and footer design of The Gaming Blog, as well as the very centered content with a lot of empty space on the sides, even on my small laptop the content wasn't spread out too much, so I will try to implement something similar:

![the-gaming-blog-header-nav](https://github.com/emmy-codes/Star-Trek-Museum/assets/70635859/13cd4718-c66b-41a5-9311-706ee310e135)

The blog content heading suited my style much more from Kotaku, so I will use that as a base for my blog posts:

![kotaku_blog_header_preview](https://github.com/emmy-codes/Star-Trek-Museum/assets/70635859/ac560aa9-d221-4833-89ad-76593b464dfb)

For the login pages I had a quick Google of login/signup pages and really liked the design of [this envatoelements design](https://elements.envato.com/login-page-screen-02-DQUHPP?irgwc=1&clickid=3BdW0o0pXxyPRuQxyZSGN09uUkH1ljy9Xwq5UQ0&iradid=298927&utm_campaign=elements_af_78798&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Speckyboy%20Design%20Magazine) both in colour scheme and cleanliness of the layout. 

### Accessibility

Plans for accessibility:

* Semantic HTML
* Descriptive alt text for images
* Ensure good colour contrast for visually impaired users with [Colour Contrast Analyzer](https://www.tpgi.com/color-contrast-checker/)
* Colour blindness: I did some research on the most common types of colour blindness and other than the vibrant pink (which will make up a small, small portion of the site) the rest of the colours still looked OK together.

### Imagery

The imagery for the blog will either be photographs from my projects, free images on the internet or perhaps AI generated if I need something specific.

### Wireframes
  
![login page](https://github.com/emmy-codes/windows-95/assets/70635859/582402ed-25e7-4796-aae5-b5f9e3dfef06)
![blog page](https://github.com/emmy-codes/windows-95/assets/70635859/dee114d6-ff61-4642-937b-4621b567025b)
![chat page not signed in](https://github.com/emmy-codes/windows-95/assets/70635859/67c6db23-e558-4806-8166-aa457a7406ec)
![chat page](https://github.com/emmy-codes/windows-95/assets/70635859/6ac17dce-e906-4620-8782-6410f31a1ec4)
![sign up page](https://github.com/emmy-codes/windows-95/assets/70635859/cee5ffd1-2713-426a-84b3-f2671627de18)
![homepage](https://github.com/emmy-codes/windows-95/assets/70635859/d02a8b57-8332-4cca-8aaa-c474c48c22fb)

### Features

- - - 

## Technologies Used

### Languages Used
 
HTML
CSS
JavaScript
Python
Tailwind CSS and components

### Frameworks, Libraries & Programs Used

[Github](https://github.com/) - For online storage of code and deployment.

[Picresize](https://picresize.com/) - Used to resize images for Readme/Testing docs.

[VS Code](https://code.visualstudio.com/) - For writing my code.

[Heroku](https://dashboard.heroku.com/apps) - For deploying my program.

[Grammarly](https://app.grammarly.com/) - For grammatical adjustments.

[Materialize](https://materializecss.com/) - Framework to make responsive front-end solutions.

[Django](https://www.djangoproject.com/) - To build my CRUD functionality.

[PostgreSQL](https://www.postgresql.org/) - For my Database.

[Cloudinary](https://cloudinary.com/) - For hosting blog images.

[Coolors](https://coolors.co/) - To create colour palettes.

[Tailwind CSS color generator](https://uicolors.app/) - To generate a CSS palette for Tailwind.

- - -
  

## Iteration over starting code

Here I will take you through some of my thought processes and first iterations of code to help see my learning and problem solving process.

I did a mix of utilizing the information from Code Institute's "I think therefore I blog" material, and trying to do it myself to see how much I'd learned. 

One of the first issues I encountered was setting up my blog post class. After a few hiccups everything migrated correctly and I could access the admin panel and see the button to add a blog post. I went in, only to realise that I had no field for the bulk of my blog content.

![bug_1_no_blog_content](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/ce42cb49-2526-4a9b-8940-d26f8df47ba2)

I checked my class on models.py - there was my blog_content attribute! But it wasn't showing up on the admin panel... so I checked my migration 0001_initial.py and checked what had been migrated.
No blog_post.
This lead me to do a quick check and yes, it was mean to have brackets on the end of my TextField type. A small error that wasn't picked up in any code compiling but still caused an undesired result. All it took was a () (and a default parameter) and a new migration to fix!

![bug1 textfield issue](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/c83d2c81-8ba1-41cd-b070-1a35f1f42c7f)


- - -

## Deployment & Local Development

### Deployment

This project was deployed at [Heroku](https://heroku.com/)

The numbers on the screenshots represent the numbers on the steps of my deployment process.

To deploy this project after creating my account, I:

1. Went to my dashboard and clicked on the New App dropdown menu

2. Clicked Create new app from the options
  

![heroku_deployment_step_1-2](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/f5810840-3399-48aa-8944-384850e2f6d9)


3. Named my app in the App name box

4. Chose a region from the dropdown menu (and accidentally chose the United States for this one)

5. Clicked Create app


![heroku_deployment_step_2-5](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/be20a348-416c-446c-8876-2a33ccb883bb)

Once the app was made I went to my dashboard where I can see my apps.

6. Clicked on the relevant app

![heroku_deployment_step_6](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/e6648e64-446c-4832-929f-3f7477c236b6)


7-8. From here, I went to settings, then to the Config Vars. I added the key of DISABLE_COLLECTSTATIC and gave it a value of 1.

![deployment_step_7-8](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/5e1a7d4f-3a96-42b5-bda3-464fbf8cd907)


9. I then had to prepare my code for deployment. Back in VSCode I installed the following gunicorn version and added it to my requirements.txt file:

![deployment step 9](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/55bf05d5-8451-4d27-95ef-f97b50d5b65b)

10. After that, I created a Procfile in the root directory and added my blogpage file directory to the Gunicorn WSGI:

![deployment_step_10](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/05cd3c9a-f252-4d98-a6c5-9400a6338c4b)

11. In order to keep my files safe when deployed, in my settings I changed DEBUG to False to prevent excessive information being shown when errors occurred which could potentially give people unwanted access. I then updated my ALLOWED_HOSTS list to include my Heroku deployment links.
12. Back on Heroku I switched to the Deployment tab and connected Github as the Deployment method. I searched my repository name and connected it.

![deployment_step_12](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/aba54a9b-9436-4ad9-9e1c-6985be01cdce)

13. Scrolling down the page, I chose to manually deploy my project as needed, but it's possible to set up automatic deployments if preferred.
  
![heroku_deployment_step_13](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/fed29cb2-9af8-4d0d-a827-ef493390b716)

  

### Local Development


#### How to Fork


Should you wish to fork this repo, here is a guide on how to do that:


Firstly, go to https://github.com/emmy-codes/geekhaven-blog/


1. On the main repo page, click the Fork button near the top right corner
2. 
(add img)  

3. On the create a fork page, check the Owner of the repo is set to the GitHub org you wish to use, and change the name of the repo if you wish.

2a: Add a description if you want to

3. Check the box here if you want to make a copy of the main branch or multiple branches (main is selected by default)

4. Create the fork

* Screenshot from an old project as I cannot fork my Python project due to not having any organizations connected to my account, and presumably because this repo is already a fork of the CI template
* 
(add img of forking repo)
  

#### How to Clone
  

For cloning the repo you will need:

* The [repo](https://github.com/emmy-codes/geekhaven-blog) open
 

* Your IDE of choice

1. On the repo page, click on the green "Code" button

2. On the dropdown from the Code button, click on your chosen key (pictured here is SSH)

3. Click the copy button (shown as two squares on top of one another)

(add img of copying SSH from repo)  

4. Open your IDE of choice and open the Terminal, or in my case, open the Terminal on your computer (I run Linux on Windows so may be slightly different for Mac/Windows users)

5. Check that you're in the right folder (shown here by checking my current folder by using the input: ls

6. Change as needed to reach your desired folder.

7. Type (without quotation marks): "git clone" followed by your copied link from GitHub.
  
8. You can now access the repo in your IDE if cloned directly there, or by typing (without quotation marks) "code ." in your Terminal.

9. Enjoy!
  
(add image of cmd git clone)
  

- - -
  

## Testing

Please refer to the [TESTING.md](https://github.com/) file for all testing carried out.  

## Bug Fixes

As I am making a blog I am very mindful of trying to keep my project as far separated as I can from the walkthrough from CI, whilst still using it as an assist tool.

I am ensuring that I change any naming conventions, both to help me understand what the code does, and to force me to have a more in-depth understanding of the codebase rather than copying the same names as CI.

This comes with its own set of problems when I don't fully understand something, as was proved when I attempted to append my blog posts to the HTML page I had created. I thought I had labelled everything correctly but received an error when attempting to run my server:

![appending_posts_to_dom](https://github.com/emmy-codes/geekhaven-blog/assets/70635859/8b4abf41-64ef-4a03-95bd-1a4bb8bb2d0e)

It was telling me that blogpost_list.html didn't exist, which was entirely true. It was looking in geekhaven_blog/blogpost_list.html because ListView was looking for a file of the same name, aka my BlogPost class. After some research I discovered it also expected geekhaven_blog to be a folder inside of my templates, which I was missing.

After making the above changes my server was once again loading!

- - -

## Credits
  
1234

### Code Used

### Content

I have used [OpenAI](https://chat.openai.com/) to create most of the blog text content for me so I can focus my time on practising with the code.
  

### Acknowledgments

I would like to acknowledge the following people:
  

* My partner who, despite having no idea about Python, has done his best to support me in my learning 🥰

* Family and friends on Facebook for user testing my game and providing feedback!

