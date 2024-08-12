from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

class UserAnswer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    question = models.ForeignKey("accounts.Question", on_delete=models.CASCADE)

    answer_value = ArrayField( models.CharField(max_length=255, null=False) )
    result = models.IntegerField(default=0, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = 'id'

    def get_result(self):
        return self.result
    
    def get_question(self):
        return self.question

    def get_recent_answered_date(self):
        return self.updated
    
    def get_initial_answered_date(self):
        return self.created
