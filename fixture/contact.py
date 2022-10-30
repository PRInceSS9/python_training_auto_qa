from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:


    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_text_value("firstname", contact.firstname)
        self.change_field_text_value("middlename", contact.middlename)
        self.change_field_text_value("lastname", contact.lastname)
        self.change_field_select_value("bday", contact.bday)
        self.change_field_select_value("bmonth", contact.bmonth)
        self.change_field_text_value("byear", contact.byear)

    def change_field_select_value(self, field_name, var):
        wd = self.app.wd
        if var is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(var)

    def change_field_text_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_main_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            firstname = element.find_element_by_xpath("td[3]").text
            lastname = element.find_element_by_xpath("td[2]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts