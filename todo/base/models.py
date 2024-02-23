from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Task(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blan=True)
    title=models.CharField( max_length=50)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=True)
    create=models.DateTimeField(auto_add_now=True)

    class Meta:
      ordering=['complete']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
