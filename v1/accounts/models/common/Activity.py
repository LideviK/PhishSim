from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------



class Activity(models.Model):

    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"

    STATUS = ( 
        (STATUS_ACTIVE, STATUS_ACTIVE), 
        (STATUS_INACTIVE, STATUS_INACTIVE)
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, null=True)
    
    deactivated = models.BooleanField(null=False, default=True)  # if a subscribtion/free trial expires

    status = models.CharField(max_length=50, null=False, default=STATUS_INACTIVE, choices=STATUS)  # if a user has activated his account for the first time
    
    introduction = models.BooleanField(null=False, default=True)
    is_first_time = models.BooleanField(null=False, default=True)

    is_user = models.BooleanField(null=False, default=False) # assumes it's always a company at first.
    
    activated_token = models.CharField(max_length=600, null=True)
    activated_date = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_token(self):
        return self.activated_token
    
    def get_activated_date(self):
        return self.activated_date
    
    def get_deactivated(self):
        return self.deactivated
