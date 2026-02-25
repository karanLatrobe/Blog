from django.contrib import admin
from .models import Experience,Project,Skills


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('designation','company','work_duration')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','company','techstack','duration')







class SkillsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = Skills.objects.all().count()
        if count == 0:
            return True 
        return False
    

# Register your models here.
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Skills,SkillsAdmin)