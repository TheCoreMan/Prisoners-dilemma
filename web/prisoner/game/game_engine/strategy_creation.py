class StrategyCreation(object):
    def get_strategy_function(self, strategy_text, which):
        strategy_function_name = "strategy_{}".format(repr(which))
        strategy_function_code = """
def {FUNCTION_NAME}(self):
    {FUNCTION_CODE}
        """.format(FUNCTION_NAME=strategy_function_name, FUNCTION_CODE=strategy_text)
        add_dynamic_method_to_class(self.__class__, strategy_function_name, strategy_function_code)


def add_dynamic_method_to_class(target_class, function_name, function_code):
    exec_string = """
{CODE}
f = {NAME}""".format(CODE=function_code, NAME=function_name)
    exec(exec_string, globals())
    setattr(target_class, function_name, f)
