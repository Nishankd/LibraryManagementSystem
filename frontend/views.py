from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from bookshareapi.serializers import *
from bookshareapi.permissions import *
from django.contrib.auth.decorators import login_required
from bookshareapi.models import *
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer])
def book_list(request):
    if request.method == 'GET':
        books = (Book.objects.filter(shared_with=request.user) | Book.objects.filter(created_by=request.user)).distinct()
        serializer = BookSerializer(books, many=True)
        if request.accepted_renderer.format == 'html':
            return Response({'books': serializer.data}, template_name='list.html')
        else:
            return JsonResponse({'books': serializer.data})

    elif request.method == 'POST':

        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            # Perform any additional processing or validation as needed

            serializer.save(created_by=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, BookPermission])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer])
def book_detail(request, pk, template_name='detail.html'):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        if request.accepted_renderer.format == 'html':
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND, template_name=template_name)
        else:
            return JsonResponse({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        if request.accepted_renderer.format == 'html':
            return Response({'book': serializer.data}, template_name=template_name)
        else:
            return JsonResponse({'book': serializer.data})

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.accepted_renderer.format == 'html':
                return Response({'book': serializer.data}, template_name=template_name)
            else:
                return JsonResponse({'book': serializer.data})
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST, template_name=template_name)

    elif request.method == 'DELETE':
        book.soft_deleted()
        if request.accepted_renderer.format == 'html':
            return Response(status=status.HTTP_204_NO_CONTENT, template_name=template_name)
        else:
            return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
