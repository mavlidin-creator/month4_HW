from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from books.models import Book

class basketmodel(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Подтвержден'),
        ('not_confirmed', 'Не подтвержден'),
    )

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    card_number = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999999999999999)],  
        help_text="Введите номер карты (до 16 цифр)"
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_confirmed')

    def __str__(self):
        return f"{self.full_name} - {self.book.title}"
