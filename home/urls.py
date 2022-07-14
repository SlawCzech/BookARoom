from django.urls import path
from . import views



app_name = 'home'

urlpatterns = [
    path('room/new/', views.AddRoom.as_view(), name='add_view'),
    path('home/', views.AllRooms.as_view(), name='all_rooms'),
    path('home/room/del/<int:room_id>/', views.DeleteRoom.as_view(), name='del_room'),
    path('home/room/edit/<int:room_id>/', views.ModifyRoom.as_view(), name='edit_room'),
    path('home/room/mk_res/<int:room_id>/', views.BookRoom.as_view(), name='book_room'),
]