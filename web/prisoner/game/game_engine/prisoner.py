import ast


def is_valid_python(code):
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True


class Prisoner(object):
    def __init__(self, name, strategy):
        self.name = name
        self._strategy_text = strategy
        assert is_valid_python(self._strategy_text), "Syntax error in strategy."

    def __repr__(self):
        return "Prisoner object. name: " + self.name + "\nstrategy: + " + self._strategy_text
