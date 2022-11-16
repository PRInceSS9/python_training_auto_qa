from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                                   bmonth="November", byear="1998"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New firstname contact.py")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_contact_middlename(app):
#     if app.contact.py.count() == 0:
#         app.contact.py.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
#                                    bmonth="November", byear="1998"))
#     app.contact.py.modify_first_contact(Contact(middlename="New middlename contact.py"))
#
#
# def test_modify_contact_lastname(app):
#     if app.contact.py.count() == 0:
#         app.contact.py.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
#                                    bmonth="November", byear="1998"))
#     app.contact.py.modify_first_contact(Contact(lastname="New lastname contact.py"))
#
#
# def test_modify_contact_bday(app):
#     if app.contact.py.count() == 0:
#         app.contact.py.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
#                                    bmonth="November", byear="1998"))
#     app.contact.py.modify_first_contact(Contact(bday="18"))
