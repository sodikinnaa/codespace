
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.daftaruniv, name="daftaruniv"),
    path('adduniv', views.addUniv, name="addUniv"),
    path('deletedata/<str:prefix>', views.deleteUniv, name="deleteUniv"),
    path('singkronisasi/<str:hasil>', views.scrape_all_authors, name="scrape_all_authors"),
    path('putuniv', views.updateUniv, name="updateUniv"),
    path('edit/<str:prefix>', views.editUniv, name="addUniv"),
    path('postuniv', views.postuniv, name="postuniv"),
    path('detuniv/<str:prefix>', views.detuniv, name='homefunction'),
]