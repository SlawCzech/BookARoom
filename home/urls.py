from django.urls import path
from . import views
# from views import AddRoom


app_name = 'home'

urlpatterns = [
    path('room/new/', views.AddRoom.as_view(), name='add_view'),

]