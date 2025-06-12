from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .forms import ReviewForm

def book_list_view(request):
  if request.method == 'GET':
    book_list = models.Book.objects.all().order_by('-id')
    context = {
      'book_list': book_list
    }
    return render(request, template_name='books.html', context=context  )
  


def book_detail_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    reviews = book_id.reviews.all()
    average_rating = book_id.average_rating()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book_id
            review.author = request.user
            review.save()
    else:
        form = ReviewForm()

    context = {
        'book_id': book_id,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    }
    return render(request, 'books_detail.html', context)
    
def your_view_function(request, book_id):
    return HttpResponse(f"Вы запросили аудиозапись для книги с ID: {book_id}")


  
def book (request):
    if request.method == 'GET':
        return HttpResponse ('Читатель проживает тысячу жизней до того, как умрет. Тот, кто никогда не читает, — только одну.  Джордж Мартин;')