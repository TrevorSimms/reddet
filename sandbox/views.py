from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Sandbox

def index(request):
    posts = Sandbox.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def addpost(request):
    w = request.POST['name']
    x = request.POST['title']
    y = request.POST['body']
    post = Sandbox(name=w, title=x, body=y)
    post.save()
    return HttpResponseRedirect(reverse('index'))
