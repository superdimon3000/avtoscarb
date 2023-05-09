from django.urls import path
from .views import search, TermsView, AboutView, CollaborationView, GuaranteeView
from . import views

app_name = 'shop'

urlpatterns = [
    path('search/', search, name='search'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('about/', AboutView.as_view(), name='about'),
    path('collaboration/', CollaborationView.as_view(), name='collaboration'),
    path('guarantee/', GuaranteeView.as_view(), name='guarantee'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
