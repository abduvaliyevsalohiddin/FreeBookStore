from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.views import *
from bookapp.serializers import *
from uploadapp.models import Upload


class BookListView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                description="Filter by Category ID",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="author_id",
                in_=openapi.IN_QUERY,
                description="Filter by Author ID",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def get(self, request):
        books = Book.objects.all()
        book_name = request.query_params.get('title')
        author_id = request.query_params.get('author_id')
        year = request.query_params.get('year')
        category_id = request.query_params.get('category_id')

        if book_name:
            books = books.filter(title__icontains=book_name)
        if author_id:
            books = books.filter(author__id=author_id)
        if year:
            books = books.filter(year__icontains=year)
        if category_id:
            books = books.filter(category__id=category_id)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCategoryListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()


class BookCategoryRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()


class AuthorListView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class MyBookListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset
