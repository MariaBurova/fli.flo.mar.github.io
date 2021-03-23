from django.db import models


class Articles(models.Model):
    title=models.CharField('Название ', max_length=50)
    task=models.TextField('Содержание')
    full_text=models.TextField('Статья')
    date=models.DateTimeField('Дата')
    likes = models.IntegerField(default=0)


    def __str__(self):
        return f'Новость:{self.title}'
    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name='Новость'
        verbose_name_plural = 'Новости'
