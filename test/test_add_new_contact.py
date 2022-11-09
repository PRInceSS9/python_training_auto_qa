# -*- coding: utf-8 -*-
from model.contact import Contact


testdata = [

]


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                               bmonth="November", byear="1998")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

