# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_main_page()
    app.open_group_page()
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="test", header="group test", footer="test group"))
    app.session.logout()



