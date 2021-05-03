from rest_framework.views import APIView
from server.models import *
from server.serializers import *
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class AuthorViewId(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def delete(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        author.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        data = request.data
        serializer = AuthorSerializer(instance=author, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            author = serializer.save()
        return Response({
            "success": "Author '{}' updated successfully".format(author)
        })


class AuthorViewAPI(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        author = request.data
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({"success": "Author '{}' created successfully".format(author_saved)})


class BookViewId(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()
        return Response({
            "message": "Book with book code `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()
        return Response({
            "success": "Book '{}' updated successfully".format(book)
        })


class BookViewAPI(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = request.data
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book)})


class GenreViewId(APIView):
    def get(self, request, pk):
        genre = get_object_or_404(Genre.objects.all(), pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def delete(self, request, pk):
        genre = get_object_or_404(Genre.objects.all(), pk=pk)
        genre.delete()
        return Response({
            "message": "Genre with id `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        genre = get_object_or_404(Genre.objects.all(), pk=pk)
        data = request.data
        serializer = GenreSerializer(instance=genre, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            genre = serializer.save()
        return Response({
            "success": "Genre '{}' updated successfully".format(genre)
        })


class GenreViewAPI(APIView):

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        genre = request.data
        serializer = GenreSerializer(data=genre)
        if serializer.is_valid(raise_exception=True):
            genre = serializer.save()
        return Response({"success": "Genre '{}' created successfully".format(genre)})


class BookInstanceViewId(APIView):
    def get(self, request, pk):
        book_instance = get_object_or_404(BookInstance.objects.all(), pk=pk)
        serializer = BookInstanceSerializer(book_instance)
        return Response(serializer.data)

    def delete(self, request, pk):
        book_instance = get_object_or_404(BookInstance.objects.all(), pk=pk)
        book_instance.delete()
        return Response({
            "message": "Genre with id `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        book_instance = get_object_or_404(BookInstance.objects.all(), pk=pk)
        data = request.data
        serializer = BookInstanceSerializer(instance=book_instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_instance = serializer.save()
        return Response({
            "success": "Book instance '{}' updated successfully".format(book_instance)
        })


class BookInstanceViewAPI(APIView):

    def get(self, request):
        book_instances = BookInstance.objects.all()
        serializer = BookInstanceSerializer(book_instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_instance = request.data
        serializer = BookInstanceSerializer(data=book_instance)
        if serializer.is_valid(raise_exception=True):
            book_instance = serializer.save()
        return Response({"success": "Book instance '{}' created successfully".format(book_instance)})


class LanguageViewId(APIView):
    def get(self, request, pk):
        language = get_object_or_404(Language.objects.all(), pk=pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def delete(self, request, pk):
        language = get_object_or_404(Language.objects.all(), pk=pk)
        language.delete()
        return Response({
            "message": "Language with id `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        language = get_object_or_404(Language.objects.all(), pk=pk)
        data = request.data
        serializer = LanguageSerializer(instance=language, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            language = serializer.save()
        return Response({
            "success": "Language '{}' updated successfully".format(language)
        })


class LanguageViewAPI(APIView):

    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    def post(self, request):
        language = request.data
        serializer = LanguageSerializer(data=language)
        if serializer.is_valid(raise_exception=True):
            genre = serializer.save()
        return Response({"success": "Language '{}' created successfully".format(language)})