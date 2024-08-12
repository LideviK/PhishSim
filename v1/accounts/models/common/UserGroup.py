from django.db import models
import uuid


# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class UserGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    group = models.ForeignKey("accounts.Group", on_delete=models.CASCADE)
   
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)