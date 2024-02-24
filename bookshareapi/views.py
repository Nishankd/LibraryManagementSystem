from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *

# Create your views here.


class BookList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        queryset=(Book.objects.filter(created_by=user) | Book.objects.filter(shared_with=user)).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update_sharing(self, serializer):
        shared_permissions = self.request.data.get('shared_permissions', {})
        shared_permission_instances = []

        for permission in shared_permissions.items():
            shared_permission_instance = SharedPermission.objects.create(permission=permission)
            shared_permission_instances.append(shared_permission_instance)

        serializer.save(shared_permissions=shared_permission_instances)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, BookPermission]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_destroy(self, instance):
        instance.soft_deleted()
