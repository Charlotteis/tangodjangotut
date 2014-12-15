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
- START CHAPTER SEVEN (Models, Templates and Views
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
