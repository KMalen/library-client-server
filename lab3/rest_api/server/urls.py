from django.urls import path

from server import views

urlpatterns = [
    path("api/bookinstances", views.BookInstanceViewAPI.as_view(), name="book_instances"),
    path("api/bookinstance/<int:pk>", views.BookInstanceViewId.as_view(), name="book_instances_delete_and_update"),
    path("api/authors", views.AuthorViewAPI.as_view(), name="authors"),
    path("api/author/<int:pk>", views.AuthorViewId.as_view(), name="authors_delete_and_update"),
    path("api/books", views.BookViewAPI.as_view(), name="books"),
    path("api/book/<int:pk>", views.BookViewId.as_view(), name="books_delete_update"),
    path("api/genres", views.GenreViewAPI.as_view(), name="genres"),
    path("api/genre/<int:pk>", views.GenreViewId.as_view(), name="genres_delete_and_update"),
    path("api/languages", views.LanguageViewAPI.as_view(), name="languages"),
    path("api/language/<int:pk>", views.LanguageViewId.as_view(), name="languages_delete_update"),

]