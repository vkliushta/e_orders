from django.core.validators import MinValueValidator, validate_image_file_extension
from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    facebook_name = models.CharField(
        "Facebook name of the client", max_length=75, unique=True
    )
    phone_number = PhoneNumberField("Phone number used for Nova Poshta", unique=True)
    post_address = models.CharField(
        "Nova Poshta address", max_length=200, null=True, blank=True
    )

    def __str__(self):
        return self.facebook_name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item_name = models.CharField("Name of the ordered item", max_length=100)
    image = models.ImageField(
        "Image of the order",
        null=True,
        blank=True,
        validators=[validate_image_file_extension],
    )
    size = models.CharField(max_length=4, null=True, blank=True)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    is_active = models.BooleanField(default=True)
    is_sent = models.BooleanField(default=False)
    date = models.DateTimeField("Date-time of the order", default=now, blank=True)
    price = models.DecimalField("Price per unit", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name
