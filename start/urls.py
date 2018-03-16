from django.urls import path

from . import views

app_name = 'start'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/uuid/', views.UUIDView.as_view(), name='uuid'),
    path('<int:pk>/uuid/results', views.UUIDView.as_view(), name='uuidresults'),
    path('addapi', views.addapi, name='addapi'),
]
# from django.urls import path

# from . import views

# app_name = 'start'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
