from django.urls import path,include
from .import views
from django.utils.translation import gettext as _

app_name = 'main'

urlpatterns = [
	# path('',views.HomePageView.as_view(), name='home'),
	path('',views.home, name='home'),
	path('about/',views.about, name='about'),
	path('post/<slug:post_slug>', views.postDetailView, name='post_detail'),
	path('test/', views.test, name='test'),


	# path('about/',views.AboutPageView.as_view(), name='about'),
	# path('category/<pk>', views.CategoryDetailView.as_view(), name='category_detail'),
	# path('product/<pk>', views.ProductDetailView.as_view(), name='product_detail'),
	
	# path('category_delete/<pk>', views.category_delete, name='category_delete'),
	# path('product_delete/<pk>', views.product_delete, name='product_delete'),
	# path('error/', views.ErrorPageView.as_view(), name='error'),
]