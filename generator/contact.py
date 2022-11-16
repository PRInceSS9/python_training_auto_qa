from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_int_string(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    day = random.randint(1, 31)
    return str(day)


def random_month():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"])


def random_year():
    year = random.randint(1950, 2022)
    return str(year)

testdata = [
            Contact(firstname=random_letters("firstname", 10),
                    middlename=random_letters("middlename", 10),
                    lastname=random_letters("lastname", 10),
                    bday=random_day(), bmonth=random_month(), byear=random_year(),
                    homephone=random_int_string(11), mobilephone=random_int_string(11),
                    workphone=random_int_string(11), secondaryphone=random_int_string(11))
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))