from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                                   bmonth="November", byear="1998"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Upd_firstname")
    contact.id = int(old_contacts[index].id)
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




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
