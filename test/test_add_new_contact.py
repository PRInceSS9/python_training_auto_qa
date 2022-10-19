# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                               bmonth="November", byear="1998"))
    app.contact.return_home_page()
    app.session.logout()

    
