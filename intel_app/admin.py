from django import forms
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.db import transaction

from . import models
from import_export.admin import ExportActionMixin

from .models import CustomUser, WalletTransaction


class CustomUserAdminForm(forms.ModelForm):
    add_balance = forms.FloatField(required=False, label="Add Balance", help_text="Add to user's wallet balance.")

    class Meta:
        model = CustomUser
        fields = '__all__'


# Register your models here.
class CustomUserAdmin(ExportActionMixin, UserAdmin):
    form = CustomUserAdminForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'username', 'email', 'wallet', 'phone', 'status']
    search_fields = ['username']

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'add_balance', 'status', 'wallet'
                )
            }
        )
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'username', 'password1', 'password2', 'wallet')
        }),)

    def save_model(self, request, obj, form, change):
        add_balance = form.cleaned_data.get('add_balance', 0)
        if add_balance and add_balance > 0:
            try:
                with transaction.atomic():
                    # Lock the user record for updating the balance
                    obj = CustomUser.objects.select_for_update().get(id=obj.id)

                    # Update the user's wallet balance
                    old_balance = obj.wallet
                    new_balance = old_balance + add_balance
                    obj.wallet = new_balance
                    obj.save()

                    # Create a WalletTransaction record
                    WalletTransaction.objects.create(
                        user=obj,
                        transaction_type="Credit",
                        transaction_amount=add_balance,
                        transaction_use="Admin Wallet Addition",
                        new_balance=new_balance,
                    )

                    # Send a success message
                    messages.success(request, f"Successfully added GHS {add_balance} to {obj.username}'s wallet.")
                    message = f"GHS{add_balance} has been added to your account"
                    # send_sms_task.delay(obj.phone, message)
            except Exception as e:
                messages.error(request, f"Failed to add balance: {str(e)}")

        super().save_model(request, obj, form, change)



class IShareBundleTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'bundle_number']


class MTNTransactionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['user', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'bundle_number']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'reference', 'transaction_date', 'amount']


class TopUpRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'reference', 'amount', 'date', 'status']


class AfaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'gh_card_number', 'name', 'occupation', 'occupation', 'date_of_birth', 'location']


class VodafoneTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'bundle_number']


class WalletTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_type', 'transaction_amount', 'transaction_use', 'new_balance', 'transaction_date']
    list_filter = ['user', 'transaction_type', 'transaction_use']
    search_fields = ['user__username']


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.IShareBundleTransaction, IShareBundleTransactionAdmin)
admin.site.register(models.MTNTransaction, MTNTransactionAdmin)
admin.site.register(models.IshareBundlePrice)
admin.site.register(models.MTNBundlePrice)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.AdminInfo)
admin.site.register(models.TopUpRequest, TopUpRequestAdmin)
admin.site.register(models.AgentIshareBundlePrice)
admin.site.register(models.AgentMTNBundlePrice)
admin.site.register(models.SuperAgentBigTimeBundlePrice)
admin.site.register(models.SuperAgentMTNBundlePrice)
admin.site.register(models.SuperAgentIshareBundlePrice)
admin.site.register(models.BigTimeTransaction)
admin.site.register(models.BigTimeBundlePrice)
admin.site.register(models.AgentBigTimeBundlePrice)
admin.site.register(models.AFARegistration, AfaAdmin)
admin.site.register(models.Announcement)
admin.site.register(models.AgentVodaBundlePrice)
admin.site.register(models.SuperAgentVodaBundlePrice)
admin.site.register(models.VodaBundlePrice)
admin.site.register(models.VodafoneTransaction, VodafoneTransactionAdmin)
admin.site.register(models.WalletTransaction, WalletTransactionAdmin)




