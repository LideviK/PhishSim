from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class ModuleCourse(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    module = models.ForeignKey("accounts.Module", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    course = models.ForeignKey("accounts.Course", on_delete=models.CASCADE)
    
    is_completed = models.BooleanField(default=False, null=False)
    retaken = models.BooleanField(default=False, null=False)

    result = models.IntegerField(default=0, null=False)
    diff = models.IntegerField(default=0, null=False)  # (Mean - Xi)^2
    
    completed_date = models.DateField(auto_now_add=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_course(self):
        return self.course

    def get_user(self):
        return self.user
    
    def get_result(self):
        return self.result
    