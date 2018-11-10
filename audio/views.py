from django.http import HttpResponse
from django.shortcuts import render

from .models import Audio, Host

def index(request):
    return render(request, 'audio/index.html')


# Shows all audio
def all_audio(request):
    return render(request, 'audio/all_audio.html')
