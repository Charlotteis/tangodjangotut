from django.shortcuts import render
from rango.models import Category, Page

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
    except Category.DoesNotExist:
        # If we do not find the specified category
        # Do nothing - template will display no category message
        pass

    # Render the response, return it to the client
    return render(request, 'rango/category.html', context_dict)
