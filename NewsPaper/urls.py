
from django.contrib import admin
from django.urls import path, include
from .views import IndexView, upgrade_premium, upgrade_authors


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('news/', (include('news.urls')) ),
    path('upgrade/premium/', upgrade_premium, name='upgrade_premium'),
    path('upgrade/authors/', upgrade_authors, name='upgrade_authors')

]
