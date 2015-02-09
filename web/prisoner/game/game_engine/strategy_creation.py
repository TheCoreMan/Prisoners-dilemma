class StrategyManager(object):

    CHOICES_LIST_ATTRIBUTE_FORMAT = "{}_choices"
    STRATEGY_FUNCTION_NAME_FORMAT = "strategy_{}"

    def __init__(self, first_prisoner_name, second_prisoner_name):
        self.first_turn = True
        setattr(self.__class__, self.CHOICES_LIST_ATTRIBUTE_FORMAT.format(first_prisoner_name), [])
        setattr(self.__class__, self.CHOICES_LIST_ATTRIBUTE_FORMAT.format(second_prisoner_name), [])

    def get_last_choice(self, who):
        choices = getattr(self.__class__, self.CHOICES_LIST_ATTRIBUTE_FORMAT.format(who))
        return choices[-1]

    def add_choice(self, choice, who):
        choices = getattr(self.__class__, self.CHOICES_LIST_ATTRIBUTE_FORMAT.format(who))
        choices.append(choice)

    def call_strategy(self, who):
        strategy = getattr(self.__class__, self.STRATEGY_FUNCTION_NAME_FORMAT.format(who))
        choice = strategy(self)
        self.add_choice(choice, who)
        return choice

    @staticmethod
    def get_function_code(strategy_function_body, strategy_function_name):
        strategy_function_code = """def {FUNCTION_NAME}(self):
{FUNCTION_CODE}""".format(FUNCTION_NAME=strategy_function_name, FUNCTION_CODE=strategy_function_body)
        strategy_function_code_lines = [line for line in strategy_function_code.splitlines(True)]

        def tabify(line):
            if not line.startswith("def"):
                line = "    " + line
            return line

        strategy_function_code = ''.join([tabify(line) for line in strategy_function_code_lines])
        return strategy_function_code

    def create_strategy_function(self, strategy_function_body, who):
        strategy_function_name = self.STRATEGY_FUNCTION_NAME_FORMAT.format(who)
        strategy_function_code = StrategyManager.get_function_code(strategy_function_body, strategy_function_name)
        add_dynamic_method_to_class(self.__class__, strategy_function_name, strategy_function_code)


def add_dynamic_method_to_class(target_class, function_name, function_code):
    exec_string = """
{CODE}
f = {NAME}""".format(CODE=function_code, NAME=function_name)
    exec(exec_string, globals())
    setattr(target_class, function_name, f)
