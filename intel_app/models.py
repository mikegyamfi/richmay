from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=250, null=False, blank=False)
    phone = models.PositiveIntegerField(null=True, blank=True)
    wallet = models.FloatField(null=True, blank=True, default=0.0)
    choices = (
        ("User", "User"),
        ("Agent", "Agent"),
        ("Super Agent", "Super Agent"),
    )
    status = models.CharField(max_length=250, null=False, blank=False, choices=choices)
    password1 = models.CharField(max_length=100, null=False, blank=False)
    password2 = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.username


class AdminInfo(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    momo_number = models.PositiveBigIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mtn_active = models.BooleanField(default=False)
    at_active = models.BooleanField(default=False)
    telecel_service_active = models.BooleanField(default=False)
    choices = (
        ("MTN Mobile Money", "MTN Mobile Money"),
        ("Vodafone Cash", "Vodafone Cash"),
        ("AT Money", "AT Money")
    )
    payment_channel = models.CharField(max_length=250, choices=choices)
    afa_price = models.FloatField(null=True, blank=True)
    mtn_api_status = models.BooleanField(default=True)
    telecel_active = models.BooleanField(default=True)
    ishare_choices = (
        ("Gyasi", "Gyasi"),
        ("Value4Moni", "Value4Moni"),
        ("Geosams", "Geosams")
    )
    ishare_source = models.CharField(max_length=250, null=True, blank=True, choices=ishare_choices, default="Value4Moni")


class IShareBundleTransaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bundle_number = models.BigIntegerField(null=False, blank=False)
    offer = models.CharField(max_length=250, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False, default=0.0)
    bundle_amount = models.FloatField()
    reference = models.CharField(max_length=20, null=False, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.bundle_number} - {self.reference}"
    

class IshareBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class AgentIshareBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class SuperAgentIshareBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class AgentBigTimeBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class SuperAgentBigTimeBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class BigTimeBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class BigTimeTransaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bundle_number = models.BigIntegerField(null=False, blank=False)
    offer = models.CharField(max_length=250, null=False, blank=False)
    bundle_amount = models.FloatField()
    amount = models.FloatField(null=False, blank=False, default=0.0)
    reference = models.CharField(max_length=20, null=False, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    choices = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Failed", "Failed")
    )
    transaction_status = models.CharField(max_length=100, choices=choices, default="Pending")
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.bundle_number} - {self.reference}"


class AFARegistration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(null=False, blank=False)
    gh_card_number = models.CharField(null=False, blank=False, max_length=256)
    name = models.CharField(max_length=250, null=False, blank=False)
    occupation = models.CharField(max_length=20, null=False, blank=True)
    reference = models.CharField(max_length=20, null=False, blank=True)
    date_of_birth = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=250, null=True, blank=True)
    choices = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Failed", "Failed")
    )
    transaction_status = models.CharField(max_length=100, choices=choices, default="Pending")
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number} - {self.gh_card_number}"


class SuperAgentMTNBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"
    

class MTNTransaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bundle_number = models.BigIntegerField(null=False, blank=False)
    offer = models.CharField(max_length=250, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False, default=0.0)
    bundle_amount = models.FloatField()
    reference = models.CharField(max_length=20, null=False, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    choices = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Failed", "Failed")
    )
    transaction_status = models.CharField(max_length=100, choices=choices, default="Completed")
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.bundle_number} - {self.reference}"
    

class MTNBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)


    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class AgentMTNBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)


    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume/1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"
    

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reference = models.CharField(max_length=256, null=False, blank=False)
    amount = models.FloatField(null=True, blank=True)
    channels = (
        ("mtn", "mtn"),
        ("ishare", "ishare"),
        ("bigtime", "bigtime"),
        ("afa", "afa"),
        ("topup", "topup")
    )
    transaction_details = models.JSONField(null=True, blank=True)
    channel = models.CharField(max_length=250, null=True, blank=True, choices=channels)
    payment_description = models.CharField(max_length=500, null=True, blank=True)
    transaction_status = models.CharField(max_length=256, null=True, blank=True, default="Unfinished")
    transaction_date = models.CharField(max_length=250, null=True, blank=True)
    payment_details = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.reference}"


class TopUpRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reference = models.CharField(max_length=250, null=False, blank=False)
    amount = models.FloatField(blank=False, null=False)
    status = models.BooleanField(default=False, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    credited_at = models.DateTimeField(auto_now_add=True)


class Announcement(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message


class VodaBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)
    purchase_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume / 1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class AgentVodaBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)
    purchase_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume / 1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class SuperAgentVodaBundlePrice(models.Model):
    price = models.FloatField(null=False, blank=False)
    bundle_volume = models.FloatField(null=False, blank=False)
    purchase_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.bundle_volume >= 1000:
            return f"GHS{self.price} - {self.bundle_volume / 1000}GB"
        return f"GHS{self.price} - {self.bundle_volume}MB"


class VodafoneTransaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bundle_number = models.BigIntegerField(null=False, blank=False)
    offer = models.CharField(max_length=250, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False, default=0.0)
    bundle_amount = models.FloatField()
    reference = models.CharField(max_length=20, null=False, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    choices = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Processing", "Processing"),
        ("Failed", "Failed")
    )
    transaction_status = models.CharField(max_length=100, choices=choices, default="Pending")
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.bundle_number} - {self.reference}"


class WalletTransaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    choices = [
        ("Credit", "Credit"),
        ("Debit", "Debit")
    ]
    transaction_type = models.CharField(max_length=250, null=False, blank=False, choices=choices)
    transaction_amount = models.FloatField(null=False, blank=False)
    transaction_use = models.CharField(max_length=250, null=False, blank=False)
    new_balance = models.FloatField(null=False, blank=False)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.transaction_amount}"


