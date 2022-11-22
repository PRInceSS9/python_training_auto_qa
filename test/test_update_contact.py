from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                                   bmonth="November", byear="1998"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
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
