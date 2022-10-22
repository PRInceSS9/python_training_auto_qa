from model.group import Group


def test_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    app.group.delete_first()

