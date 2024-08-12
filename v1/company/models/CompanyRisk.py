from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class CompanyRisk(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    risk_level = models.FloatField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_risk(self):
        return self.risk_level