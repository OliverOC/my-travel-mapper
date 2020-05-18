from django.shortcuts import render, redirect


def landing_page_view(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'landing_page/landing_page.html', context)