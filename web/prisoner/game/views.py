from django.shortcuts import render


def index(request):
    context = {'text': "Welcome to the prisoner game."}
    return render(request, 'game/index.html', context)