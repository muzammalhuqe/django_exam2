from django.db import models
from category.models import AddCategory
# Create your models here.

class AddTask(models.Model):
    task_title = models.CharField(max_length = 100)
    Task_assign_date = models.DateField(auto_now_add = True)
    task_description = models.TextField()
    is_completed = models.BooleanField(default = False)
    category = models.ManyToManyField(AddCategory, blank=True, null=True)

    def __str__(self):
        return self.task_title
