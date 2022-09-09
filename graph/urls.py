from django.urls import re_path as url
from . import views
from django.urls import path

urlpatterns = [
    path("login", views.login),
    path("logout", views.logout),
    path("filter/<str:date>/<str:job>", views.filtre),
    path("filtre_/<str:date>", views.filtre_NA),
    path("recherch/<str:date>", views.recherche_accueil),
    # path("update_rows", views.update_rows),
    path("get_duration_per_task/<str:date>", views.get_duration_per_task),
    path("end_time_start_time/<str:date>", views.end_time_start_time),
    url(r'^graph/index/$', view=views.index, name="index"),
    path("update_dashboard/" ,views.update_dashboard , name='update_dashboard'),
    url(r'^graph/index2/$', view=views.index2, name="index2"),
    url(r'^graph/index3/$', view=views.index3, name="index3"),
    path('graph/index4/<str:date>/<str:job>', view=views.index4, name="index4"),
    path('graph/index14/<str:date>/<str:job>', view=views.index14, name="index14"),
    url(r'^graph/accueil/$', view=views.accueil, name="accueil"),
    path('graph/index5/<str:date2>/<str:date>', view=views.indextest, name="indextest"),
    path('graph/index52/<str:date2>/<str:date>', view=views.indextest11, name="indextest11"),
    path('graph/index5/<str:date>', view=views.indextest2, name="indextest2"),
    url(r'^graph/index5/$', view=views.index5, name="index5"),
    url(r'^graph/index6/$', view=views.etude_na2, name="index6"),
    url(r'^graph/index7/$', view=views.etude_na3, name="index7"),
    url(r'^graph/index8/$', view=views.etude_na, name="index8"),
    url(r'^graph/index9/$', view=views.get_last_4csv, name="index9"),
    url(r'^graph/index10/$', view=views.get_last_4csv2, name="index10"),
    url(r'^graph/index52/$', view=views.index52, name="index52"),
    path('graph/index52/<str:date>', view=views.indextest22, name="indextest22"),

]
