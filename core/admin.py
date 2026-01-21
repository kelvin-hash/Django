from dataclasses import fields
from django.contrib import admin
from .models import Freelancer, Job

# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'budgetPerHour','hours','total_budget', 'freelancer', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'freelancer')
    ordering = ['-created_at']
    readonly_fields = ('created_at',)
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

    def total_budget(self, obj):
        return obj.budgetPerHour * obj.hours

    total_budget.short_description = "TotalBudget"

    def bulk_delete(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{request.user} deleted {count} jobs successfully.")

    bulk_delete.short_description = "Delete selected jobs"

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill', 'email')
    search_fields = ('name', 'skill')
    list_filter = ('skill','name')
    ordering = ['name']
    readonly_fields = ('email',)
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
    actions = ['bulk_delete']

    def bulk_delete(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{request.user} deleted {count} freelancers successfully.")

    bulk_delete.short_description = "Delete selected freelancers"

