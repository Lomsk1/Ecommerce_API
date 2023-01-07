from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v1',
      description="API Requests and Links",
   ),
   public=True,
   permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('brand/', include('Brands.brand.urls'), name="Brand"),
    path('brand_category/', include('Brands.category.urls')),

    path('category/', include('Category.urls')),

    path('branch_working_hour/', include('Branch.working_hours.urls')),
    path('branch_coord/', include('Branch.coord.urls')),
    path('branch/', include('Branch.branch.urls')),

    path('weekly_sale/', include('WeeklySales.urls')),

    path('news/', include('News.urls')),

    path('product/', include('Products.product.urls')),
    path('product_image/', include('Products.product_images.urls')),
    path('product_specification/', include('Products.specification.urls')),
    path('product_basic/', include('Products.spec_basic.urls')),
    path('stock/', include('Products.branch.urls')),

    path('sub/', include('Subscription.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
