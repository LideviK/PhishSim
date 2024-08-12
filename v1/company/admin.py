from django.contrib import admin

# ------------- models -------------
from v1.company.models import Company, CompanyRisk, InvitedUser, Logo
# ----------------------------------



admin.site.register(Company.Company)
admin.site.register(CompanyRisk.CompanyRisk)
admin.site.register(InvitedUser.InvitedUser)
admin.site.register(Logo.Logo)

