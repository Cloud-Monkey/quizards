![Logo/header img](/documentation/readme-images/quizards-text-logo.webp) ![Quizard img](/documentation/readme-images/quizzard-img.webp)

# Project overview 

## live site https://dashboard.heroku.com/apps/quizards/deploy/github

Quizards is a digital platform for Trivia enthusiasts. Built with Django, it allows registered users to tackle 5 quiz questions daily. With a user-friendly interface and engaging content, it aims to make learning convenient and interactive. 

This daily quiz format aims to set the app apart by fostering consistent engagement while enhancing general knowledge retention.

### How To Play

Sign up/sign in as a user, quizzes will then be available for completion. Quizzes will be presented in multiple choice formats of 5 questions, feedback on scores will be presented on completion.

# List of features

#### Feature 1

![navbar img](/documentation/readme-images/navbar-img-1.png)

Navbar present on all pages, links to all pages, link to home on hat icon, displayed login status and login/logout button alters dynamically.

#### Feature 2

![home img](/documentation/readme-images/homepage-img.png)

Welcome area on homepage with call to action, quiz button redirects to quiz page for logged in users.

#### Feature 3

![quiz page img](/documentation/readme-images/quizpage-img.png)

Quiz page with questions and submit to view score modal with messages.

#### Feature 4

![scores img](/documentation/readme-images/scores-img.png)

Scores page with leaderboard, displays user, scores and percentages based on quiz results.

#### Feature 5

![login/signup img](/documentation/readme-images/login-page-img.png) ![login/signup img](/documentation/readme-images/signup-page-img.png)

Login page/Sign up page, users can login or signup and will beredirected to the homepage after buttons are clicked.

# UX/UI

### Audience Properties:
- Key Demographics: Ages 18-35, students, young professionals.  
- Key Psychographics: Enjoys learning and self-improvement, digital-savvy.  
- Pain Points: Difficulty finding time for learning, desire for regular progress tracking.  
- Buying Process: Looks for reviews, tests free trials, appreciates straightforward subscriptions.  
- Brands & Tone: Inspired by brands like Duolingo, Khan Academy; appreciates an engaging yet informational tone.

### Job
The main job of this website is to encourage user registration and daily engagement. It should clearly present the app's benefits, showcase its daily quiz format, and motivate users to sign up and participate regularly.

### Messaging and tone

Brand Archetype: Sage (knowledge).  
Tone Characteristics:  
- Informative, Engaging: Make trivia fun and accessible.  
- Trustworthy, Conversational: Build confidence with straightforward dialogue.  
- Respectful, Caring: Show understanding of user goals and learning journeys.  
- Matter-of-fact, Upbeat: Communicate with enthusiasm.

Example Messaging:  
“Sharpen your mind, day by day.”  
“Daily quizzes, boundless knowledge.”  
“Engage, learn, excel.”

### Design direction
- Simple, intuitive design: Reflects ease of use.  
- Engaging graphics: Visualize the daily learning journey.  
- Clear navigation: Highlights daily quiz feature.  
- Bright color scheme: Inspires excitement and curiosity.

### Website Structure
- Home Section: Welcome message, quick overview, and CTA to register/login.  
- Daily Quiz Details: Explain daily  and benefits.  
- How It Works: Step-by-step guide to engaging with content.  
- User Testimonials: Reviews from enthusiastic learners.  
- Benefits: Clear bullet points on learning and engagement advantages.  
- Call to Action: Encouragement to sign up and start playing.  
- Footer: Contact details, community forums, and support links.

### Wireframes

![ui image 1](/documentation/readme-images/wireframes-img.png)

- Initial designs produced using https://app.scene.io/ 
- Design rolled back to a simple three page design during the iterative process.

### Colour scheme

Initial colour schemes were produced using http://colormind.io/ colour palette was chosen to be cohesive, while being bright and engaging.

![Colour scheme image](/documentation/readme-images/color-scheme-img.png)

Variables were used within the CSS file to call colours as they were needed:

- Royal Blue: #4A5DE8;
- Burnt Ocre: #FF9F1C;
- Off-white: #F5F5F5;
- Pastel yellow: #FFEA00;
- Charcol: #333333;

Initial colour schemes were produced using http://colormind.io/ colour palette was chosen to be cohesive, while being bright and engaging.

Adjustments from initial designs were made where there was any accessability issue relating to choices.

### Typography & Iconography

In developing our full-stack Django site, we chose to utilize Bootstrap's default fonts to keep the project scope manageable. By leveraging these pre-designed fonts, we were able to maintain a consistent and professional aesthetic without the added complexity of custom typography.

This decision not only streamlined the design process but also allowed us to focus on core functionalities and features, ensuring we could deliver a high-quality user experience efficiently. Using Bootstrap's default fonts provided a solid foundation for our site's visual identity while simplifying development and enhancing overall productivity.

### Database Schema

![ERD Diamgram](/documentation/readme-images/erd-img.png)

Database Schema Entity Relationship Diagram (ERD) for Quizards displaying relationships between feature components saved within the database

Lucidchart was used to create the ERD for Quizards. To satisfy the application needs, models were created for the project. These include:

- **User** (User is created on signup, linked to results)
- **Questions** (Questions model exits in database to store and return questions)
- **Results** (Linked to User)

# Testing

## Responsiveness
The website has been thoroughly tested for responsiveness across all pages and components. Manual testing was conducted for three primary screen sizes:
- Mobile
- Laptop
- Desktop

## Functionality Testing
All website pages underwent manual testing to ensure every feature functions as intended. 

### Bug Report
- **Issue**: Login page form was not posting.
- **Cause**: An additional  `</form>` closing tag was present before the contents of the form.
- **Resolution**: The extra tag has been removed, resolving the issue.

## HTML Validation
All HTML code was validated using the W3C Markup Validation Service.

### Findings
- An extra `</div>` closing tag was identified on the `registration-success.html` page.
- **Resolution**: The superfluous tag has been removed.

### Current Status
The current build operates without errors in both browser and mobile views.

## CSS Validation
All CSS code was validated using the W3C CSS Validation Service (Jigsaw).

### Results
No issues were detected during the CSS validation process.

## Lighthouse

![lighthouse scores performance](/documentation/readme-images/quizzards_lighthouse.png)

All pages run through Lighthouse to check scores. 

![lighthouse scores img1](/documentation/readme-images/lighthouse-2-img.png) ![lighthouse scores img2](/documentation/readme-images/lighthouse-3-img.png)

Acceptable scores in all categories. No major issues.

## Deployment

https://quiz-heads-c1d86a4688ff.herokuapp.com

###Connecting to GitHub

To begin this project from scratch, you must first create a new GitHub repository using the Code Institute's Template. This template provides the relevant tools to get you started. To use this template:

- Log in to GitHub or create a new account.
- Navigate to the above CI Full Template.
- Click 'Use this template' -> 'Create a new repository'.
- Choose a new repository name and click 'Create repository from template'.
- In your new repository space, click the gitpod open button to generate a new workspace.
- Django Project SetUp
- Install Django and supporting libraries:
- pip3 install 'django<4' gunicorn
- pip3 install dj_database_url psycopg2
- 
Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a requirements.txt file and add all installed libraries to it with the pip3 freeze --local > requirements.txt command in the terminal.

Create a new Django project in the terminal django-admin startproject <project name>.
Create a new app eg. python3 mangage.py startapp home

Add this to list of INSTALLED_APPS in settings.py - 'home',

Create a superuser for the project to allow Admin access and enter credentials: python3 manage.py createsuperuser

## Migrate the changes with commands: python3 manage.py migrate

An env.py file must be created to store all protected data such as the DATABASE_URL and SECRET_KEY. These may be called upon in your project's settings.py file along with your Database configurations. The env.py file must be added to your gitignore file so that your important, protected information is not pushed to public viewing on GitHub. 

For adding to env.py:

import os
os.environ["DATABASE_URL"]="<copiedURLpostGres>"
os.environ["SECRET_KEY"]="my_super^secret@key"
For adding to settings.py:

import os
import dj_database_url
if os.path.exists("env.py"):
import env
SECRET_KEY = os.environ.get('SECRET_KEY') (actual extracted to variable within env.py)

Replace DATABASES with:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }

Set up the templates directory in settings.py:

Under BASE_DIR enter TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)
Update TEMPLATES = 'DIRS': [TEMPLATES_DIR] with:
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')

Create the media, static and templates directories in the top level of the project file in the IDE workspace.

A Procfile must be created within the project repo for Heroku deployment with the following placed within it: web: gunicorn ecommerce.wsgi

Make the necessary migrations again.
Postgres SQL
A new database instance was created on Postgres SQL for the project.

From your user dashboard, retrieve the important 'postgres://....' value. Place the value within your DATABASE_URL in your env.py file and follow the below instructions to place it in your Heroku Config Vars.

## Heroku Deployment

To start the deployment process , please follow the below steps:

Log in to Heroku or create an account if you are a new user.

Once logged in, in the Heroku Dashboard, navigate to the 'New' button in the top, right corner, and select 'Create New App'.

Enter an app name and choose your region. Click 'Create App'.

In the Deploy tab, click on the 'Settings', reach the 'Config Vars' section and click on 'Reveal Config Vars'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your:

DATABASE_URL:postgres://...
DISABLE_COLLECTSTATIC of value '1' (N.B Remove this Config Var before deployment),
SECRET_KEY and value
CLOUDINARY_API_KEY and value
CLOUDINARY_API_SECRET and value
CLOUDINARY_CLOUD_NAME and value
Add the Heroku host name into ALLOWED_HOSTS in your projects settings.py file -> ['herokuappname', ‘localhost’, ‘8000 port url’].

Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that DEBUG=False, save your project, add the files, commit for initial deployment and push the data to GitHub.

Go to the 'Deploy' tab and choose GitHub as the Deployment method.

Search for the repository name, select the branch that you would like to build from, and connect it via the 'Connect' button.

Choose from 'Automatic' or 'Manual' deployment options, I chose the 'Manual' deployment method. Click 'Deploy Branch'.

Once the waiting period for the app to build has finished, click the 'View' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. DISABLE_COLLECTSTATIC may be removed from the Config Vars once you have saved and pushed an image within your project.

## Clone Project

A local clone of this repository can be made on GitHub. Please follow the below steps:

Navigate to GitHub and log in.
The repository can be found at this location. https://github.com/MGW-GH/Hackathon3

Above the repository file section, locate the 'Code' button.

Click on the code button choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the 'Copy' button.
Open your Git Bash Terminal.

Change the current working directory to the location you want the cloned directory to be made.
Type git clone and paste in the copied URL from step 4.

Press 'Enter' for the local clone to be created.

Using the pip3 install -r requirements.txt command, the dependencies and libraries needed for will be installed.

Set up your env.py file and from the above steps for ElephantSQL, gather the Elephant SQL url for addition to your code and add your SECRET_KEY and STRIPE/AWS keys if using these services.
Ensure that your env.py file is placed in your .gitignore file and follow the remaining steps in the above Django Project Setup section before pushing your code to GitHub.

## Fork Project
A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:

## Navigate to GitHub and log in.

Once logged in, navigate to this repository using this link https://github.com/MGW-GH/Hackathon3 Repository.

Above the repository file section and to the top, right of the page is the 'Fork' button, click on this to make a fork of this repository.

You should now have access to a forked copy of this repository in your Github account.
Follow the above Django Project Steps if you wish to work on the project.

## Citation of ALL sources(code, images, text, tutorials and UX/UI tools)

- Initial wireframes https://scene.io
- Colour scheme http://colormind.io/
- Question generation https://perplexity.ai
- Wizard icons created by Freepik - Flaticon https://www.flaticon.com/free-icons/wizard
- Quiz Wizard image https://pro-quiz-wizard.netlify.app/
- Quizards text logo https://www.textstudio.com/
- Stackoverflow https://stackoverflow.co/
  
## Future features

Future planned features added to backlog for next iteration include:

- Categories of questions
- Ability for users to add questions to the site once approved
- Ensure questions already answered wont be repeated for the same user
- Users can answer 5 daily questions and this cannot be repeated

## Collaberators

- [MGW-GH](https://github.com/MGW-GH)
- [chuckydillo](https://github.com/chuckydillo)