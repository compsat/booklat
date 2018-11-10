from django.db import models

class Audio(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Host(models.Model):
    link = models.CharField(max_length=255)

    audio = models.ForeignKey(
        'Audio',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.link