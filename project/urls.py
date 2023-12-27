from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # pedido
    path('pedido/', include('pedido.urls')),
    
    # perfil
    path('perfil/', include('perfil.urls')),

    # admin
    path('admin/', admin.site.urls),

    # produto
    path('', include('produto.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # debug toolbar
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns