from dataclasses import fields
from django.contrib import admin
from .models import Freelancer, Job



#use decorators to register model to admin site
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    #columns to display in admin list view
    list_display = ('title', 'budgetPerHour','hours','total_budget', 'freelancer', 'created_at')
    #columns to search in admin list view
    search_fields = ('title', 'description')
    #what fields to use when filtering

    list_filter = ('created_at', 'freelancer')
    #feild used for ordering the list view
    ordering = ['-created_at']
    #view only fields
    readonly_fields = ('created_at',)
    #function to perform bulk delete action 
    fieldsets = (
        ('job info', {
            'fields': ('title', 'description','budgetPerHour', 'hours', 'freelancer')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
)
    actions = ['bulk_delete']
     
    # Calculate total budget(computed field) 
    def total_budget(self, obj):
        return obj.budgetPerHour * obj.hours
    #column label
    total_budget.short_description = "TotalBudget"
    #function to perform bulk delete action    
    def bulk_delete(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{request.user} deleted {count} jobs successfully.")

    bulk_delete.short_description = "Delete selected jobs"

    #freelancer dashboard view

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    #columns to display in admin list view
    list_display = ('name', 'skill', 'email')
    #columns to search in admin list view
    search_fields = ('name', 'skill')
    #what fields to use when filtering
    list_filter = ('skill','name')
    #feild used for ordering the list view
    ordering = ['name']
    #view only fields
    readonly_fields = ()
    #grouping fields in admin detail view
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'email')
        }
        ),
        ('Professional Info', {
            'fields': ('skill', 'bio'),
            'classes': ('collapse',)
        }),
)
    #set the bulk delete action
    actions = ['bulk_delete']

    def bulk_delete(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{request.user} deleted {count} freelancers successfully.")

    bulk_delete.short_description = "Delete selected freelancers"

