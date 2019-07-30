from django.shortcuts import render
from .models import Forum

# Create your views here.
def forum(request):
    forums=Forum.objects.all()
    forum_name=list()
    return render(request, 'forum/forum.html', {'forums': forums})

