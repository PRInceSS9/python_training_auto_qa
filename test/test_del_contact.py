

def test_delete_contact(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()

    