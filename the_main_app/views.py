from django.shortcuts import render
from .models import Story, ImgModel


def home(request):
    # if request.method == 'GET':
    stories = Story.objects.all()
    return render(request, 'index.html', {'stories': stories})
    # elif request.method == 'POST':
        # Create image using ImgModel, then associate it to the story you want,
        #  or create a new story and then associate, I can't do it as I don't know how you separate stories from each other

        # {% for img in story.images.all %}
        # {% for img in story.images.all %}