from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class CampaignCourse(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    campaign = models.ForeignKey("accounts.Campaign", on_delete=models.CASCADE)
    course = models.ForeignKey("accounts.Course", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)  # needs tobe array Field renamed because it started with '_'.
    
    is_completed = models.BooleanField(default=False)
    retaken = models.BooleanField(default=False)  # if the course is taken beforehand
    
    result = models.IntegerField(default=0, null=False)
    diff = models.IntegerField(default=0, null=False)  # (Mean - Xi)^2
    
    completed_on = models.DateField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_course(self):
        return self.course
    
    def get_completed_date(self):
        return self.completed_on
    
    def get_user(self):
        return self.user
