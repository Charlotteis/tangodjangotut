from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm

def index(request):
    # Query the db for a list of all categories stored
    # Order the categories by number of likes in descending order
    # Retrieve the top five only, or all if less than five categories
    # Place the list in our context dictionary which will we pass to template
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}

    # Render response and send it back
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')

def category(request, category_name_slug):
    # Create a context dictionary which we can pass to the template
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If not, the .get() method raises a DoesNotExist exception
        # The .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all pages associated with the category
        # Filter returns >= 1 model instance
        pages = Page.objects.filter(category=category)

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

    # Render the response, return it to the client
    return render(request, 'rango/category.html', context_dict)

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
