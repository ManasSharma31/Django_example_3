from basic_app import views
from django.urls import re_path,path

app_name='basic_app'

urlpatterns=[
path('',views.SchoolList.as_view(),name='manas'),
path('<int:pk>/',views.SchoolDetail.as_view(),name='detail'),
path('create/',views.SchoolCreatview.as_view(),name='create'),
path('update/<int:pk>/',views.SchoolUpdate.as_view(),name='update'),
path('delete/<int:pk>/',views.SchoolDelete.as_view(),name='delete'),
]
