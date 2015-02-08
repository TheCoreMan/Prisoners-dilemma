from .prisoner_DAL import get_prisoner
from .strategy_creation import StrategyCreation


def play():
    first_prisoner_object = get_prisoner(0)
    second_prisoner_object = get_prisoner(1)

    s = StrategyCreation()
    s.get_strategy_function(first_prisoner_object.strategy, 1)
    s.get_strategy_function(second_prisoner_object.strategy, 2)

    first_res = s.strategy_1()
    second_res = s.strategy_2()

    return "Strategy #1: " + first_prisoner_object.strategy + "\nStrategy #2: " + second_prisoner_object.strategy
