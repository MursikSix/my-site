from django.db import models
from django.utils import timezone


class Post(models.Model): #строка определяет нашу модель
    author = models.ForeignKey('auth.User')  #Ссылка на другую модель
    title = models.CharField(max_length=200) #ограничение символов
    text = models.TextField() #Неограниченный текст
    created_date = models.DateTimeField(
            default=timezone.now) # Дата и время
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # def создание функкии/ publish название метода
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # Вывод текста
        return self.title
    #C:\Users\Mursik\AppData\Local\Programs\Python\Python36-32\python.exe  manage.py  makemigrations  mysite (сохранение модели)
