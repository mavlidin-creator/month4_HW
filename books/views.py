from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def book_list_view(request):
  if request.method == 'GET':
    book_list = models.Book.objects.all().order_by('-id')
    context = {
      'book_list': book_list
    }
    return render(request, template_name='books.html', context=context  )
  

def book_detail_view(request, id):
   if request.method == 'GET':
      book_id = get_object_or_404(models.Book, id=id)
      context = {
         'book_id' : book_id
      }
      return render(request, template_name='books_detail.html', context=context  )
def your_view_function(request, book_id):
    return HttpResponse(f"Вы запросили аудиозапись для книги с ID: {book_id}")


  
def book (request):
    if request.method == 'GET':
        return HttpResponse ('Читатель проживает тысячу жизней до того, как умрет. Тот, кто никогда не читает, — только одну.  Джордж Мартин;')