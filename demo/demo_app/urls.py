from django.contrib import admin
from django.urls import path, include
from .views import home, login_user, books

urlpatterns = [
    path('adamin/', admin.site.urls),
    path('', home, name='home'),
    path('login_user', login_user, name='login'),
    path('books', books, name='list-books'),
]

"""urlpatterns = [
    path('adamin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('', home, name='home'),
    path('login_user', login_user, name='login'),
]"""