from django.db import models
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class Question(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    course = models.ForeignKey("accounts.Course", on_delete=models.CASCADE)
    persona = models.ForeignKey("accounts.Persona", on_delete=models.CASCADE)
    answer = models.ForeignKey("accounts.Answer", on_delete=models.CASCADE)
    
    content = models.CharField(max_length=700, null=False)
    answeramount = models.IntegerField(null=False, default=1)  # Field name made lowercase.

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_answer(self):
        return self.answer

    def get_course(self):
        return self.course