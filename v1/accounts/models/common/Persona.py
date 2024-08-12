from django.db import models
import uuid


# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class Persona(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    name = models.CharField(max_length=400, null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name