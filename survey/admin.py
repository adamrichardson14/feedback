from django.contrib import admin
from survey.models import Survey

class SurveyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Survey, SurveyAdmin)