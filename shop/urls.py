from django.urls import path
from .import views
urlpatterns = [
 path("",views.index,name="ShopHome"),
 path("about/",views.about, name="AboutUS"),
 path("contact/",views.contact, name="ContactUS"),
 path("tracker/",views.tracker, name="TrackingStatus"),
 path("search/",views.search, name="Search"),
 path("products/<int:myid>",views.productView, name="prodView"),
 path("checkout/",views.checkout, name="Checkout"),




]
