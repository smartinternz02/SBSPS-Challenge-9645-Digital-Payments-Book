from calendar import c
from logging import exception
from math import prod
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer,PurchaseHistorySerializer,CartSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .permissions import IsAdmin
from .models import Cart, Product, PurchaseHistory,User

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    # import pdb;pdb.set_trace()
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    # import pdb;pdb.set_trace()
    serializer = UserLoginSerializer(data=request.data)
    print(request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      print(token)      
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status
    .HTTP_200_OK)

class CartPurchaseHistory(generics.GenericAPIView):
     permission_classes = [IsAuthenticated]
     renderer_classes =[UserRenderer]
     '''
     purchase history by user
     '''
     def get(self,request):
        cart_data = PurchaseHistory.objects.filter(cart_id=request.GET.get('cart_id'),customer=request.user.id).values_list('product__name','quantity','total_product_amount','cart_id__total')
        main_dict=list()
        for cart in cart_data:
          main_dict.append({'product_name':cart[0],'quantity':cart[1],'total_product_amount':int(cart[2]),'cart_total':int(cart[3])})
        return Response(main_dict,status=status.HTTP_200_OK)


class PaymentHistory(generics.GenericAPIView):
     permission_classes = [IsAuthenticated]
     renderer_classes =[UserRenderer]
     '''
     payment history of logged in user
     '''
     def get(self,request):
        payment_data  = Cart.objects.filter(username=request.user).values_list('id','total','status','updated')
        main_dict=list()
        for data in payment_data:
            main_dict.append({"cart_id":data[0],"total_amount":float(data[1]),"status":data[2], "last_updated":data[3].strftime("%m/%d/%Y, %H:%M:%S")})
        return Response(main_dict,status=status.HTTP_200_OK)
class Addproduct(generics.GenericAPIView):
  permission_classes = [IsAuthenticated,IsAdmin]
  renderer_classes = [UserRenderer]
  '''
    add product fora  admin
  '''
  def post(self,request):
     name = request.POST.get('product')
     wprice = request.POST.get('wholesaleprice')
     retail_price = request.POST.get('retailprice')
     quantity = request.POST.get('quantity')
     product = Product()
     try:
        product.name = name
        product.wholesaleprice = wprice
        product.retail_price = retail_price
        product.quantity = quantity
        product.save()
        return Response("Prodcuct Added Successfully",status=status.HTTP_200_OK)
     except Exception as e:
        print(e)
        return Response("Something Went Wrong.",status=status.HTTP_401_UNAUTHORIZED)

class GenerateProductHistory(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    renderer_classes = [UserRenderer]
    '''
    generate cart and purchase history
    '''
    def post(self,request):
      cust_id = request.data.get('user_id')
      customer = User.objects.get(id=cust_id)
      products = request.data.get('products')
      cart_total = request.data.get('cart_total')
      cart_status = request.data.get('status')
      try:
        cart = Cart.objects.create(username=customer, total=cart_total,status=cart_status)
        cart_id = cart
        for product in products:
            productObject = Product.objects.get(id=product[0])
            product_price= productObject.retail_price
            total_product_amount = int(product[1]) * product_price
            quantity = product[1]
            PurchaseHistory.objects.create(customer=customer,product=productObject,quantity=quantity,total_product_amount=total_product_amount,cart_id=cart_id)
        return Response('Purchase Success',status=status.HTTP_200_OK)
      except Exception as e:
        print(e)
        return Response('Something Went Wrong! Please Try again',status=status.HTTP_400_BAD_REQUEST)


class GetPurchaseHistory(generics.GenericAPIView):
    permission_classes =  [IsAuthenticated,IsAdmin]
    renderer_classes = [UserRenderer]
    serializer_class = PurchaseHistorySerializer
    '''
    purchase history for admin
    '''
    def get(self,request,*args,**kwargs):
        purchase_data = PurchaseHistory.objects.all()
        try:
            serializer = PurchaseHistorySerializer(purchase_data,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e,status=status.HTTP_400_BAD_REQUEST)

class GetCartHistory(generics.GenericAPIView):
    permission_classes =  [IsAuthenticated]
    renderer_classes = [UserRenderer]
    serializer_class = CartSerializer
    '''
    cart history by user
    '''
    def get(self,request,*args,**kwargs):
        cart_data = Cart.objects.filter(username=request.user.id)
        try:
            serializer = CartSerializer(cart_data,many=True)
            if serializer.is_valid:
              return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(e,status=status.HTTP_400_BAD_REQUEST)

class GetPurchaseHistoryByUser(generics.GenericAPIView):
    permission_classes =  [IsAuthenticated,IsAdmin]
    renderer_classes = [UserRenderer]
    serializer_class = PurchaseHistorySerializer
    '''
    cart details for user
    '''
    def get(self,request,*args,**kwargs):
      purchase_data = PurchaseHistory.objects.filter(cart_id__id = request.GET.get('cart_id'))
      try:
          serializer = PurchaseHistorySerializer(purchase_data,many=True)
          return Response(data=serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
          print(e)
          return Response(e,status=status.HTTP_400_BAD_REQUEST)

class UpdatePaymentStatus(generics.GenericAPIView):
    permission_classes =  [IsAuthenticated,IsAdmin]
    renderer_classes = [UserRenderer]
    serializer_class = CartSerializer
    '''
    update payment status
    '''
    def post(self,request,*args,**kwargs):
      cart_id=request.data.get('cart_id')
      user_id = request.data.get('user_id')
      cart_status=request.data.get('status')
      try:
        cart=Cart.objects.get(id=cart_id,username__id=user_id)
        cart.status = cart_status
        cart.save()
        return Response('status updated to {}'.format(cart_status),status=status.HTTP_200_OK)
      except Exception as e:
        print(e)
        return Response(e,status=status.HTTP_400_BAD_REQUEST)