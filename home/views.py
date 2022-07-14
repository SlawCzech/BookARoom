from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from home.models import Room


class AddRoom(View):
    def get(self, request):
        return render(request, 'home/add_room.html')

    def post(self, request):
        name = request.POST.get("name")
        if not name:
            return HttpResponse('Room name was empty')
        room_capacity = int(request.POST.get("room_capacity"))
        if not room_capacity or room_capacity < 1:
            return HttpResponse('Please indicate room capacity')
        is_projector = request.POST.get("is_projector")
        if is_projector == 'on':
            is_projector = True
        else:
            is_projector = False
        if Room.objects.filter(name=name):
            return HttpResponse('This room is already in database')

        Room.objects.create(name=name, capacity=room_capacity, is_projector=is_projector)
        return render(request, 'home/add_room.html')

class AllRooms(View):
    def get(self, request):
        rooms = Room.objects.all().values()
        return render(request, 'home/all_rooms.html', {'rooms': rooms})

class DeleteRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        room.delete()
        rooms = Room.objects.all().values()
        return render(request, 'home/all_rooms.html', {'rooms': rooms})

class ModifyRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        return render(request, 'home/edit.html', {'room': room})

    def post(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        name = request.POST.get("name")
        if not name:
            return HttpResponse('Room name was empty')
        room_capacity = int(request.POST.get("room_capacity"))
        if not room_capacity or room_capacity < 1:
            return HttpResponse('Please indicate room capacity')
        is_projector = request.POST.get("is_projector")
        if is_projector == 'on':
            is_projector = True
        else:
            is_projector = False

        room.name = name
        room.capacity = room_capacity
        room.is_projector = is_projector
        room.save()

        return redirect('home:all_rooms')