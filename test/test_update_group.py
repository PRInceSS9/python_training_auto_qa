from model.group import Group


def test_update_first_group(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.group.open_page()
    app.group.update_first(Group(name="update name", header="update header", footer="update footer"))
    app.group.return_to_groups_page()
    app.session.logout()