from django.urls import path
from myfinal_app import views

app_name = 'myfinal_app'

urlpatterns=[
path('other/',views.other,name='other'),
]
