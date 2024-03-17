from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from uploadapp.serializers import *


class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        comments = Comment.objects.filter(book__id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user,
                book=Book.objects.get(id=pk)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        download = Download.objects.get(id=pk)
        book = download.book
        book.num_downloaded += 1
        book.save()
        serializer = DownloadSerializer(download)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
