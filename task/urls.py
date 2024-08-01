from django.urls import path
from task.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_assign_to_task,
    TagListView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "task/<int:pk>/toggle-assing/", toggle_assign_to_task, name="task-toggle-assign"
    ),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]


app_name = "task"
