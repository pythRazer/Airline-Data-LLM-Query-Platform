from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import query_db1b_data
app_name = "adqp"
urlpatterns = [
    path('', views.home_page, name="home-page"),

    path('query/', query_db1b_data, name='query_db1b_data'),
    # Other URLs
    path('api/', include('adqp.api.urls')),  # Include API URLs


    path('text-to-sql', views.text_to_sql_view, name="text-to-sql"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
