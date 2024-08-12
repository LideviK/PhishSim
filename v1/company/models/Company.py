from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# from v1.accounts.models.common import Sector
# ---------------------------------------------------------


class Company(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    sector = models.ForeignKey("accounts.Sector", on_delete=models.CASCADE)
    country = models.CharField(max_length=100, null=True)
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def get_name(self):
        return self.name
        


