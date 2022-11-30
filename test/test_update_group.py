from model.group import Group
from random import randrange


def test_modify_group_name(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="upd_name", header="upd_header", footer="upd_footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="group test", footer="test group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New name header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="group test", footer="test group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New name footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

