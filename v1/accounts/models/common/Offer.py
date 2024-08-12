from django.db import models
import uuid


# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class Offer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    title = models.CharField(max_length=600, null=True)

    offered_by = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    group = models.ForeignKey("accounts.Group", on_delete=models.CASCADE, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_title(self):
        return self.title

    def get_company(self):
        return self.offered_by
