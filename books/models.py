from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите картинку')
    description = models.TextField(verbose_name='Дайте описание')
    audio_recording = models.URLField(max_length=200, blank=True, null=True, help_text='Ссылка на YouTube аудиокнигу')

    TYPE_BOOK = (
        ('Short stories', 'Short stories'),
        ('Horror', 'Horror'),
        ('Fantasy', 'Fantasy')
    )
    type_book = models.CharField(max_length=100, choices=TYPE_BOOK)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 2)
        return None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'

def average_rating(self):
    reviews = self.reviews.all()
    if reviews.exists():
        return round(sum(r.rating for r in reviews) / reviews.count(), 2)
    return None

class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Напишите отзыв')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.PositiveIntegerField(
        verbose_name='Оценка',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} - {self.author} - {self.rating}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class BookProfile(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    extra_info = models.TextField()

    def __str__(self):
        return f"Профиль книги: {self.book.title}"
