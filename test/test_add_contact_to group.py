from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Василий", middlename="Анатольевич", lastname="Кусков", bday="9",
                                   bmonth="November", byear="1998"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    all_contacts = db.get_contact_list()
    contact = random.choice(all_contacts)
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group

