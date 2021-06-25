import random
import string
import json


lis_name = list()
for i in range(10):
    lis_name.append(random.choice(string.ascii_letters))
name = ''.join(lis_name)
print(name)

lis_pass = list()
for i in range(6):
    test = random.random()
    test = round(test, 1) * 10
    test = int(test)
    test = str(test)
    lis_pass.append(test)
    lis_pass.append(random.choice(string.ascii_letters))
password = '.'.join(lis_pass)
print(password)


def load_log():
    a_dict = ({"name": name, "pass": password},)

    with open('mails.json') as f:
        data = json.load(f)
    data = list(data)
    data += list(a_dict)

    with open('mails.json', 'w') as f:
        json.dump(data, f)


# convert into JSON:
# y = json.dumps(x)

with open('mails.txt', 'r') as oldMails:
    content = oldMails.readline()


def del_last_line():
    with open('mails.txt', 'r+') as f:  # open in read / write mode
        f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size



