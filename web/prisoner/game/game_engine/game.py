from .prisoner_DAL import get_prisoner
from .strategy_creation import StrategyManager


class PossibleChoices(object):
    KEEP_QUIET = 0
    RAT_OUT = 1


def get_years_from_choices(first_choice, second_choice):
    if first_choice == PossibleChoices.KEEP_QUIET:
        if second_choice == PossibleChoices.KEEP_QUIET:
            return 1, 1
        else:
            return 3, 0
    else:
        if second_choice == PossibleChoices.KEEP_QUIET:
            return 0, 3
        else:
            return 2, 2


def play_single_turn(first_prisoner, second_prisoner, strategy_manager):
    first_choice = strategy_manager.call_strategy(first_prisoner.name)
    second_choice = strategy_manager.call_strategy(second_prisoner.name)
    years_to_add_to_first, years_to_add_to_second = get_years_from_choices(first_choice, second_choice)
    first_prisoner.years += years_to_add_to_first
    second_prisoner.years += years_to_add_to_second


def play():
    first_prisoner_object = get_prisoner(0)
    second_prisoner_object = get_prisoner(1)

    s = StrategyManager(first_prisoner_object.name, second_prisoner_object.name)
    s.create_strategy_function(first_prisoner_object.strategy, first_prisoner_object.name)
    s.create_strategy_function(second_prisoner_object.strategy, second_prisoner_object.name)

    play_single_turn(first_prisoner_object, second_prisoner_object, s)
    s.first_turn = False

    for i in range(0, 10):
        play_single_turn(first_prisoner_object, second_prisoner_object, s)

    results_text = """
    Strategy #1: {S1}
    Strategy #2: {S2}
    Years #1: {Y1}
    Years #2: {Y2}
    """.format(S1=first_prisoner_object.strategy, S2=second_prisoner_object.strategy,
               Y1=first_prisoner_object.years, Y2=second_prisoner_object.years)

    return results_text
