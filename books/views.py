from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status, viewsets


class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True).data
        data = {
            'status': status.HTTP_200_OK,
            'count': books.count(),
            'message': 'success',
            'books': serializer

        }
        return Response(data)


class CreateBookApiView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'success',
                'data': serializer.data

            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBookApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            data = {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data': serializer.data

            }
            return Response(data)
        except Book.DoesNotExist:
            a = {
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'book not found',

            }
            return Response(a)


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            # book = get_object_or_404(pk=pk) bunga try iwlatmaslikk uchun
            book.delete()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'success',

            }
            return Response(data)
        except Exception:
            a = {
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'book not found',
            }
            return Response(a)


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        """Book yangilash uchun PUT so'rov"""
        book = get_object_or_404(Book, pk=pk)

        # Request ma'lumotlarini berilgan kitob bilan serialize qilish
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Book successfully updated',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Validation failed',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class BookViewSet(ModelViewSet):
     queryset = Book.objects.all()
     serializer_class = BookSerializer

    
    
    
    
    
    
    
    
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):  # uchirish, korish, update
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# funksion viws
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)  # ko'p aybyektlat borligini bildiradi, lit korinishida
    return Response(serializer.data)
