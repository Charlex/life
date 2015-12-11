from django.contrib import admin
from .models import Roomie, Debt, Payment, Item


@admin.register(Roomie)
class RoomieAdmin(admin.ModelAdmin):
    pass


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
	pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	pass

