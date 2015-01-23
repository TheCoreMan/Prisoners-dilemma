from django.shortcuts import render


def index(request):
    context = {'text': "Welcome to the prisoner game."}
    return render(request, 'game/index.html', context)


def results(request):
    context = {'name': request.POST['name'], 'strategy_text': request.POST['strategy']}
    return render(request, 'game/results.html', context)