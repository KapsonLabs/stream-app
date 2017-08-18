from django.http import HttpResponse 
from django.template import loader  
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(templete.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h1>Album details for  " + str(album_id) +"</h1>")

