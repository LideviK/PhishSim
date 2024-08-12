from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class CommonField(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    module = models.ForeignKey("accounts.Module", on_delete=models.CASCADE, null=True)
    course = models.ForeignKey("accounts.Course", on_delete=models.CASCADE, null=True)
    
    is_course = models.BooleanField(null=False) 
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_course(self):
        return self.course

    def get_module(self):
        return self.module