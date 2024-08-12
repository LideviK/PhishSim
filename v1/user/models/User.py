from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------



# ------------ ROLE CHOICES ----------------
ROLE_CHOICE = [
    ('ADMIN', 'ADMIN'),
    ('USER', 'USER')
]
# -----------------------------------------


# ------------ LEVEL CHOICES --------------
LEVEL_CHOICE = (
    ('BEGINNER', 'BEGINNER'),
    ('INTERMIDIATE', 'INTERMIDIATE'),
    ('ADVANCED', 'ADVANCED')
)
# -----------------------------------------


class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
  
    persona = models.ForeignKey("accounts.Persona", on_delete=models.CASCADE)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
  
    country = models.CharField(max_length=100, null=True)
  
    role = models.CharField(max_length=100, choices=ROLE_CHOICE)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name
    
    def get_created(self):
        return self.created
    
    def get_level(self):
        return self.level
    
    def get_country(self):
        return self.country
    
    def get_last_update(self):
        return updated


