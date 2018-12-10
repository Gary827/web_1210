from django.http import HttpResponse



def root(request):
    name = request.GET.get('name', 'guest')
    return HttpResponse('HI,{}'.format(name))

def hello(request, name):
    return HttpResponse('Hi,{}'.format(name))

def s(request, number):
    return HttpResponse(number ** 2)

def l(request, number1, number2):
    result = ['<li>{}</li>'.format(i) for i in range(number1, number2+1)]
    return HttpResponse('<ul>{}</ul>'.format(''.join(result)))