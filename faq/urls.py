from django.urls import path
from .views import ArticleDetail, ArticleList, RequestCreate

urlpatterns = [
    path('list/', ArticleList.as_view(), name='faq_list'),
    path('<int:pk>/article/', ArticleDetail.as_view(), name='faq_detail'),
    path('request/create/', RequestCreate.as_view(), name='request_create'),
]
