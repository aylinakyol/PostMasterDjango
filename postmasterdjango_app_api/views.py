from rest_framework import viewsets # type: ignore
from .models import Task
from .serializers import TaskSerializer

# Tüm CRUD (Create, Retrieve, Update, Delete, List) işlemlerini tek bir sınıf içinde otomatik olarak tanımlar.

# HTTP Method	    URL (varsayılan router)     Ne yapar?
# GET	            /api/tasks/                 Tüm task'ları listeler
# GET	            /api/tasks/<id>/            Belirli bir task'ı getirir
# POST	            /api/tasks/                 Yeni bir task oluşturur
# PATCH	            /api/tasks/<id>/            Belirli bir Task'ı tamamen günceller
# PUT	            /api/tasks/<id>/            Belirli bir Task'ı kısmi günceller
# DELETE	        /api/tasks/<id>/            Belirli bir Task'ı siler
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer