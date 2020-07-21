from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "website"
urlpatterns = [
    path('', views.dash, name="dashb"),
    path('landing/', views.Dashboard, name="dashboard"),
    path('admin/', views.admin, name="admin"),
    path('CarList/<int:id>/', views.CarList, name="CarList"),
    path('signup/', views.signup, name="signup"),
    path('PostYourCar/', views.PostYourCar, name="PostYourCar"),
    path('EditYourCar/<int:id>/', views.EditYourCar, name="EditYourCar"),
    path('DeleteMyCarList/<int:id>/', views.DeleteMyCarList, name="DeleteMyCarList"),
    path('listing_car/', views.listing_car, name="listing_car"),
    path('postcar/', views.AddPostCar, name="PostCar"),
    path('add_maker/', views.AddMaker, name="maker"),
    path('add_model/', views.AddModel, name="model"),
    path('add_color/', views.AddColor, name="color"),
    path('add_transmission/', views.AddTransmission, name="transmission"),
    path('add_cylinder/', views.AddCylinder, name="cylinder"),
    path('add_drive_train/', views.AddDrive_train, name="drive_train"),
    path('add_seller_type/', views.AddSeller_type, name="seller_type"),
    path('add_fuel/', views.AddFuel, name="fuel"),
    path('add_body/', views.AddBody, name="body"),
    path('body_list/', views.body_list, name="body_list"),
    path('fuel_list/', views.fuel_list, name="fuel_list"),
    path('seller_type_list/', views.seller_type_list, name="seller_type_list"),
    path('driven_type_list/', views.driven_type_list, name="driven_type_list"),
    path('cylinder_list/', views.cylinder_list, name="cylinder_list"),
    path('transmission_list/', views.transmission_list, name="transmission_list"),
    path('color_list/', views.color_list, name="color_list"),
    path('model_list/', views.model_list, name="model_list"),
    path('maker_list/', views.maker_list, name="maker_list"),
<<<<<<< HEAD
    path('filter/', views.Filter.as_view(), name="filter"),
=======
    path('ManageYourCar/', views.ManageYourCar, name="ManageYourCar"),
    path('image_delete/<int:id>/<int:caredit_id>/', views.image_delete, name="image_delete"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('forgot_password/<str:secret>/', views.otp_forgot_password, name="otp_forgot_password"),
    path('reset_password/<str:secret>/', views.reset_password, name="reset_password"),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
    path('car_image/', views.car_image, name='car_image'),
>>>>>>> 64b2e4937fc7ce39de6dbbb14c7799929714df23

]
