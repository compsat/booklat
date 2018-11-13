from django.http import HttpResponse
from django.shortcuts import render

from .models import Audio, Host


def index(request):
	all_audio = Audio.objects.all()
	context = {"all_audio" : all_audio}
	return render(request, 'audio/index.html', context)


# Shows all audio
def all_audio(request):
	return render(request, 'audio/all_audio.html')
