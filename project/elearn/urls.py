from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path(
        "create_lesson/",
        login_required(views.CreateLessonView.as_view()),
        name="create_lesson",
    ),
    path(
        "create_test/",
        login_required(views.CreateTestView.as_view()),
        name="create_test",
    ),
    path("list_lesson/", views.ListLessonView.as_view(), name="list_lesson"),
    path(
        "solve_test_list/",
        login_required(views.SolveTestListView.as_view()),
        name="solve_test_list",
    ),
    path(
        "show_lesson/<int:pk>/",
        login_required(views.ShowLessonView.as_view()),
        name="show_lesson",
    ),
    path(
        "update_lesson/<int:pk>/",
        login_required(views.UpdateLessonView.as_view()),
        name="update_lesson",
    ),
    path("test_list", login_required(views.TestListView.as_view()), name="test_list"),
    path(
        "update_test/<int:pk>/",
        login_required(views.UpdateTestView.as_view()),
        name="update_test",
    ),
    path(
        "show_test/<int:pk>/",
        login_required(views.ShowTestView.as_view()),
        name="show_test",
    ),
    path(
        "solve_test/<int:pk>/",
        login_required(views.SolveTestView.as_view()),
        name="solve_test",
    ),
    path(
        "test_list/<int:pk>/test_confirm_delete",
        login_required(views.DeleteTestView.as_view()),
        name="delete_test",
    ),
    path(
        "list_lesson/<int:pk>/lesson_confirm_delete",
        login_required(views.LessonDeleteView.as_view()),
        name="delete_lesson",
    ),

]
