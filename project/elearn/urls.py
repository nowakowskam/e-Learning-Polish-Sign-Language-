from django.urls import path
from . import views


urlpatterns=[
path('create_lesson/', views.CreateLessonView.as_view(), name='create_lesson'),
path('create_lesson/<pk>/', views.CreateLessonView.as_view(), name='create_lesson'),
path('create_test/', views.CreateTestView.as_view(), name='create_test'),
path('list_lesson/', views.ListLessonView.as_view(), name='list_lesson'),
path('update_lesson/<pk>/', views.UpdateLessonView.as_view(), name='update_lesson'),
path('show_lesson/<int:pk>/', views.ShowLessonView.as_view(), name='show_lesson')
]
#TODO usuniete as view