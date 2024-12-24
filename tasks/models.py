from django.utils import timezone

from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import User
from django.db.models import Q

class BaseModel(models.Model):
    objects = Manager()
    class Meta:
        abstract = True

class Status(models.TextChoices):
    TODO = "To do"
    IN_PROGRESS = "In progress"
    DONE = "Done"
    CANCELLED = "Cancelled"

class Priority(models.TextChoices):
    LOW = "Low"
    NORMAL = "Normal"
    HIGH = "High"

class Task(BaseModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.TODO)
    priority = models.CharField(max_length=6, choices=Priority.choices, default=Priority.NORMAL)
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by_tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(due_date__gte=timezone.now()),
                name="due_date_not_in_past"
            )
        ]

    def save(self,*args, **kwargs):
        if self.status == Status.DONE and self.completed_at is None:
            self.completed_at = timezone.now()
        else:
            self.completed_at = None

        super().save(*args, **kwargs)
