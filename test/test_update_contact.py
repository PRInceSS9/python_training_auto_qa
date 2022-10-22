from model.contact import Contact


def test_modify_contact_firstname(app):
    app.open_main_page()
    app.contact.modify_first_contact(Contact(firstname="New name contact"))


def test_modify_contact_middlename(app):
    app.open_main_page()
    app.contact.modify_first_contact(Contact(middlename="New name contact"))


def test_modify_contact_lastname(app):
    app.open_main_page()
    app.contact.modify_first_contact(Contact(lastname="New name contact"))


def test_modify_contact_bday(app):
    app.open_main_page()
    app.contact.modify_first_contact(Contact(bday="18"))
