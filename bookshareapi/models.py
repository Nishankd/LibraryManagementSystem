from django.db import models
from django.contrib.auth.models import User


class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    everything = models.Manager()
    objects = NonDeleted()

    def soft_deleted(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class SharedPermission(models.Model):
    permission = models.CharField(max_length=100)

    def __str__(self):
        return self.permission


class Book(SoftDelete):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_created')
    shared_with = models.ManyToManyField(User, related_name='books_shared', blank=True)
    shared_permissions = models.ManyToManyField(SharedPermission, related_name='books_shared_permission', blank=True)

    def __str__(self):
        return self.title



