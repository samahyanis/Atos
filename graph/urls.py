from django.urls import re_path as url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^graph/index/$', view=views.index, name="index"),
    url(r'^graph/index2/$', view=views.index2, name="index2"),
    url(r'^graph/index3/$', view=views.index3, name="index3"),
    url(r'^graph/index4/$', view=views.index4, name="index4"),
    url(r'^graph/accueil/$', view=views.accueil, name="accueil"),
    url(r'^graph/indextest/$', view=views.indextest, name="indextest"),
    url(r'^graph/indextest2/$', view=views.indextest2, name="indextest2"),
    url(r'^graph/index5/$', view=views.index5, name="index5"),
    url(r'^graph/index6/$', view=views.etude_na2, name="index6"),
    url(r'^graph/index7/$', view=views.etude_na3, name="index7"),
    url(r'^graph/index8/$', view=views.etude_na, name="index8"),
    url(r'^graph/index9/$', view=views.get_last_4csv, name="index9"),
    url(r'^graph/index10/$', view=views.get_last_4csv2, name="index10"),

]
