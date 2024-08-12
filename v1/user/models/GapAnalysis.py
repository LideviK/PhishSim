from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class GapAnalysis(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    benchmark = models.IntegerField()
    result = models.IntegerField(null=True)
    
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    completed_date = models.DateTimeField(auto_now_add=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_result(self):
        return self.result