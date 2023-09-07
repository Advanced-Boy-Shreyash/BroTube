from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Video

# Create your views here.
def index(request):
    objs = Video.objects.all()
    context = {
        'videos': objs
    }
    return render(
            request,
            'index.html',
            context=context
        )

def player(request, id):
    obj = get_object_or_404(Video, id=id)
    context = {
        'video': obj
    }
    return render(
            request,
            'player.html',
            context=context
    )
