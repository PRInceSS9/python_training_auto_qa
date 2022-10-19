

def test_first_group(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.group.open_page()
    app.group.delete_first()
    app.group.return_to_groups_page()
    app.session.logout()