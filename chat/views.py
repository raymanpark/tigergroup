from django.http import HttpResponse
from django.shortcuts import render
import webbrowser

def index(request):
    return render(request, 'chat/index.html', {})

def a(request):
    return render(request, 'chat/a.html', {})

def about(request):
    return render(request, 'chat/about.html', {})

def g(request):
    #url = "https://oauth.groupme.com/oauth/authorize?client_id=BLmGX0dIG8rQGtSUZS4kcOVkP9RoNb65x01H8fxPSK9ANNR7"
    #return webbrowser.open(url)
    return HttpResponse().write("<p>Here's the text of the Web page.</p>")

def redirect(request):
    return HttpResponse().write("redirect worked</p>")