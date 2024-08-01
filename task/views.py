from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3

    def get_queryset(self):
        return Task.objects.order_by("boolean_field", "-created_task")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_confirm_delete.html"


def toggle_assign_to_task(request, pk) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.boolean_field = not task.boolean_field
    task.save()
    return HttpResponseRedirect(reverse_lazy("task:task-list"))
