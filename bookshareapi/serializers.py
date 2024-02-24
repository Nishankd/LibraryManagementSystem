# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, SharedPermission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class SharedPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedPermission
        fields = ['id', 'permission']


class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    shared_with_names = serializers.SerializerMethodField()
    permission_given = serializers.SerializerMethodField()
    # shared_permissions = SharedPermissionSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'created_by', 'shared_with', 'shared_with_names', 'shared_permissions', 'permission_given']

    def get_shared_with_names(self, obj):
        return [user.username for user in obj.shared_with.all()]

    def get_permission_given(self, obj):
        # Assuming shared_permissions have a 'permission' field
        return [permission.permission for permission in obj.shared_permissions.all()]


