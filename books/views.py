from django.shortcuts import render
from django.http import HttpResponse
def book (request):
    if request.method == 'GET':
        return HttpResponse ('Читатель проживает тысячу жизней до того, как умрет. Тот, кто никогда не читает, — только одну.  Джордж Мартин;')