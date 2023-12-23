from django.db import models

class Table(models.Model):
    title = models.CharField('Назва статистики', max_length = 30)
    country = models.CharField('Країна', max_length = 30)
    year = models.CharField('Рік', max_length = 30)
    nums = models.CharField('Бюджет', max_length = 30)

    def __str__(self):
        return self.title
