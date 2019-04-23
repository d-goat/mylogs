from django.db import models

# Create your models here.
class Logs(models.Model):
    #id = 1,2,3....と見えないけれど存在する
    content = models.CharField(max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True)
