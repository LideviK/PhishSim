from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class UserRisk(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    risk_level = models.FloatField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        
        order_with_respect_to = 'id'

    def get_risk(self):
        return self.risk_level
    
    def get_user(self):
        return self.user

