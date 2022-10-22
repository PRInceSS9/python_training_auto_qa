from model.group import Group


def test_modify_group_name(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.group.open_page()
    app.group.modify_first_group(Group(name="New name group"))
    app.session.logout()


def test_modify_group_header(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.group.open_page()
    app.group.modify_first_group(Group(header="New name header"))
    app.session.logout()


def test_modify_group_footer(app):
    app.open_main_page()
    app.session.login(username="admin", password="secret")
    app.group.open_page()
    app.group.modify_first_group(Group(footer="New name footer"))
    app.session.logout()
