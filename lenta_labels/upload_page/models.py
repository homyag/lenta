from django.db import models


# модель для хранения файла на сервере
class UploadFile(models.Model):
    file = models.FileField(upload_to='documents/uploads/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)