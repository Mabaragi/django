from django.shortcuts import render

# Create your views here.

def calculation(request):
    return render(request, 'calculators/calculation.html')

def catch(request):

    flag = False
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    product = first * second
    minus = first - second

    if second != 0:
        divide = first / second
        flag = True


    if flag:
        context = {
            'first': first,
            'second': second,
            'product': product,
            'minus': minus,
            'divide': divide,
            'flag': flag,
        }
    else:
        context = {
            'first': first,
            'second': second,
            'product': product,
            'minus': minus,
            'flag': flag,
        }

    return render(request, 'calculators/catch.html', context)