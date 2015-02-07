from django.shortcuts import render
from .game_engine.prisoner import Prisoner
from .game_engine.game import Game


my_game = Game()


def process_prisoner(request):
    try:
        prisoner = Prisoner(name=request.POST['name'], strategy=request.POST['strategy'])
        my_game.save_prisoner(prisoner)

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
    process_prisoner(request)

    context = {'title': "Welcome to the Prisoner's Dilemma...", 'prisoner_number': "2", "dest_page": "results"}
    return render(request, 'game/prisoner.html', context)


def results(request):
    process_prisoner(request)

    first_prisoner_object = my_game.get_prisoner(0)

    context = {'name': first_prisoner_object.name,
               'strategy_text': "the prisoner strats, played out."}
    return render(request, 'game/results.html', context)


def help_page(request):
    context = {}
    return render(request, 'game/help_page.html', context)
