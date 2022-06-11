from dataclasses import fields
import email
from inspect import Parameter
from pyexpat import model
from re import search
from tkinter import VERTICAL
from turtle import title
from django.contrib import admin, messages
from .models import User
from .models import Student
from .models import Coach
from .models import Project
from .models import MembershipInProjects

# Register your models here.


class ProjectInLine(admin.StackedInline): #admin.TabularInline
    model = Project 
    # fieldsets = [
    #     (
    #         None, 
    #         {
    #         'fields': ['project_name']
    #         }
    #     )
    # ]
class ProjectDurationFilter(admin.SimpleListFilter):
    title = 'durée'  #affichage
    parameter_name = 'project_duration'   #link to model
    def lookups(self, request, model_admin):
        return (
            ('1 month', ('less than a month')),
            ('3 months', ('less than 3 months')),
            ('4 months', ('more than 3 months'))
        )
        
    def queryset(self, request, queryset):
        if self.value() == '1 month':
                return queryset.filter(project_duration__lte =30) #queryset est equivalent a select * from project where pd <=30
        if self.value() == '3 months':
                return queryset.filter(project_duration__lte =90,project_duration__gte =30)
        if self.value() == '4 months':
                return queryset.filter(project_duration__gte =90)


def set_valid(modeladmin,request, queryset):
        rows = queryset.update(isValid = True)
        if rows == 1:
            message = '1 project was'
        else:
            message = f'{rows} projects were'
        messages.success(request, message= f'{message} marked as valid' ) 
set_valid.short_description = "Validate"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def set_invalid(modeladmin,request, queryset):
        rows_invalid = queryset.filter(isValid=False)
        if rows_invalid.count()>0:
            messages.error(request, message = f'{rows_invalid.count()} are already marked invalid ') 
        else:
            rows = queryset.update(isValid = False)
            if rows == 1:
                message = '1 project was'
            else:
                message = f'{rows} projects were'
            messages.success(request, message= f'{message} marked as invalid' ) 
    set_invalid.short_description = "Refuse"
    actions = [set_valid, 'set_invalid']
    actions_on_bottom = True
    actions_on_top = True

    # actions = [set_valid]
    list_display=(
        'project_name',
        'project_duration',
        'time_allocated',
        'creator',
        'supervisor',
        'isValid'
    )
    search_fields = ['project_name']
    # date_hierarchy= 'updated_at'
    # autocomplete_fields= ['supervisor']
    fieldsets = [
            (
                'Etat', 
                {
                'fields': ['isValid']
                }
            ),
            (
                'About',
                {   'classes':('collapse',),
                    'fields' :(('project_name','project_duration'),('time_allocated'),('creator','supervisor'))
                }
            ),
             (
                'more',
                {   'classes':('collapse',),
                    'fields' :['needs']
                }
            )
        ]
    empty_value_display = ' -empty-'
    radio_fields = {"supervisor": admin.HORIZONTAL}
    list_filter = (
        'creator',
        'isValid',
         ProjectDurationFilter
    )

class StudentAdmin(admin.ModelAdmin):
     list_display = (                
        'email',
        'name',
        'first_name',
    )
   
     fields = (
        ( 'name', 'first_name'),
        'email'
    )
     search_fields = ['first_name']
     inlines = [
         ProjectInLine,
          ]

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
     list_display = (                
        'email',
        'name',
        'first_name',
    )
   
     fields = (
        ( 'name', 'first_name'),
        'email'
    )
     search_fields = ['name']

admin.site.register(User)
admin.site.register(Student,StudentAdmin)
# admin.site.register(Coach)
admin.site.register(MembershipInProjects)

