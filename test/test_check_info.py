import re
from model.contact import Contact


def test_properties_on_home_page(app, db):
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(db_contacts) == len(ui_contacts)
    for index in range(len(db_contacts)):
        assert ui_contacts[index].firstname == db_contacts[index].firstname
        assert ui_contacts[index].lastname == db_contacts[index].lastname
        assert ui_contacts[index].address == db_contacts[index].address
        assert ui_contacts[index].all_emails_from_home_page == merge_emails_like_on_home_page(db_contacts[index])
        assert ui_contacts[index].all_phones_from_home_page == merge_phones_like_on_home_page(db_contacts[index])


# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                          map(lambda x: clear(x),
                                              filter(lambda x: x is not None,
                                                     [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))