from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import MovieForm
from .models import Movie


def index(request):
    movie = Movie.objects.all()
    context = {
        'movies_list': movie
    }
    return render(request, "index.html", context)


def details(request, m_id):
    movie = Movie.objects.get(id=m_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        imge = request.FILES['imge']
        movie = Movie(name=name, desc=desc, year=year, imge=imge)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})

def delete(request, id):
    if request.method == "POST":
        movie =Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
