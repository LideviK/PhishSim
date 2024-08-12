from django.db import models
import uuid

# ----------------- Other models deps ---------------------
#----------------------------------------------------------

class Campaign(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    title = models.CharField(max_length=400, null=False)
    
    offered_by = models.ForeignKey("company.Company", on_delete=models.CASCADE)  # Field renamed because it started with '_'.
    group = models.ForeignKey("accounts.Group", on_delete=models.CASCADE, null=True)
    
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)  # Field name made lowercase.
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_title(self):
        return self.title
    
    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date
