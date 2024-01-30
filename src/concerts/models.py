from django.db import models


# Create your models here.
class Concert(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to="concerts/")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)


class Score(models.Model):
    name = models.CharField(max_length=100)
    concert = models.ForeignKey(
        Concert, on_delete=models.CASCADE, related_name="scores"
    )
    file = models.FileField(blank=True, upload_to="scores/")

    def __str__(self):
        return self.name
