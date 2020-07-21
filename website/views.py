from django.shortcuts import render, redirect, reverse
from .forms import *
from PIL import Image
from resizeimage import resizeimage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serilizers
=======
from django.contrib import messages
import datetime, random, string, json
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

>>>>>>> 64b2e4937fc7ce39de6dbbb14c7799929714df23

# Create your views here.

def Dashboard(request):
    car_listt = Car.objects.all()
    for car_list in car_listt:
        print("============", car_list)
    # ad_view = AdViews.objects.
    page = request.GET.get('page', 1)
    paginator = Paginator(car_listt, 9)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'car_listt': car_listt,
        'blogs': blogs,

    }
    return render(request, 'templateq/default/home.html', context)


def dash(request):
    car_listt = Car.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(car_listt, 9)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'car_listt': car_listt,
        'blogs': blogs,

    }
    return render(request, 'templateq/default/home.html', context)


def admin(request):
    return render(request, 'car/dashboard.html')


def CarList(request, id):
    car_details = Car.objects.get(id=id)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)

    if request.user != "AnonymousUser":
        ad_views = AdViews()
        ad_views.user_ip = ip
        ad_views.ad_id = car_details
        ad_views.save()
        car_details.viewed += 1
        car_details.save()
    else:
        ad_views = AdViews()
        ad_views.user_id = request.user
        ad_views.user_ip = ip
        ad_views.ad_id = car_details
        ad_views.save()
        car_details.viewed += 1
        car_details.save()


    context = {
        'car_details': car_details
    }
    return render(request, 'car/CarList.html', context)


@login_required
def PostYourCar(request):
    if request.method == 'POST':
        try:
            car = Car()
            car.user = request.user
            car.name = request.POST['name']
            car.detail = request.POST['detail']
            car.price = request.POST['price']
            car.model_id = request.POST['model']
            car.mileage = request.POST['mileage']
            car.body_style_id = request.POST['body_style']
            car.transmission_id = request.POST['transmission']
            car.exterior_color_id = request.POST['exterior_color']
            car.interior_color_id = request.POST['interior_color']
            car.drivetrain_id = request.POST['drive_train']
            car.cylinder_count_id = request.POST['cylinder_count']
            car.seller_type_id = request.POST['seller_type']
            car.fuel_id = request.POST['fuel']
            car.phone = request.POST['phone']
            car.country_code = request.POST['country_code']
            car.save()

            for each in request.FILES.getlist('image'):
                car_image = CarImages()
                car_image.images = each

                car_image.save()
                car.images.add(car_image)
                car.save()
            return redirect(reverse('website:dashboard'))
        except Exception as e:
            print("++++++++++++", e)
            messages.error(request, 'Please enter all the fields correctly')

        # try:
        # if car.images.all() != '' or car.images.all() != None:
        #     for imagee in car.images.all():
        #         print("=============",imagee.images.path)
        #
        #         with open(imagee.images.path, 'r+b') as f:
        #             with Image.open(f) as image:
        #                 cover = resizeimage.resize_cover(image, [500, 323])
        #                 print("++++++++++",cover)
        #                 cover.save(imagee.images.path, image.format)
        #                 car.save()
        # except:
        #     pass
    car_list = Car.objects.all()
    model = Model.objects.all()
    body_style = Body.objects.all()
    transmission = Transmission.objects.all()
    exterior_color = Color.objects.all()
    interior_color = Color.objects.all()
    drive_train = Drivetrain.objects.all()
    cylinder_count = Cylinder.objects.all()
    seller_type = SellerType.objects.all()
    fuel = Fuel.objects.all()

    context = {
        'model': model,
        'body_style': body_style,
        'transmission': transmission,
        'exterior_color': exterior_color,
        'interior_color': interior_color,
        'drive_train': drive_train,
        'cylinder_count': cylinder_count,
        'seller_type': seller_type,
        'fuel': fuel,
        'car_list': car_list,

    }

    return render(request, 'car/PostYourCar.html', context)


# from .decorator import *


# def permissions(request):
#     url = request.resolver_match.app_name + ":" + request.resolver_match.url_name
#     print(url)
#
#     count = 0
#     for each in request.user.roles.all():
#         if (each.id == 15) or (each.id == 4):
#             return True
#
#         for item in Permissions.objects.all():
#             if (each.id == item.role_id) and (url == item.action):
#                 count = count + 1
#
#     if count > 0:
#         return True
#     else:
#         return False
@login_required
# @user_check
def EditYourCar(request, id):
    user_check = Car.objects.filter(id=id, user=request.user)
    if user_check.count() <= 0:
        return redirect(reverse('website:dashboard'))

    if request.method == 'POST':
        car_edit = Car.objects.get(id=id)
        try:
            car_edit.name = request.POST['name']
            car_edit.detail = request.POST['detail']
            car_edit.price = request.POST['price']
            car_edit.model_id = request.POST['model']
            car_edit.mileage = request.POST['mileage']
            car_edit.body_style_id = request.POST['body_style']
            car_edit.transmission_id = request.POST['transmission']
            car_edit.exterior_color_id = request.POST['exterior_color']
            car_edit.interior_color_id = request.POST['interior_color']
            car_edit.drivetrain_id = request.POST['drive_train']
            car_edit.cylinder_count_id = request.POST['cylinder_count']
            car_edit.seller_type_id = request.POST['seller_type']
            car_edit.country_code = request.POST['country_code']
            car_edit.fuel_id = request.POST['fuel']
            car_edit.phone = request.POST['phone']
            car_edit.save()

            for each in request.FILES.getlist('image'):
                car_image = CarImages()
                car_image.images = each
                car_image.save()
                car_edit.images.add(car_image)
                car_edit.save()
            return redirect(reverse('website:dashboard'))
        except Exception as e:
            print("=============", e)
            messages.error(request, 'Please enter all the fields correctly')

    # try:
    # if car.images.all() != '' or car.images.all() != None:
    #     for imagee in car.images.all():
    #         print("=============",imagee.images.path)
    #
    #         with open(imagee.images.path, 'r+b') as f:
    #             with Image.open(f) as image:
    #                 cover = resizeimage.resize_cover(image, [500, 323])
    #                 print("++++++++++",cover)
    #                 cover.save(imagee.images.path, image.format)
    #                 car.save()
    # except:
    #     pass
    car_edit = Car.objects.get(id=id)

    car_list = Car.objects.all()
    model = Model.objects.all()
    body_style = Body.objects.all()
    transmission = Transmission.objects.all()
    exterior_color = Color.objects.all()
    interior_color = Color.objects.all()
    drive_train = Drivetrain.objects.all()
    cylinder_count = Cylinder.objects.all()
    seller_type = SellerType.objects.all()
    fuel = Fuel.objects.all()

    context = {
        'model': model,
        'car_edit': car_edit,
        'body_style': body_style,
        'transmission': transmission,
        'exterior_color': exterior_color,
        'interior_color': interior_color,
        'drive_train': drive_train,
        'cylinder_count': cylinder_count,
        'seller_type': seller_type,
        'fuel': fuel,
        'car_list': car_list,

    }

    return render(request, 'car/edit_post_car.html', context)


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def signup(request):
    if request.method == "POST":
        user = User()

        if request.POST['password'] == request.POST['confirm_password']:
            user = User()
            try:
                User.objects.get(username__iexact=request.POST['username'])
                context = {
                    'message': "User already Exist"
                }
                return render(request, 'registration/signup.html', context)
            except ObjectDoesNotExist:
                # com = re.compile(r'^[0-9]{10}[^a-zA-Z]*$')
                # print(bool(com.match(request.POST['phone'])))
                # if com.match(request.POST['phone']):
                user.username = request.POST['username']
                user.email = request.POST['email']
                user.set_password(request.POST['password'])
                user.save()
                customer = Profile()
                customer.user = user
                customer.phone = request.POST['phone']
                customer.save()
                return redirect(reverse('login'))

        #
        # else:
        #     context = {
        #         'message': "Invalid Mobile Number"
        #     }
        #     return render(request, 'registration/signup.html', context)
        else:
            context = {
                'message': "Password is Mismatch",

            }
            return render(request, 'registration/signup.html', context)

    return render(request, "registration/signup.html")


def listing_car(request):
    car = Car.objects.all()
    context = {
        'car': car
    }
    return render(request, 'car/listing_cars.html', context)


@login_required
def AddPostCar(request):
    model = Model.objects.all()
    car = Car()
    if request.method == 'POST':
        car.name = request.POST['name']
        car.detail = request.POST['detail']
        car.price = request.POST['price']
        car.model_id = request.POST['model']
        car.mileage = request.POST['mileage']
        car.body_style_id = request.POST['body_style']
        car.transmission_id = request.POST['transmission']
        car.exterior_color_id = request.POST['exterior_color']
        car.interior_color_id = request.POST['interior_color']
        car.drivetrain_id = request.POST['drive_train']
        car.cylinder_count_id = request.POST['cylinder_count']
        car.seller_type_id = request.POST['seller_type']
        car.fuel_id = request.POST['fuel']
        car.phone = request.POST['phone']
        if 'car_image' in request.FILES:
            car.car_image = request.FILES['car_image']
        car.save()
        try:
            if car.car_image != '' or car.car_image != None:
                with open(car.car_image.path, 'r+b') as f:
                    with Image.open(f) as image:
                        cover = resizeimage.resize_cover(image, [500, 323])
                        cover.save(car.car_image.path, image.format)
                        car.save()
        except:
            pass

        return redirect(reverse('website:listing_car'))
    body_style = Body.objects.all()
    transmission = Transmission.objects.all()
    exterior_color = Color.objects.all()
    interior_color = Color.objects.all()
    drive_train = Drivetrain.objects.all()
    cylinder_count = Cylinder.objects.all()
    seller_type = SellerType.objects.all()
    fuel = Fuel.objects.all()

    context = {
        'model': model,
        'body_style': body_style,
        'transmission': transmission,
        'exterior_color': exterior_color,
        'interior_color': interior_color,
        'drive_train': drive_train,
        'cylinder_count': cylinder_count,
        'seller_type': seller_type,
        'fuel': fuel,

    }
    return render(request, 'car/post_your_car.html', context)


@login_required
def AddMaker(request):
    if request.method == 'POST':
        form = MakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:maker_list'))
    form = MakerForm()
    return render(request, 'car/maker.html', {'form': form})


@login_required
def AddModel(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:model_list'))
    form = ModelForm()
    return render(request, 'car/model.html', {'form': form})


@login_required
def AddColor(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:color_list'))
    form = ColorForm()
    return render(request, 'car/color.html', {'form': form})


@login_required
def AddTransmission(request):
    if request.method == 'POST':
        form = TransmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:transmission_list'))
    form = TransmissionForm()
    return render(request, 'car/transmission.html', {'form': form})


@login_required
def AddCylinder(request):
    if request.method == 'POST':
        form = CylinderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:cylinder_list'))
    form = CylinderForm()
    return render(request, 'car/cylinder.html', {'form': form})


@login_required
def AddDrive_train(request):
    if request.method == 'POST':
        form = DrivetrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:driven_type_list'))
    form = DrivetrainForm()
    return render(request, 'car/drive_train.html', {'form': form})


@login_required
def AddSeller_type(request):
    if request.method == 'POST':
        form = SellerTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:seller_type_list'))
    form = SellerTypeForm()
    return render(request, 'car/seller_type.html', {'form': form})


@login_required
def AddFuel(request):
    if request.method == 'POST':
        form = FuelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:fuel_list'))
    form = FuelForm()
    return render(request, 'car/fuel.html', {'form': form})


@login_required
def AddBody(request):
    if request.method == 'POST':
        form = BodyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:body_list'))
    form = BodyForm()
    return render(request, 'car/body.html', {'form': form})


@login_required
def body_list(request):
    body_list = Body.objects.all()
    context = {
        'body_list': body_list
    }
    return render(request, 'car/body_list.html', context)


@login_required
def fuel_list(request):
    fuel_list = Fuel.objects.all()
    context = {
        'fuel_list': fuel_list
    }
    return render(request, 'car/fuel_list.html', context)


@login_required
def seller_type_list(request):
    seller_type_list = SellerType.objects.all()
    context = {
        'seller_type_list': seller_type_list
    }
    return render(request, 'car/seller_type_list.html', context)


@login_required
def driven_type_list(request):
    driven_type_list = Drivetrain.objects.all()
    context = {
        'driven_type_list': driven_type_list
    }
    return render(request, 'car/driven_train_list.html', context)


@login_required
def cylinder_list(request):
    cylinder_list = Cylinder.objects.all()
    context = {
        'cylinder_list': cylinder_list
    }
    return render(request, 'car/cylinder_list.html', context)


@login_required
def transmission_list(request):
    transmission_list = Transmission.objects.all()
    context = {
        'transmission_list': transmission_list
    }
    return render(request, 'car/transmission_list.html', context)


@login_required
def color_list(request):
    color_list = Color.objects.all()
    context = {
        'color_list': color_list
    }
    return render(request, 'car/color_list.html', context)


@login_required
def model_list(request):
    model_list = Model.objects.all()
    context = {
        'model_list': model_list
    }
    return render(request, 'car/model_list.html', context)


@login_required
def maker_list(request):
    maker_list = Maker.objects.all()
    context = {
        'maker_list': maker_list
    }
    return render(request, 'car/maker_list.html', context)


<<<<<<< HEAD
class Filter(APIView):

    def get(self, request):
        context ={
            "Response":"working"
        }
        return Response(context)

    def post(self, request):

        if "Transmission" in request.POST:
            print(request.POST["Transmission"])
        car_list = Car.objects.all()
        serializer = serilizers.CarsSerializer(car_list, many=True)


        context = {"Res":"working"}
        return Response(serializer.data)
=======
@login_required
def ManageYourCar(request):
    car_list = Car.objects.filter(user=request.user)
    context = {
        'car_list': car_list

    }
    return render(request, 'profiledetails/managecarlist.html', context)


@login_required
def image_delete(request, id, caredit_id):
    image = CarImages.objects.get(id=id).delete()
    return redirect(reverse('website:EditYourCar', kwargs={'id': caredit_id}))


@login_required
def DeleteMyCarList(request, id):
    image = Car.objects.get(user=request.user, id=id).delete()
    return redirect(reverse('website:ManageYourCar'))


def OTP_generator(stringLength):
    password_numbers = string.digits
    return ''.join(random.choice(password_numbers) for i in range(stringLength))


def reg_generator(stringLength):
    password_numbers = string.digits + string.ascii_letters
    return ''.join(random.choice(password_numbers) for i in range(stringLength))


from django.core.mail import send_mail
import datetime
import pytz
from django.views.decorators.csrf import csrf_exempt

from carwebsite.settings import *

utc = pytz.UTC


@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        try:

            user = Profile.objects.get(user__username__iexact=request.POST['username'])
            # if user.otp_expire is not None:
            #     otp_expire = user.otp_expire.replace(tzinfo=utc)
            # else:
            #     otp_expire = None

            datetimenow = datetime.datetime.now().replace(tzinfo=utc)

            if user.otp_expire is None or user.otp_expire < datetimenow:
                otp = OTP_generator(6)
                custom_secret = reg_generator(255)
                user.gen_otp = int(otp)
                user.retry_otp_count = user.retry_otp_count + 1
                user.otp_expire = datetime.datetime.now() + datetime.timedelta(minutes=10)
                user.custom_secret = custom_secret
                user.save()
                sms_message = 'Dear ' + user.user.username + ',\nOTP to reset the password is ' + otp + '. Please do not share with anyone. OTP will expire in 10 Minutes.'
                subject = 'Forgot Password - OTP'
                email = []
                email.append(user.user.email)
                email_from = settings.EMAIL_HOST_USER
                send_mail(subject, sms_message, email_from, email)
                custom_secret = reg_generator(255)
                user.custom_secret = custom_secret
                user.save()
                messages.success(request, 'OTP has been send to register e-Mail')
                return redirect(reverse('website:otp_forgot_password', kwargs={'secret': user.custom_secret}))
            else:
                messages.info(request, 'Otp Valid until 10 minutes')
        except Exception as e:

            messages.error(request, 'Request username is not registered')

    return render(request, 'registration/forgot_password.html')


@csrf_exempt
def reset_password(request, secret):
    try:
        user = Profile.objects.get(custom_secret=secret)
        user_name = User.objects.get(id=user.user.id)

        if request.method == 'POST':
            if request.POST['password'] == request.POST['confirm_password']:
                user_name.set_password(request.POST['password'])
                user_name.save()
                user.custom_secret = None
                user.retry_otp_count = 0
                user.gen_otp = None
                user.otp_expire = None
                user.save()
                messages.success(request, 'Password Reset Successfully')
                return redirect(reverse('login'))
            else:
                messages.error(request, 'password and confirm password is not match')
    except:
        messages.error(request, 'Session Expired')
        return redirect(reverse('website:dashboard'))
    return render(request, 'registration/reset_password.html')


@csrf_exempt
def otp_forgot_password(request, secret):
    try:
        user = Profile.objects.get(custom_secret=secret)
        if request.method == 'POST':
            datetimenow = datetime.datetime.now().replace(tzinfo=utc)

            if user.otp_expire > datetimenow:

                if int(user.gen_otp) == int(request.POST['check_otp']):

                    custom = reg_generator(255)
                    user.custom_secret = custom
                    user.otp_expire = None
                    user.gen_otp = None
                    user.save()
                    messages.success(request, 'Otp verified Successfully')
                    return redirect(reverse('website:reset_password', kwargs={'secret': user.custom_secret}))
                else:
                    messages.error(request, 'Invalid OTP, try again')
                    return redirect(reverse('website:otp_forgot_password', kwargs={'secret': user.custom_secret}))
            else:
                otp = OTP_generator(6)
                custom_secret = reg_generator(255)
                user.gen_otp = int(otp)
                user.retry_otp_count = user.retry_otp_count + 1
                user.otp_expire = datetime.datetime.now() + datetime.timedelta(minutes=10)
                user.custom_secret = custom_secret
                user.save()
                sms_message = 'Dear ' + user.user.username + ',\nOTP to reset the password is ' + otp + '. Please do not share with anyone. OTP will expire in 10 Minutes.'
                subject = 'Forgot Password - OTP'
                email = []
                email.append(user.user.email)
                email_from = settings.EMAIL_HOST_USER
                send_mail(subject, sms_message, email_from, email)
                custom_secret = reg_generator(255)
                user.custom_secret = custom_secret
                user.save()
                messages.error(request, 'OTP Expired, New OTP has been sent.')
                return redirect(reverse('website:otp_forgot_password', kwargs={'secret': user.custom_secret}))
    except:
        messages.error(request, 'Session Expired, Try again')
        return redirect(reverse('website:dashboard'))
    return render(request, 'registration/forgot_password2.html')


@login_required
def change_password(request):
    user_check = User.objects.get(id=request.user.id, username=request.user.username)

    if request.method == 'POST':
        if check_password(request.POST['current_password'], user_check.password):
            if check_password(request.POST['new_password'], user_check.password):
                messages.error(request, 'New Password is same as Old Password')
                return redirect(reverse('website:change_password'))
            if request.POST['new_password'] == request.POST['confirm_password']:
                user_check.set_password(request.POST['new_password'])
                user_check.save()
                messages.success(request, 'Password Changed Successfully. Please log in back.')
                return redirect(reverse('logout'))
            else:
                messages.error(request, 'New and Confirm Password do not match')
                return redirect(reverse('website:change_password'))
        else:
            messages.error(request, 'Old Password is Wrong')
            return redirect(reverse('website:change_password'))
    return render(request, 'registration/change_password.html')


@login_required
def profile(request):
    user = Profile.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        try:
            user.user.username = request.POST['username']
            user.user.first_name = request.POST['first_name']
            user.user.last_name = request.POST['last_name']
            user.user.email = request.POST['email']
            user.phone = request.POST['phone']
            user.city = request.POST['city']
            user.country_code = request.POST['country_code']
            user.user.save()
            user.save()
        except Exception as e:
            print("profile edit details", e)
            messages.error(request, 'Please check and fill Correctly')

    context = {
        'user': user
    }
    return render(request, 'car/profile.html', context)


def car_image(request):
    return render(request, 'car/car_image.html')
>>>>>>> 64b2e4937fc7ce39de6dbbb14c7799929714df23
