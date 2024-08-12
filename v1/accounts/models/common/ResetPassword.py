from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class ResetPassword(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, null=True)
    
    is_user = models.BooleanField(null=False)

    resetToken = models.CharField(max_length=700, null=True)
    tokenExp = models.DateField(null=True)
    
    reseted_Date = models.DateField(null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_token(self):
        return self.resetToken
    
    def get_user(self):
        return self.user
    
    def get_company(self):
        return self.company
    