from django.db import models

# Audiobooks
class Audio(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name

# Websites were audiobooks are hosted for download 
class Host(models.Model):
    link = models.URLField(max_length=200)

    audio = models.ForeignKey(
        'Audio',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.link
