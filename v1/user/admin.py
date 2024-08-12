from django.contrib import admin

# --------------- MODELS ---------------
from v1.user.models import GapAnalysis, GapAnalysisCourse, ModuleCourse, User, UserAnswer, UserRisk
# --------------------------------------


admin.site.register(GapAnalysis.GapAnalysis)
admin.site.register(GapAnalysisCourse.GapAnalysisCourse)
admin.site.register(ModuleCourse.ModuleCourse)
admin.site.register(User.User)
admin.site.register(UserAnswer.UserAnswer)
admin.site.register(UserRisk.UserRisk)

