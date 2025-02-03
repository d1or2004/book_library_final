from django.urls import path
from .views import book_list, BookDetailView, BookDeleteView, BookUpdateView, BookListCreateView, BookUpdateDeleteView, \
    BookListApiView, CreateBookApiView, DetailBookApiView, BookDeleteApiView, BookUpdateApiView, BookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')
urlpatterns = [
    # path('', BookListApiView.as_view()),
    # path('books/', CreateBookApiView.as_view()),
    # path('books/<int:pk>/', DetailBookApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/', book_list),  # kam ishlatiladi funktions
    # path('books/<int:pk>/', BookDetailView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateView.as_view()),
    # # path('books/create/', BookCreateView.as_view()),
    # path('book-list-create/', BookListCreateView.as_view()),
    # path('book-delete-update/<int:pk>/', BookUpdateView.as_view()),
]

urlpatterns += router.urls
