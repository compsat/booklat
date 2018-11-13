from django.db import models

# Audiobooks
class Audio(models.Model):
	name = models.CharField(max_length=255, null=True)
	author = models.CharField(max_length=255, default="Anonymous")	
	series = models.CharField(max_length=255, null=True)
	genre = models.CharField(max_length=255, null=True)
	narrated_by = models.CharField(max_length=255, null=True)
	length = models.CharField(max_length=255, null=True)
	release_date = models.CharField(max_length=255, null=True)
	description = models.TextField()
	embedded = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.name

# Websites where audiobooks are hosted for download 
class Host(models.Model):
    link = models.URLField(max_length=200)

    audio = models.ForeignKey(
        'Audio',
        on_delete = models.CASCADE,
    )
