from djangovue.urls import *
from django.test import Client
from django.urls import reverse
import pytest

from listelement.models import Element, Type, Category
from store.models import Payment
from comment.models import Contact



def test_element_creation():
    element = Element(

        title='test1',
        url_clean='url_clean_asdadsad',
        description='descripcionprueba',
        price='20',
       
    )

    assert element.title == 'test1'
    assert element.url_clean == 'url_clean_asdadsad'
    assert element.description == 'descripcionprueba'
    assert element.price == '20'


def test_type_creation():
    type = Type(

        title='test2',
        url_clean='url_clean_asdadsad',


    )

    assert type.title == 'test2'
    assert type.url_clean == 'url_clean_asdadsad'


def test_category_creation():
    category = Category(

        title='test3',
        url_clean='url_clean_test3',
       

    )

    assert category.title == 'test3'
    assert category.url_clean == 'url_clean_test3'


def test_payment_creation():
    payment = Payment(

        created_at= '01/01/2023',
        uptated_at= '01/01/2023',
        payment_id= 'test4',
        payer_id= 'test4',
        price= 15
      

    )
        
    
    assert payment.created_at == '01/01/2023'
    assert payment.uptated_at == '01/01/2023'
    assert payment.payment_id == 'test4'
    assert payment.payer_id == 'test4'
    assert payment.price == 15

def test_contact_creation():
    contact = Contact(

        name='test5',
        surname='test5',
        email='test5@test5.com',
        phone='test5',
        

    )

    assert contact.name == 'test5'
    assert contact.surname == 'test5'
    assert contact.email == 'test5@test5.com'
    assert contact.phone == 'test5'


