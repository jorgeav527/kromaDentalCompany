from django.shortcuts import render

def frontpage(request):
    """The front page"""
    return render(request, 'core/frontpage.html')


def contact(request):
    """The contact page"""
    return render(request, 'core/contact.html')
