from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
from rango.forms import UserForm, UserProfileForm
from rango.bing_search import run_query

from datetime import datetime


def index(request):
    # Query the db for a list of all categories stored
    # Order the categories by number of likes in descending order
    # Retrieve the top five only, or all if less than five categories
    # Place the list in our context dictionary which will we pass to template
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}

    visits = request.session.get('visits')
    print visits
    if not visits:
        visits = 0
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    print last_visit
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 5:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    context_dict['visits'] = visits
    request.session['visits'] = visits

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())

    response = render(request, 'rango/index.html', context_dict)

    return response

def about(request):

    visits = request.session.get('visits')
    context_dict = {'visits': visits}

    return render(request, 'rango/about.html', context_dict)


def category(request, category_name_slug):
    # Create a context dictionary which we can pass to the template
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = run_query(query)

            context_dict['result_list'] = result_list
            context_dict['query'] = query

    try:
        # Can we find a category name slug with the given name?
        # If not, the .get() method raises a DoesNotExist exception
        # The .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all pages associated with the category
        # Filter returns >= 1 model instance
        pages = Page.objects.filter(category=category).order_by('-views')

        # Add results list to template context
        context_dict['pages'] = pages
        # Add category object from db to context dict
        # Use category obekect in template to verify the category exists
        context_dict['category'] = category

        # Add cat name slug to context_dict
        context_dict['category_name_slug'] = category_name_slug
    except Category.DoesNotExist:
        # If we do not find the specified category
        # Do nothing - template will display no category message
        pass

    if not context_dict['query']:
        context_dict['query'] = category.name

    # Render the response, return it to the client
    return render(request, 'rango/category.html', context_dict)

@login_required
def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details
        form = CategoryForm()

    # Bad form or form details, or no form supplied...
    # Render the form eith error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):

    context = RequestContext(request)
    # category_name = category_name_slug.replace('_', ' ')

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated.
            page = form.save(commit = False)

            # Retrieve the associated Category object so we can add it.
            cat = Category.objects.get(slug=category_name_slug)
            page.category = cat

            # Also, create a default value for the number of views.
            page.views = 0

            # With this, we can then save our new model instance.
            page.save()

            # Now that the page is saved, display the category instead.
            return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    return render_to_response('rango/add_page.html', {'category_name_slug': category_name_slug,
                                                      'form': form}, context)

# def register(request):
#     # A boolean value to tell template if registration was successful
#     # Set to false initially, code will change value to True if reg success
#     registered = False
#
#     # If HTTP.Post, we can process form data
#     if request.method == 'POST':
#         # Grab info from raw form
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#
#         # If both forms valid:
#         if user_form.is_valid() and profile_form.is_valid():
#             # Save users form to Database
#             user = user_form.save()
#
#             # Hash the password with set_password method
#             user.set_password(user.password)
#             user.save()
#
#             # We need to set the user attribute ourselves, set commit=False
#             # This delays saving the model until we're ready
#             profile = profile_form.save(commit=False)
#             profile.user = user
#
#             # Did the user provide an avatar?
#             # If so, we need to get it from form and put it into UserProfile model
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']
#
#             # Save UserProfile instance
#             profile.save()
#
#             # Tell for that registration was successful
#             registered = True
#
#         # If invalid form/forms
#         # Print issues to terminal and show to user
#         else:
#             print user_form.errors, profile_form.errors
#
#     # Not a HTTP POST? Render form using two ModelForm instances
#     # Blank forms ready for input
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#
#     # Render template depending on context
#     return render(request, 'rango/register.html',
#     {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
#
#
# def user_login(request):
#
#     # If request is HTTP POST, try to get form ingo
#     if request.method == 'POST':
#         # Gather username and password
#         # This information is obtained from the login form
#         username = request.POST['username']
#         password = request.POST['password']
#
#         # See if password/username combination is valid, return user object if so
#         user = authenticate(username=username, password=password)
#
#         # If we have a User object, the details are correct
#         # If none, no user with matching credentials found
#         if user:
#             # Is account active?
#             if user.is_active:
#                 # Log user in, send back to homepage
#                 login(request, user)
#                 return HttpResponseRedirect('/rango/')
#             else:
#                 # Inactive account, no log ing!
#                 return HttpResponse("Your Rango account is disabled.")
#         else:
#             # Bad login details provided
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")
#
#     # Request not a HTTP POST? Display the login form
#     else:
#         # No context vriables to pass to template system
#         return render(request, 'rango/login.html', {})


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})


# @login_required
# def user_logout(request):
#     # Log the user out
#     logout(request)
#
#     # Redirect user to homepage
#     return HttpResponseRedirect('/rango/')

def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})



def track_url(request):
    page_id = None
    url = '/rango/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass

    return redirect(url)
