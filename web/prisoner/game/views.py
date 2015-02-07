from django.shortcuts import render
from .game_engine.prisoner import Prisoner


def save_first_prisoner(prisoner):
    print("*** first prisoner \n" + repr(prisoner))


def save_second_prisoner(prisoner):
    print("*** second prisoner \n" + repr(prisoner))


def process_first_prisoner(request):
    try:
        first_prisoner = Prisoner(name=request.POST['name'], strategy=request.POST['strategy'])
        save_first_prisoner(first_prisoner)

    except AssertionError as e:  # means bad strategy code
        context = {'name': request.POST['name'], 'strategy_text': request.POST['strategy']}
        return render(request, 'game/invalid_code.html', context)


def process_second_prisoner(request):
    try:
        second_prisoner = Prisoner(name=request.POST['name'], strategy=request.POST['strategy'])
        save_second_prisoner(second_prisoner)

    except AssertionError as e:  # means bad strategy code
        context = {'name': request.POST['name'], 'strategy_text': request.POST['strategy']}
        return render(request, 'game/invalid_code.html', context)


def index(request):
    context = {'title': "Welcome to the Prisoner's Dilemma..."}
    return render(request, 'game/index.html', context)


def first_prisoner(request):
    context = {'title': "Welcome to the Prisoner's Dilemma...", 'prisoner_number': "1", "dest_page": "second_prisoner"}
    return render(request, 'game/prisoner.html', context)


def second_prisoner(request):
    process_first_prisoner(request)

    context = {'title': "Welcome to the Prisoner's Dilemma...", 'prisoner_number': "2", "dest_page": "results"}
    return render(request, 'game/prisoner.html', context)


def results(request):
    process_second_prisoner(request)

    context = {'name': "the prisoner names", 'strategy_text': "the prisoner strats, played out."}
    return render(request, 'game/results.html', context)


def help_page(request):
    context = {}
    return render(request, 'game/help_page.html', context)
