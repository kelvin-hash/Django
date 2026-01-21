from django.db import models
    # Create your models here.

class Freelancer(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    budgetPerHour = models.IntegerField()
    hours= models.IntegerField()
    freelancer = models.ForeignKey(
        Freelancer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='jobs'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
