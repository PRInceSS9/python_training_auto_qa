from model.contact import Contact


def test_update_contact(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.open_main_page()
    app.contact.update_first(Contact(firstname="Update name", middlename="update middlename", lastname="update lastname", bday="10",
                               bmonth="December", byear="1999"))
    app.contact.return_home_page()
    app.session.logout()


def test_modify_contact_firstname(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.open_main_page()
    app.contact.modify_first_contact(Contact(firstname="New name contact"))
    app.session.logout()


def test_modify_contact_middlename(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.open_main_page()
    app.contact.modify_first_contact(Contact(middlename="New name contact"))
    app.session.logout()


def test_modify_contact_lastname(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.open_main_page()
    app.contact.modify_first_contact(Contact(lastname="New name contact"))
    app.session.logout()


def test_modify_contact_bday(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.open_main_page()
    app.contact.modify_first_contact(Contact(bday="18"))
    app.session.logout()