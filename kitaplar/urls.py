from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from writers.views import WriterViewSet
from books.views import BookViewSet

router = routers.DefaultRouter()

router.register('writers', WriterViewSet, basename='writers')
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
