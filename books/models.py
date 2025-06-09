from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите картинку')
    description = models.TextField(verbose_name='Дайте описание')
    audio_recording = models.URLField(max_length=200,blank=True,null=True,help_text='Ссылка на YouTube аудиокнигу')
    TYPE_BOOK =(
        ('Short stories', 'Short stories'),
        ('Horror', 'Horror'),
        ('Fantasy', 'Fantasy')
    )
    type_book = models.CharField(max_length=100, choices=TYPE_BOOK)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_youtube_embed_url(self):
        if self.youtube_audio_url:
            import re
            match = re.search(r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})', self.youtube_audio_url)
            if match:
                video_id = match.group(1)
                return f"https://www.youtube.com/embed/{video_id}?rel=0&autoplay=0"
        return None
    
    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'
