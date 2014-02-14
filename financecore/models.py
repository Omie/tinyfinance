from django.db import models
#from django.contrib.auth.models import User
from financecore.constants import INTEREST_TYPE_CHOICES

class InstitutionType(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=64)
    type = models.ForeignKey(InstitutionType)

    def __unicode__(self):
        return '-'.join([self.name, self.type.name])

class InvestmentType(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Investment(models.Model):
    name = models.CharField(max_length=64)
    type = models.ForeignKey(InvestmentType)
    institution = models.ForeignKey(Institution)

    start_date = models.DateField()
    period = models.IntegerField() #months

    interest_rate = models.DecimalField(max_digits=32,decimal_places=2)
    interest_type = models.CharField(choices=INTEREST_TYPE_CHOICES,
                        max_length=4)

    def __unicode__(self):
        return " ".join([self.name, "-", self.type.name, "at", 
                    self.institution.name])

