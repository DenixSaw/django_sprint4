from django.shortcuts import render  # type: ignore[import-untyped]
from django.http import HttpResponse  # type: ignore[import-untyped]


def about(request) -> HttpResponse:
    """Описание проекта."""
    template: str = 'pages/about.html'
    return render(request, template)


def rules(request) -> HttpResponse:
    """Правила проекта."""
    template: str = 'pages/rules.html'
    return render(request, template)

def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def internal_server_error(request):
    return render(request, 'pages/500.html', status=500)