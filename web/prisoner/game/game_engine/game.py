from .prisoner_DAL import get_prisoner
from .strategy_creation import StrategyManager


class PossibleChoices(object):
    KEEP_QUIET = 0
    RAT_OUT = 1


def get_years_from_choices(first_choice, second_choice):
    if first_choice == PossibleChoices.KEEP_QUIET:
        if second_choice == PossibleChoices.KEEP_QUIET:
            return 1, 1  # Both keep quiet
        else:
            return 3, 0  # B rats out
    else:
        if second_choice == PossibleChoices.KEEP_QUIET:
            return 0, 3  # A rats out
        else:
            return 2, 2  # Both rat out


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

    first_prisoner_object.save()
    second_prisoner_object.save()
