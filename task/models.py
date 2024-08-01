from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=250)
    created_task = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    boolean_field = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("created_task",)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
