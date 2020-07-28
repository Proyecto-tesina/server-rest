from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(
    title="DRT Simulator API",
    description="API for manage statistics of the DRT simulation",
    version="1.0.0"
)

api_doc_view = TemplateView.as_view(
    template_name='doc.html',
    extra_context={'schema_url': 'api-schema'}
)


urlpatterns = [
    path('', api_doc_view, name='api-documentation'),
    path('api/', schema_view, name='api-schema'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('experiments.urls')),
]
