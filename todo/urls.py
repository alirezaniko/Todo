from django.urls import path
from . import views
urlpatterns = [
    path('generics/<pk>', views.TodoGenericsDetailView.as_view()),
    path('generics', views.TodosGenericApiView.as_view()),
    path('Users', views.UserGenericsApiView.as_view()),

]
