from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import landing_page, login, signup
from store.views import store, customer, add_item, delete_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('store', store, name='store'),
    path('customer', customer, name='customer'),
    path('add_item', add_item, name='add_item'),
    path('delete_item', delete_item, name='delete_item'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
