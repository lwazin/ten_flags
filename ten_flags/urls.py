from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import landing_page, login, signup, logout
from store.views import store, customer, add_item, delete_item, create_item, generate_qrcode, receipt
from purchase.views import transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('store/<str:slug>', store, name='store'),
    path('customer', customer, name='customer'),
    path('add_item', add_item, name='add_item'),
    path('delete_item', delete_item, name='delete_item'),
    path('create_item', create_item, name='create_item'),
    path('generate_qrcode', generate_qrcode, name='generate_qrcode'),
    path('receipt', receipt, name='receipt'),
    path('transaction', transaction, name='transaction'),
    path('logout', logout, name='logout'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
