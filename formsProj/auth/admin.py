# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import BloodPressureLogModel
# Register your models here.
class BloodPressureLogAdmin(admin.ModelAdmin):
    class Meta:
        model = BloodPressureLogModel

admin.site.register(BloodPressureLogModel, BloodPressureLogAdmin)