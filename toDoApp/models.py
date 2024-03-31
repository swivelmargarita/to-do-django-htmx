from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Level(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'

    description = models.CharField(max_length=300)
    importance = models.SmallIntegerField(null=True, blank=True, choices=Level)
    urgency = models.SmallIntegerField(null=True, blank=True, choices=Level)
    due = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    is_dismissed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        curr_tags = ', '.join(tag.name for tag in self.tags.all())
        return f"Description: {self.description}, Tags: {curr_tags}\n\n"
