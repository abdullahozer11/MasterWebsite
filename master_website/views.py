"""views.py. This file includes 404 views."""
from django.shortcuts import render


# pylint: disable=unused-argument
def page_not_found_view(request, exception):
    """
    Method to view 404 pages for each namespace.
    :param request:
    :return:
    """
    if request.path.startswith('/commerce/'):
        response = render(request, 'commerce_app/404.html', status=404)
    elif request.path.startswith('/todo/'):
        response = render(request, 'todo_app/404.html', status=404)
    else:
        response = render(request, 'portfolio/404.html', status=404)
    return response
