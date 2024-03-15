from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [

    path('index/', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),

    # path('index/', views.index, name='index'),
    # path("<int:question_id>/", views.detial, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]