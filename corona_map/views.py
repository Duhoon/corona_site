from django.shortcuts import render

def index(request):
    return render(request, 'corona_map/index.html',{})