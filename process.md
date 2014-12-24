Process
============

## 09/12/2014
- Make the code directory
- Set up a virtual environment
- Initialise git repository
- Add django project
- Move SECRET_KEY to an environment variable within virtualenv activate.sh

## 10/12/2014
- Ran python manage.py migrate: creating the initial database tables for things like
the admin and authorisation sections

## 14/12/2014
- Started the 'rango' app
- Add 'rango' to the projects INSTALLED_APPS
- Added the index view and url in the rango app
- Told the overall project where to go if it is fed the 'rango' URL (to the rango
    app)
- Create 'about' view, map it to urls.py, link to about page from index view and
link to home from about view.
- END OF CHAPTER FOUR

- START CHAPTER FIVE (Templates and Static Media)
- Set up templates directory and absolute template path in settings.py
- Created index.html rango template
- Update the index view to 'render' the index.html template
- Set up 'static' folder and point to it in settings.py
- Loaded staticfiles into index.html, loaded angielans image.
- Setting up a simple development media server to upload images
- Create about.html template, render it in the 'about' view, use a staticimage
- END OF CHAPTER FIVE

- START CHAPTER SIX (Models and Databases)
- Make sure using the SqlLite Database
- Set up Category Model
- set up Page model with a ForeignKey (one to many) relationship with Category
- Make sure the database is initialised with 'python manage.py migrate'
- Created a superuse to work with admin interface/database
- Make migrations for changed models 'python manage.py makemigrations rango'
- Apply migrations 'python manage.py migrate'
- Accessed the /admin interface for the first time with our superuser creds
- Import and register the rango.models into the admin page to work with them
- Add a meta class to the Category model to define a correct verbose_name_plural
- Created and ran a database population script/model. 'populate_rango.py'
- Exercises: Add 'likes' and 'views' with default of 0 to Category model,
- Exercises: Migrate the new model changes
- Exercises: Update populate script to include views and likes
- Exercises: Customise the Admin Interface so that Page model shows category, page name and url
- END OF CHAPTER SIX

## 15/12/2014
- START CHAPTER SEVEN (Models, Templates and Views)
- Updated index view to use a queryset to display the top five categories (depending on likes)
- Amend index template to use the categories within the index view
- Implemented clean URLS using Django Slugify for pages within a category
- Experienced database conflicts with the new slug implemenatation,
hacked around it as per what I commented here: https://github.com/leifos/tango_with_django/issues/19
- Created a Category view, to show pages within each category
- Created a category template
- Change the index template to link to category slugs
- Exercise: Update populate script to add default view counts to pages
- Exercise: Display the top five viewed pages in the index template
- END CHAPTER SEVEN

- START CHAPTER EIGHT (Fun with Forms)
- Created a Category and Page form in forms.py
- Created an 'add category' view
- Created an 'add category' template
- Mapped the 'add category' view to the 'add category' template
- Add 'add category' link to index template
- Defined our own clean method within PageForm to prepend http:// to urls without http:// prepended
    - This was broken. I had to make sure the PageForm Url had an widget of TextInpit()
- The AddPage stuff was also broken. I can't explain how it was fixed, it involved 'rendertoresponse' and 'responsecontext'
that I found by trawling through the internet for hours
- END CHAPTER EIGHT

## 16/12/2014
- START CHAPTER NINE (User Authentication)
- Add Password Hashers to settings.py
- Added URLField and Image Upload field to User Model
- Add UserProfile to Django Admin
- Migrate the new UserModel attributes
- Created the User and UserProfile forms
- Created the user registration view
- Created the user registration template
- Created the user registration url
- Added registration link to index template
- Created the login view
- Created the login template
- Mapped login view to url
- Added login link to index, also display username if user logged in, in index template
- Created login url mapping
- Ensured not-logged-in folk are directed the login page when trying to access restricted pages
(Done via LOGIN_URL in settings.py)
- Created logout view
- Mapped logout view to logout url
- Restricted Add Page & Add Category to logged in users
- END CHAPTER NINE

- START CHAPTER TEN (Working with Templates)
- Created base.html for other templates to inherit from (includes the DOCTYPE and user links)
- Updated category.html to make use of template blocks and extends

## 17/12/2014

- Updated all templates to extend from base.html
- Updated all urls in templates to utilise the url template tag
- Updated restricted view to render the restricted.html template
- END CHAPTER TEN

- START CHAPTER ELEVEN (Cookies and Sessions)
- Build a visitor counter in index view

## 21/12/2014

- Cookies in the tutorial were broken, moved straight to sessions.
- Added sessions so info stored in backend not in cookies
- Added visitor counter to the about page
- END CHAPTER ELEVEN

- START CHAPTER TWELVE (User Auth with Django-Registration-Redux)
- pip install django-registration-redux
- One step registration process (no emails involved)
- Create registration templates: login, registration_form, registration_complete, logout
- Remove old 'register', 'login' and 'logout' templates, views and urls
- Amend RegistrationView model to direct users to index page on register (instead of registration_complete)
- Add password_change_form and password_change_done templates
- END CHAPTER TWELVE

- START CHAPTER THIRTEEN (Bootstrapping Rango)
- Updated base to use bootstrap
- Updated all templates to have a styled header
- Updated the index template
- Updated login template
- Updated add_category and add_page templates
- Updated registration_form template
- END CHAPTER THIRTEEN

- START CHAPTER FOURTEEN (Template Tags)
- Learning to create our own template tags
- Show all the categories a user can browse through in the sidebar
- Created rango/templatetags folder
- END CHAPTER FOURTEEN

- START CHAPTER FIFTEEN (Adding External Search Functionality)
- Created a bing-search model
- Created a search templae
- Created a search view
- Mapped search url
- Added search link to base template
- END CHAPTER FIFTEEN

- START CHAPTER SIXTEEN (Making Rango Tango! Exercises) & SEVENTEEN (Solutions)
- Track Page Click Through:
    - Created track_url() view and url.
    - Add goto link to categories in category template, rather than hard link
- Searching within a Category Page:
    - If user can't find the page they want within the category they should be able to search for it
    - Remove generic search from top nav
    - Add search template markup to category template
    - Update category view to handle a POST request. View must then include any search results on context_dict
    - Only authenticated users can search in a category
- END CHAPTERS SIXTEEN AND SEVENTEEN

## 23/12/2014

- START CHAPTER EIGHTEEN (jQuery and Django)
- Add jQuery to Project
- Messed around with jQ.
- END CHAPTER EIGHTEEN

- START CHAPTER NINETEEN (Ajax in Django with jQuery)
- Adding a like button, let users like a category, doesn't keep track though so expecting them not click like again...
    - Add like count to categories
    - Create a 'like category' view
    - Write an AJAX GET Request for like button
- Adding an inline category suggestion method
    - Add ajax request form sidebar form
    - Add get_category_list function and suggest_category view

## 24/12/2014

- Enable registered users to add a page to the suggested category by putting an "add" button next to each search results
- Can't get the fucking thing working.
- END CHAPTER NINETEEN

- START CHAPTER TWENTY (Automated Testing)
- Wrote some tests
- Tutorial fairly incomplete
- Would like to try Selinium
- 'pip install coverage' to see what percent of my code is covered by tests
- END CHAPTER TWENTY

- START CHAPTER TWENTY-ONE (Deploying your Project)
- Deployed rango to PythonAnywhere
- Changed debug mode, added bing API key
- END CHAPTER TWENTY-ONE





### Notes
- How can I redirect to the category just created once add_category is completed.
- How can I add the website and picture fields to the user registration form?
- How can I implement the creation and viewing of user profiles? (16.3)
- AUTO_ADD_PAGE is broken
