from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class Logo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    owner = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    
    set_date = models.DateTimeField(auto_now_add=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_owner(self):
        return self.owner
    
    def get_updated(self):
        return self.updated
    
    def get_created(self):
        return self.created
    
    def get_set_date(self):
        return self.set_date

