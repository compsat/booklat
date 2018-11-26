from django.http import HttpResponse
from django.shortcuts import render

from .models import Audio, Host, Contact, Social, Donate_Option, Partner


def index(request):
	featured_audio = Audio.objects.all()[:3]
	context = {"featured_audio" : featured_audio}
	return render(request, 'audio/index.html', context)

def seeall(request):
	all_audio = Audio.objects.all()
	context = {"all_audio" : all_audio}
	return render(request, 'audio/seeall.html', context)

# Shows all audio
def all_audio(request):
	return render(request, 'audio/all_audio.html')
