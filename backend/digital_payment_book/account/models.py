from email.policy import default
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
status=(('Due','Due'),('Paid','Paid'),('Pending','Pending'))
#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, tc, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,

          tc=tc,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          tc=tc,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200,null=False)
  last_name = models.CharField(max_length=200,null=False)
  phone_number = models.BigIntegerField(null=False)
  tc = models.BooleanField()
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'tc']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin



class Product(models.Model):
    name= models.CharField(max_length=255, null=False)
    wholesaleprice = models.IntegerField(default=0)
    retail_price = models.IntegerField(default=0)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.id)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    status  = models.CharField(choices=status,null=True,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} ".format(self.id)

class PurchaseHistory(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total_product_amount = models.IntegerField(null=True)
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {}".format(self.customer, self.total_product_amount)


