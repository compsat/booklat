from django.db import models

# Audiobooks
class Audio(models.Model):
	name = models.CharField(max_length=255, null=True)
	author = models.CharField(max_length=255, default="Anonymous", blank=True, null=True)	
	series = models.CharField(max_length=255, blank=True, null=True)
	genre = models.CharField(max_length=255, blank=True, null=True)
	narrated_by = models.CharField(max_length=255, default="Anonymous", blank=True, null=True)
	length = models.CharField(max_length=255, blank=True, null=True)
	release_date = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField()
	embedded = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

# Websites where audiobooks are hosted for download 
class Host(models.Model):
	link = models.URLField(max_length=255)
	audio = models.ForeignKey(
		'Audio',
		on_delete = models.CASCADE,
	)

class Contact(models.Model):
	service_name = models.CharField(max_length=255, null=True)
	account = models.CharField(max_length=255, null=True)
	audio = models.ForeignKey(
		'Audio',
		on_delete = models.CASCADE,
	)
	def __str__(self):
		return self.name

class Social(models.Model):
	social_media = models.CharField(max_length=255, null=True)
	account_link = models.URLField(max_length=255, null=True)
	audio = models.ForeignKey(
		'Audio',
		on_delete = models.CASCADE,
	)
	def __str__(self):
		return self.name

class Donate_Option(models.Model):
	option_name = models.CharField(max_length=255, null=True)
	account_details = models.CharField(max_length=255, null=True)
	option_logo = models.ImageField(null=True)
	audio = models.ForeignKey(
		'Audio',
		on_delete = models.CASCADE,
	)
	def __str__(self):
		return self.name


class Partner(models.Model):
	partner_name = models.CharField(max_length=255, default="Anonymous")
	partner_link = models.URLField(max_length=255, null=True)
	partner_logo = models.ImageField(null=True)
	audio = models.ForeignKey(
		'Audio',
		on_delete = models.CASCADE,
	)
	def __str__(self):
		return self.name