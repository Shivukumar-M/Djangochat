from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room

@login_required
def rooms(req):
    rooms = Room.objects.all()

    return render(req, 'rooms.html', {'rooms':rooms})

@login_required
def room(req, slug):
    room = Room.objects.get(slug=slug)

    return render(req, 'room.html', {'room':room})