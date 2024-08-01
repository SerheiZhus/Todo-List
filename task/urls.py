from django.urls import path
from task.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_assign_to_task,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "task/<int:pk>/toggle-assing/", toggle_assign_to_task, name="task-toggle-assign"
    ),
]


app_name = "task"
