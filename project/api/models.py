from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    introduction = models.CharField(max_length=13, default="+998991234567")
    price = models.SmallIntegerField(default=2010)
    image = models.ImageField(upload_to="images/students/", null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

