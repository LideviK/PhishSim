import uuid
from django.db import models

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class vuckeel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, null=True)
    
    is_user = models.BooleanField(null=False, default=False) # assumes it's always a company at first.
  
    key = models.CharField(max_length=400, null=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_key(self):
        return self.key
    
    def get_user(self):
        return self.user
    
    def get_company(self):
        return self.company