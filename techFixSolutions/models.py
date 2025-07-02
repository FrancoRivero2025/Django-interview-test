from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):    
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=765, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    whatsapp_phone = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        db_index=True,
        verbose_name="Telefono WhatsApp (+54)"
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
    )
    
    @property
    def full_name(self):
        return u"{} {}".format(self.first_name if self.first_name else '',
                               self.last_name if self.last_name else '')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserManager()

    class Meta:
        app_label = 'techfixsolutions'
        verbose_name = _('TechFixSolutions User')
        verbose_name_plural = _('TechFixSolutions Users')  


class Scheme(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'techfixsolutions'
        verbose_name = _('Order Scheme')
        verbose_name_plural = _('Order Schemes')


class Company(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=80)
    website = models.CharField(max_length=100)

    class Meta:
        app_label = 'techfixsolutions'
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class Order(models.Model):
    REQUEST = 0
    ORDER = 1

    REQUEST_TYPE = (
        (SOLICITUD, 'Request'),
        (ORDER, 'Order'),
    )
    type_request = models.IntegerField(
        choices=REQUEST_TYPE,
        db_index=True,
        default=ORDER
    )
    client = models.ForeignKey(
        User,
        verbose_name='client',
        on_delete=models.CASCADE
    )
    scheme = models.ForeignKey(
        Scheme,
        null=True,
        on_delete=models.CASCADE
    )
    hours_worked = models.IntegerField(default=0)

    class Meta:
        app_label = 'techfixsolutions'
        verbose_name_plural = 'orders'
        ordering = ('-id', )
