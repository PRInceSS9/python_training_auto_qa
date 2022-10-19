# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.open_main_page()
    app.group.open_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test", header="group test", footer="test group"))
    app.group.return_to_groups_page()
    app.session.logout()



