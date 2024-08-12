from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model

import uuid

# ----------------- Other models deps ---------------------
# ---------------------------------------------------------

# ----------------------- Managers ------------------------
from v1.accounts.managers.UserManager import CustomUserManager, UserManager
# ---------------------------------------------------------


class Account(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, unique=True)

    email = models.EmailField(max_length=254, null=False, unique=True)
    is_user = models.BooleanField(default=False)

    company_user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, null=True)

    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=255, default='')
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "accounts"

    def get_email(self):
        return self.email
    

    def get_created(self):
        return self.created

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.username
        if not self.username:
            self.username = self.email
        super(Account, self).save(*args, **kwargs)

    


