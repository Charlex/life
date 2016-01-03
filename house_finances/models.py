from django.db import models
from django.utils.text import slugify
from django.template.loader import render_to_string
from django.conf import settings


class LifeBase(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_last_modified = models.DateTimeField(auto_now=True, editable=False)

    def dollar_amount(self, amount):
        if amount is None:
            return "$0"
        return "$%s" % str(amount)

    class Meta:
        abstract = True


class Roomie(LifeBase):
    """
    Gary, Brian & Charley
    """
    name = models.CharField(max_length=500)
    email_address = models.EmailField(max_length=500)

    @property
    def debts(self):
        return Debt.objects.filter(debtor=self)
    
    @property
    def total_owed(self):
        return sum(debt.amount_still_owed for debt in self.debts)

    @property
    def total_paid(self):
        return sum(debt.payment_sum for debt in self.debts)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Item(LifeBase):
    """
    A record of debt
    """
    name = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=500,decimal_places=2)
    date_bought = models.DateField(editable=True)

    class Meta:
        ordering = ('-date_bought', 'name')

    @property
    def debts(self):
        return Debt.objects.filter(item=self)

    @property
    def payment_sum(self):
        return sum([debt.amount for debt in self.debts])

    @property
    def amount_still_owed(self):
        return sum([debt.amount_still_owed for debt in self.debts])

    @property
    def paid_for(self):
        return self.amount_still_owed == 0

    @property
    def creditors(self):
        return [debt.creditor for debt in self.debts]

    @property
    def debtors(self):
        return [debt.debtor for debt in self.debts]


    def __unicode__(self):
        return self.name


class Debt(LifeBase):
    """
    A record of debt
    """
    item = models.ForeignKey(Item)
    creditor = models.ForeignKey(Roomie, related_name="+", default=1)
    debtor = models.ForeignKey(Roomie, related_name="+")
    amount = models.DecimalField(max_digits=500,decimal_places=2)
    date_began = models.DateField(editable=True)
    date_due = models.DateField(blank=True,null=True)

    class Meta:
        ordering = ('-date_began', 'item')

    @property
    def amount_still_owed(self):
        running_amount = self.amount
        for payment in self.payments:
            running_amount = running_amount - payment.amount
        return running_amount

    @property
    def payments(self):
        return Payment.objects.filter(debt=self)

    @property
    def payment_count(self):
        return len(self.payments)

    @property
    def payment_sum(self):
        return sum(payment.amount for payment in self.payments)

    @property
    def paid_percent(self):
        return int((self.payment_sum / self.amount) * 100)

    @property
    def paid_in_full(self):
        return self.amount_still_owed == 0


    def __unicode__(self):
        return "%s owes $%i to %s for %s" % (self.debtor.name, self.amount_still_owed, self.creditor.name, self.item.name)


class Payment(LifeBase):
    """
    A record of debt
    """
    debt = models.ForeignKey(Debt)
    amount = models.DecimalField(max_digits=500,decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s paid $%i to %s for %s" % (
            self.debt.debtor,
            self.amount,
            self.debt.creditor,
            self.debt.item.name
        )
