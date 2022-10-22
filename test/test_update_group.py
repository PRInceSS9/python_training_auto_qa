from model.group import Group


def test_modify_group_name(app):
    app.open_main_page()
    app.group.open_page()
    app.group.modify_first_group(Group(name="New name group"))


def test_modify_group_header(app):
    app.open_main_page()
    app.group.open_page()
    app.group.modify_first_group(Group(header="New name header"))


def test_modify_group_footer(app):
    app.open_main_page()
    app.group.open_page()
    app.group.modify_first_group(Group(footer="New name footer"))

