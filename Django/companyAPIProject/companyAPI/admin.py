from django.contrib import admin

from companyAPI.models import Company
from .models import Company
# Register your models here.
admin.site.register(Company)