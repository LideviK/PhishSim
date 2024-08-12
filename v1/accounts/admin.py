from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User

# ---------------- MODELS ----------------
from v1.accounts.models.common import Activity, Answer, Campaign, CampaignCourse, CommonField, Course, Group, Module, \
    Offer, OfferedCourse, Persona, Question, ResetPassword, Sector, UserGroup, Vuckeel
from v1.accounts.models.Account import Account
# ----------------------------------------


class CustomAccount(UserAdmin):
    model = Account

    list_display_links = ('email', 'username',)
    fieldsets = UserAdmin.fieldsets[:-1] + (
        (
            None,
            {
                'fields': (
                    'last_login',
                    'is_user',
                ),
            },
        ),
    )


admin.site.register(Account, CustomAccount)
admin.site.register(Activity.Activity)
admin.site.register(Answer.Answer)
admin.site.register(Campaign.Campaign)
admin.site.register(CampaignCourse.CampaignCourse)
admin.site.register(CommonField.CommonField)
admin.site.register(Course.Course)
admin.site.register(Group.Group)
admin.site.register(Module.Module)
admin.site.register(Offer.Offer)
admin.site.register(OfferedCourse.OfferedCourse)
admin.site.register(Persona.Persona)
admin.site.register(Question.Question)
admin.site.register(ResetPassword.ResetPassword)
admin.site.register(Sector.Sector)
admin.site.register(UserGroup.UserGroup)
admin.site.register(Vuckeel.vuckeel)
