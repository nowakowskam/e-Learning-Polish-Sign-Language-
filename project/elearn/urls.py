from django.urls import path
from . import views

urlpatterns=[
path('create_lesson/', views.CreateLessonView.as_view(), name='create_lesson'),
path('create_lesson/<int:pk>', views.CreateLessonView.as_view(), name='create_lesson'),
path('create_test/', views.CreateTestView.as_view(), name='create_test'),
path('list_lesson/', views.ListLessonView.as_view(), name='list_lesson'),
]