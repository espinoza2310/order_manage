from django.urls import path
from Projectwebapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home, name="Home"),
    path('services',views.services, name="Services"),
    path('shop',views.shop, name="Shop"),
    path('contact',views.contact, name="Contact"),
    path('blog',views.blog, name="Blog"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
