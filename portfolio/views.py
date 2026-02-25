from django.shortcuts import render
from .models import Experience, Project, Skills
# Create your views here.




def portfolio(request):
    experience_detail = Experience.objects.all()
    project_detail = Project.objects.all()
    tech_stack_list = list(Project.objects.values_list('techstack',flat = True))
    tech_stack_list = tech_stack_list[0].split(',')

    ai_skill = Skills.objects.values_list('ai',flat=True)
    frontend_skill = Skills.objects.values_list('frontend',flat=True)
    backend_skill = Skills.objects.values_list('backend',flat=True)
    tools_skill = Skills.objects.values_list('tools',flat=True)
    deployment_skill = Skills.objects.values_list('deployment',flat=True)

    ai_skill = ai_skill[0].split(',')
    frontend_skill = frontend_skill[0].split(',')
    backend_skill = backend_skill[0].split(',')
    tools_skill = tools_skill[0].split(',')
    deployment_skill = deployment_skill[0].split(',')

    print(ai_skill)

    context = {'experience_detail':experience_detail,
            'projects':project_detail,
            'tech_stack_list':tech_stack_list, 
            'ai_skill' : ai_skill,
            'frontend_skill': frontend_skill,
            'backend_skill':backend_skill,
            'tools_skill':tools_skill,
            'deployment_skill':deployment_skill,

            }
    return render(request,'portfolio/karan.html',context )



