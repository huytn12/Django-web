from django.conf.urls import url
from rango_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w-]+)/$',
        views.show_category, name='show_category'),
]