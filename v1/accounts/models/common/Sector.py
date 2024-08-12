from django.db import models
import uuid


# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class Sector(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    name = models.CharField(max_length=400)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name