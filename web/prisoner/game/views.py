from django.shortcuts import render
import ast


def is_valid_python(code):
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True


def index(request):
    context = {'text': "Welcome to the prisoner game."}
    return render(request, 'game/index.html', context)


def results(request):
    code = request.POST['strategy']
    print("Is " + code + " valid?" + str(is_valid_python(code)))
    if is_valid_python(code):
        context = {'name': request.POST['name'], 'strategy_text': code}
        return render(request, 'game/results.html', context)
    else:
        context = {'name': request.POST['name'], 'strategy_text': code}
        return render(request, 'game/invalid_code.html', context)