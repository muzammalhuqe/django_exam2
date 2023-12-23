from django.shortcuts import render
# from category.models import AddCategory
from task.models import AddTask
def home(request):
    # data = AddCategory.objects.all()
    data = AddTask.objects.all()
    return render(request, 'home.html', {'data' : data})