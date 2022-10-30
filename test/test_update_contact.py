from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                                   bmonth="November", byear="1998"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname contact")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_contact_middlename(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
#                                    bmonth="November", byear="1998"))
#     app.contact.modify_first_contact(Contact(middlename="New middlename contact"))
#
#
# def test_modify_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
#                                    bmonth="November", byear="1998"))
#     app.contact.modify_first_contact(Contact(lastname="New lastname contact"))
#
#
# def test_modify_contact_bday(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
#                                    bmonth="November", byear="1998"))
#     app.contact.modify_first_contact(Contact(bday="18"))
