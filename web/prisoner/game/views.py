from django.shortcuts import render
from .models import Prisoner
from .game_engine.prisoner_DAL import save_prisoner, get_prisoner, delete_players_from_db
from .game_engine.game import play


def process_prisoner(request):
    prisoner = Prisoner(name=request.POST['name'], strategy=request.POST['strategy'])
    print(repr(prisoner))
    save_prisoner(prisoner)


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


def get_results_into_context():
    first_prisoner_object = get_prisoner(0)
    second_prisoner_object = get_prisoner(1)

    context = {}
    if first_prisoner_object.years != second_prisoner_object.years:
        context = {
            'winner':   first_prisoner_object if first_prisoner_object.years < second_prisoner_object.years else second_prisoner_object,
            'loser':    first_prisoner_object if first_prisoner_object.years > second_prisoner_object.years else second_prisoner_object}
    else:
        context = {
            'winner':   first_prisoner_object,
            'loser':    second_prisoner_object,
            'tie':      True}
    return context


def results(request):
    process_prisoner(request)

    try:
        play()
    except:
        delete_players_from_db()
        raise

    context = get_results_into_context()

    delete_players_from_db()

    return render(request, 'game/results.html', context)


def help_page(request):
    context = {}
    return render(request, 'game/help_page.html', context)
