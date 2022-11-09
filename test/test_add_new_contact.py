# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_int_string(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    day = random.randint(1, 31)
    return str(day)


def random_month():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"])


def random_year():
    year = random.randint(1950, 2022)
    return str(year)


testdata = [
            Contact(firstname=random_letters("firstname", 10),
                    middlename=random_letters("middlename", 10),
                    lastname=random_letters("lastname", 10),
                    bday=random_day(), bmonth=random_month(), byear=random_year())
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

