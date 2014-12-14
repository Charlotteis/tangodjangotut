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
