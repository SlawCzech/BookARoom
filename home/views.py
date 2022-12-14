from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from home.models import Room, Bookings
import datetime


class AddRoom(View):
    """
    Adding a room to database.
    Checks if the room already exists and controls for proper input data.
    """
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
    """
    Produces a view of all rooms.
    """
    def get(self, request):
        rooms = Room.objects.all().values()
        for room in rooms:
            booked = False
            reservations = Bookings.objects.filter(room_id_id=room['id'])
            reservation_dates = [res.booking_date for res in reservations]
            booked = datetime.date.today() in reservation_dates
        return render(request, 'home/all_rooms.html', {'rooms': rooms})

class DeleteRoom(View):
    """
    Deletes room from database.

    :param int room_id: id of the room
    """
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        room.delete()
        rooms = Room.objects.all().values()
        return render(request, 'home/all_rooms.html', {'rooms': rooms})

class ModifyRoom(View):
    """
    Allows for modifying rooms (name, capacity, projector).
    Controls for proper input data.

    :param int room_id: id of the room
    """
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

class BookRoom(View):
    """
    Allows for making reservations.
    Checks if the room is already booked and if the requested date is in the future.

    :param int room_id: id of the room
    """
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        reservations = Bookings.objects.filter(room_id_id=room_id).filter(
            booking_date__gte=str(datetime.date.today())).order_by('booking_date')
        return render(request, 'home/booking.html', {'room': room, 'reservations': reservations})

    def post(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        room = room.id
        date = request.POST.get("date")
        comment = request.POST.get("comment")

        reservations = Bookings.objects.filter(room_id_id=room_id).filter(
            booking_date__gte=str(datetime.date.today())).order_by('booking_date')

        if Bookings.objects.filter(room_id_id=room, booking_date=date):
            return HttpResponse("This room is already booked for this date.")
        if date < str(datetime.date.today()):
            return HttpResponse("Please indicate future date for your reservation")

        Bookings.objects.create(room_id_id=room, booking_date=date, commentary=comment)
        return redirect('home:all_rooms')

class RoomDetails(View):
    """
    Produces detailed view for a particular room (features and reservations).

    :param int room_id: id of the room
    """
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        reservations = Bookings.objects.filter(room_id_id=room_id).filter(booking_date__gte=str(datetime.date.today())).order_by('booking_date')
        return render(request, 'home/room_details.html', context={'room': room, 'reservations': reservations})

class Search(View):
    """
    Search engine for finding rooms with minimum expected capacity and projector availability.

    """
    def get(self, request):
        return render(request, 'home/search.html')

    def post(self, request):
        name = request.POST.get("name")
        room_capacity = int(request.POST.get("room_capacity"))
        if not room_capacity or room_capacity < 1:
            return HttpResponse('Please indicate real room capacity')
        is_projector = request.POST.get("is_projector")
        if is_projector == 'on':
            is_projector = True
        else:
            is_projector = False

        rooms = Room.objects.all().values()
        if is_projector:
            rooms = rooms.filter(is_projector=is_projector)
        if room_capacity:
            rooms = rooms.filter(room_capacity__gte=room_capacity)

        for room in rooms:
            reservations = Bookings.objects.filter(name=name).filter(
                booking_date__gte=str(datetime.date.today()))
            room.reserved = str(datetime.date.today()) in reservations

        return render(request, 'home/search.html', context={'rooms': rooms})

