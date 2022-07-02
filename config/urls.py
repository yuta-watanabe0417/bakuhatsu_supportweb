from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import TopPage, FaqList, FaqDetail, ContentsList, ContentsDetail, InformationList, InformationDetail

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', TopPage.as_view(), name='index'),
   path('faq/list', FaqList.as_view(), name='faq/list'),
   path('faq/detail', FaqDetail.as_view(), name='faq/detail'),
   path('contents/list', ContentsList.as_view(), name='contents/list'),
   path('contents/detail', ContentsDetail.as_view(), name='contents/detail'),
   path('information/list', InformationList.as_view(), name='information/list'),
   path('information/detail', InformationDetail.as_view(), name='information/detail'),
   # path('blog/', include('blogs.urls')),
   # path('accounts/', include('accounts.urls')),
   # path('qa/', include('QA.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
