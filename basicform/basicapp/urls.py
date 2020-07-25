
from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns=[
    path('otherone/', views.otherone, name='otherone'),
    path('othertwo/', views.othertwo,name='othertwo')
]
