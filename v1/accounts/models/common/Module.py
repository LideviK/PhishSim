from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class Module(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
     
    title = models.CharField(max_length=300, null=False)
    description = models.CharField(max_length=600, null=True)
    weight = models.IntegerField(null=False)
    
    sector = models.ForeignKey("accounts.Sector", on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def get_title(self):
        return self.title
    
    def get_weight(self):
        return self.weight
    
    def get_description(self):
        return self.description

    