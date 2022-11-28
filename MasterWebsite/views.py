from django.shortcuts import render


def page_not_found_view(request, exception):
    if request.path.startswith('/commerce/'):
        return render(request, 'commerce_app/404.html', status=404)
    elif request.path.startswith('/todo/'):
        return render(request, 'todo_app/404.html', status=404)
    else:
        return render(request, 'portfolio/404.html', status=404)