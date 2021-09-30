from django.db import models
from users.models import CustomUser
# Create your models here.

class Domain(models.Model):
    text=models.CharField(max_length=50)

    def __str__(self):
        return self.text
        
class Question(models.Model):
    text=models.CharField(max_length=100)
    domain=models.ForeignKey(Domain,on_delete=models.CASCADE)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Reply(models.Model):
    text=models.CharField(max_length=200)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.question[:10]+" "+self.text[:10]
