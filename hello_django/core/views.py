from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse('<h1>hello {} de {} anos</h1>'.format(nome, idade))


def soma(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f'A soma é {num1} + {num2} = {result}')


def subtracao(request, num1, num2):
    result = num1 - num2
    return HttpResponse(f'A diferença é {num1} - {num2} = {result}')


def multiplicacao(request, num1, num2):
    result = num1 * num2
    return HttpResponse(f'A multiplicação é  {num1} x {num2} = {result}')


def divisao(request, num1, num2):
    result = num1 / num2
    return HttpResponse(f'A divisão é {num1} / {num2} = {result}')
