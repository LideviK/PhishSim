from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class InvitedUser(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    
    invited_date = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_invitees(self):
        return self.user