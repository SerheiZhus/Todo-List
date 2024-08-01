from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm
from task.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3

    def get_queryset(self) -> Task:
        return Task.objects.order_by("boolean_field", "-created_task")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_confirm_delete.html"


def toggle_assign_to_task(request, pk) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.boolean_field = not task.boolean_field
    task.save()
    return HttpResponseRedirect(reverse_lazy("task:task-list"))


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 3


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")
    template_name = "task/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")
    template_name = "task/tag_confirm_delete.html"
