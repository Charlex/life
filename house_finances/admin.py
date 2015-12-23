from django.contrib import admin
from .models import Roomie, Debt, Payment, Item
from nested_inline.admin import NestedStackedInline, NestedModelAdmin



class PaymentInline(NestedStackedInline):
    model = Payment
    extra = 0

class DebtInline(NestedStackedInline):
    model = Debt
    extra = 0
    inlines = [PaymentInline]


@admin.register(Roomie)
class RoomieAdmin(NestedModelAdmin):
    pass


# @admin.register(Payment)
# class PaymentAdmin(NestedModelAdmin):
#     list_display = (
#         '__unicode__',
#         'date_created',
#     )



# @admin.register(Debt)
# class DebtAdmin(NestedModelAdmin):
#     inlines = [
#         PaymentInline,
#     ]


@admin.register(Item)
class ItemAdmin(NestedModelAdmin):
    inlines = [
        DebtInline,
    ]