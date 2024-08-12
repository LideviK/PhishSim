from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class Course(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=600, null=True)

    module = models.ForeignKey("accounts.Module", on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_course(self):
        return self.title
    
    def get_module(self):
        return self.module
    
    def get_description(self):
        return self.description
