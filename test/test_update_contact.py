from model.contact import Contact


def test_update_contact(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.open_main_page()
    app.contact.update_first(Contact(firstname="Update name", middlename="update middlename", lastname="update lastname", bday="10",
                               bmonth="December", byear="1999"))
    app.contact.return_home_page()
    app.session.logout()