from django.shortcuts import render


def about(request):
    """О проекте."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """Наши правила."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
