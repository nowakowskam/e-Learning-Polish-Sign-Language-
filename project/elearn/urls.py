from django.urls import path
from . import views


urlpatterns=[
path('create_lesson/', views.CreateLessonView.as_view(), name='create_lesson'),
# path('create_lesson/<pk>/', views.CreateLessonView.as_view(), name='create_lesson'),
path('create_test/', views.CreateTestView.as_view(), name='create_test'),
path('list_lesson/', views.ListLessonView.as_view(), name='list_lesson'),
path('show_lesson/<int:pk>/', views.ShowLessonView.as_view(), name='show_lesson'),
path('update_lesson/<int:pk>/',views.UpdateLessonView.as_view(), name='update_lesson'),
path('test_list', views.TestListView.as_view(), name='test_list'),
path('update_test/<int:pk>/', views.UpdateTestView.as_view(), name='update_test'),
path('show_test/<int:pk>/', views.ShowTestView.as_view(), name='show_test'),
path('solve_test/<int:pk>/', views.SolveTestView.as_view(), name='solve_test'),
path('test_list/<int:pk>/test_confirm_delete', views.DeleteTestView.as_view(), name='delete_test'),
path('list_lesson/<int:pk>/lesson_confirm_delete', views.LessonDeleteView.as_view(), name='delete_lesson')
]
