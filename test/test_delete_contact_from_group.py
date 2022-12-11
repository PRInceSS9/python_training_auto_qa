from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                                   bmonth="November", byear="1998"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    contact = random.choice(app.contact.get_id_from_group_view_page(group.name))
    app.contact.del_contact_from_group(contact.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact not in contacts_in_group
