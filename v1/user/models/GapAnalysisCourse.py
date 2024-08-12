from django.db import models
import uuid


# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

# a Gap Analysis Course


class GapAnalysisCourse(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    gap_analysis = models.ForeignKey("user.GapAnalysis", on_delete=models.CASCADE)
    course = models.ForeignKey("accounts.Course", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    result = models.IntegerField(null=True)

    diff = models.IntegerField(default=0, null=False)  # (Mean - Xi)^2  if gap
    
    completed_date = models.DateField(auto_now_add=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_course(self):
        return self.course