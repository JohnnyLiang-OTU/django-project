from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.catalog, name="catalogo"),
    # path('catalogo/', views.catalog, name="catalogo"),
    # path('recommend/', views.recommend, name="recommend"),
    # path('product-form/', views.product_form, name="product-form"),
    path('administrador/edit/<str:pk>', views.edit_form, name="edit_form"),
    path('catalogo/delete/<str:pk>', views.delete_product, name="delete_product"),
    path('administrador/', views.administrador, name="administrador"),
    path('administrador/add/', views.product_form, name="add_product"),
    # path('product-form/success/', views.success, name="success")
    path('delete_models/', views.delete_models, name='delete_models'),
    path('errorazo/', views.test_error_email, name="error_raiser")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)