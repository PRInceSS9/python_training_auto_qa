import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host,
        self.name = name,
        self.user = user,
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname,"
                           " address, home, mobile, work, phone2, email, email2, email3, bday, bmonth, byear from addressbook "
                           "where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, address, home, mobile, work, phone2, email, email2, email3, bday, bmonth, byear) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    address=address, homephone=home, mobilephone=mobile, workphone=work, secondaryphone=phone2,
                                    email=email, email2=email2, email3=email3, bday=bday, bmonth=bmonth, byear=byear))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()