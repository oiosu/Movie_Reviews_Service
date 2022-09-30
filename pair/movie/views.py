from django.shortcuts import render
from .models import Review

# Create your views here.
def index(request):
    return render(request, "movie/index.html")


def new(request):
    return render(request, "movie/new.html")

def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)
    context = {
        "title": title,
        "content":content,
    }

    return render(request, "movie/index.html", context)