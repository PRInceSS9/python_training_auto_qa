from selenium.webdriver.support.ui import Select

class ContactHelper:


    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.fill_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

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
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_first(self, contact):
        wd = self.app.wd
        self.fill_form(contact)
        wd.find_element_by_name("submit").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_home_page()



    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()