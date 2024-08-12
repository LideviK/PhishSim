from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class OfferedCourse(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    offer = models.ForeignKey("accounts.Offer", on_delete=models.CASCADE)
    
    course = models.ForeignKey("accounts.Course", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    
    is_completed = models.BooleanField(default=False)
    retaken = models.BooleanField(default=True)
    
    result = models.IntegerField(default=0, null=False)
    diff = models.IntegerField(default=0, null=False) 

    completed_date = models.DateField(null=True,auto_now=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_course(self):
        return self.course
    
    def get_result(self):
        return self.result