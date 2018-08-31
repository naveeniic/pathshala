from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from student import views


urlpatterns = [
    url(r'^Student/$', views.StudentList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
