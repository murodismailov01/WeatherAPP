from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):
    appid = '3b7b6389179c5f62e83633b1d0d6d206'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {"all_info": all_cities, 'form': form}

    return render(request, 'index.html', context)


def city_delete(request, slug):
    city = City.objects.get(slug=slug)
    if request.method == 'POST':
        city.delete()
        return redirect('article_func')
    return render(request, 'index_delete.html', {'city': city})