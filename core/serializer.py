from rest_framework import serializers
from .models import Job, Freelancer

class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    total_budget = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'description',
            'budgetPerHour',
            'hours',
            'total_budget',
            'freelancer',
            'created_at',
        ]
    def get_total_budget(self, obj):
            return obj.budgetPerHour * obj.hours

