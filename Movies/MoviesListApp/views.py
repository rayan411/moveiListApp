from django.shortcuts import render
from MoviesListApp.models import Movies_Info


from django.shortcuts import render
from MoviesListApp.models import Movies_Info

def Movies_list(request):
    movies_list = Movies_Info.objects.all()
    context = {'movies_list': movies_list}
    return render(request, 'MoviesListApp/Movies_list.html', context)
