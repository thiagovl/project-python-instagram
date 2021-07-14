from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False) # campo text de tamanho 140 caracters, blank - fazio, null em branco
    image = ImageField()

    def __str__(self):
        return self.text # retorna o nome do text para que seja mostrado na pagina /admin
