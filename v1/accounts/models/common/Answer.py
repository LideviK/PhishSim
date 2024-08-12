from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------


class Answer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, unique=True)
    
    answer_value = ArrayField( models.CharField(max_length=255, null=False) )
    
    # question = models.ForeignKey("accounts.Question", on_delete=models.CASCADE)
    external_id = models.UUIDField(unique=True)  # the id from the chat{app,bot}

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def get_external_id(self):
        return self.external_id
    
    def get_answer_value(self):
        return self.answer_value
