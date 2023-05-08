from django.db import models
from django.contrib.auth.models import User
from listelement.models import Element

# Create your models here.

class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uptated_at = models.DateTimeField(auto_now=True)
    payment_id = models.CharField(max_length=200)
    payer_id = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=6.10) # 12345678.10
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)

    @classmethod
    def create(cls, payment_id, payer_id, price, user_id, element_id):
        #super(Payment,self).__init__()

        payment = cls(
            payment_id=payment_id, 
            payer_id=payer_id,
            price=price,
            element_id=element_id,
            user_id=user_id
        )

        return payment

        """self.payment_id = payment_id
        self.payer_id = payer_id
        self.price = price
        self.user = user_id
        self.element = element_id"""

    def __str__(self):
        return self.price