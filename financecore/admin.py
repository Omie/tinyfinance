from django.contrib import admin
from financecore.models import Institution, InstitutionType
from financecore.models import Investment, InvestmentType

admin.site.register(Institution)
admin.site.register(InstitutionType)

admin.site.register(Investment)
admin.site.register(InvestmentType)


