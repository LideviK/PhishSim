from django.db import models
import uuid



class Group(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    name = models.CharField(max_length=255, null=True)
    group_type = models.CharField(max_length=255, null=False) 
   
    created_date = models.DateField(null=False) 

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_namee(self):
        return self.name
    
    def get_group_type(self):
        return self.group_type