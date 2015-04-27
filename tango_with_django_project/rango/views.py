from django.shortcuts import render

def index(request):
    model = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', model)