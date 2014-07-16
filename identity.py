import luhn
import random
import time
import csv

__author__ = "Nicholas Ezyk"
__copyright__ = "Copyright (c) 2014 Nicholas Ezyk"
__license__ = "Creative Commons BY-NC-SA 4.0"

male_first_names = ['James', 'John', 'Robert', 'Michael', 'William',
                    'David', 'Richard', 'Charles', 'Joseph', 'Thomas',
                    'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald',
                    'George', 'Kenneth', 'Steven', 'Edward', 'Brian',
                    'Ronald', 'Anthony', 'Kevin', 'Jason', 'Matthew',
                    'Gary', 'Timothy', 'Jose', 'Larry', 'Jeffrey',
                    'Frank', 'Scott', 'Eric', 'Stephen', 'Andrew',
                    'Raymond', 'Gregory', 'Joshua', 'Jerry', 'Dennis',
                    'Walter', 'Patrick', 'Peter', 'Harold', 'Douglas',
                    'Henry', 'Carl', 'Arthur', 'Ryan', 'Roger']
                    #http://names.mongabay.com/male_names.htm
                    #Accurate as of the 1990 Census

female_first_names = ['Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth',
                      'Jennifer', 'Maria', 'Susan', 'Margaret', 'Dorothy',
                      'Lisa', 'Nancy', 'Karen', 'Betty', 'Helen',
                      'Sandra', 'Donna', 'Carol', 'Ruth', 'Sharon',
                      'Michelle', 'Laura', 'Sarah', 'Kimberly', 'Deborah',
                      'Jessica', 'Shirley', 'Cynthia', 'Angela', 'Melissa',
                      'Brenda', 'Amy', 'Anna', 'Rebecca', 'Virginia',
                      'Kathleen', 'Pamela', 'Martha', 'Debra', 'Amanda',
                      'Stephanie', 'Carolyn', 'Christine', 'Marie', 'Janet',
                      'Catherine', 'Frances', 'Ann', 'Joyce', 'Diane']
                     #http://names.mongabay.com/female_names.htm
                     #Accurate as of the 1990 Census

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
              'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson',
              'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez',
              'Moore', 'Martin', 'Jackson', 'Thompson', 'White',
              'Lopez', 'Lee', 'Gonzalez', 'Harris', 'Clark',
              'Lewis', 'Robinson', 'Walker', 'Perez', 'Hall',
              'Young', 'Allen', 'Sanchez', 'Wright', 'King',
              'Scott', 'Green', 'Baker', 'Adams', 'Nelson',
              'Hill', 'Ramirez', 'Campbell', 'Mitchell', 'Roberts',
              'Carter', 'Phillips', 'Evans', 'Turner', 'Torres']
             #http://names.mongabay.com/data/1000.html
             #Accurate as of the 1990 Census

additions = ['First','Middle','Last','CCprovider','CCnumber']

def writeCSV(data):
    with open('identities.csv', 'wb') as csvfile:
        c = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for s in data:
            c.writerow(s)

        c.writerow(['Steven', 'Quartz', 'Universe', 'VISA', '4543103432003224'])


def people(num):
    mm = str(len(male_first_names))
    ff = str(len(female_first_names))
    ll = str(len(last_names))
    print("Males: " + mm)
    print("Females: " + ff)
    print("Surnames: " + ll)
    time.sleep(1)
    n = str(num)
    p = str((len(male_first_names) + len(female_first_names)) * len(last_names))
    
    print("Please note that this tool is for educational purposes only and the creator of this script would like to note that credit card verification is far more complex than the Luhn algorithm alone, making any attempts at fraud rather futile. Please don't try to break the law using this script.")
    time.sleep(2)
    print("Generating " + n + " identities from " + p + " combinations 3 seconds from now...")
    time.sleep(3)
    for i in xrange(0, num):
        a = random.randrange(2)
        g = ''
        f = ''
        if (a == 0):
            g = 'M'
            f = male_first_names[random.randrange(len(male_first_names))]
        else:
            g = 'F'
            f = female_first_names[random.randrange(len(female_first_names))]
        l = last_names[random.randrange(len(last_names))]
        per = Person(g, f, None, l)
    print(n + " identities generated. Thank you for using this script!")

    writeCSV(additions)

class Person():
    def __init__(self, gender, first_name, middle_name, last_name):
        if (gender is None or not (gender == 'M' or gender == 'F')):
            a = random.randrange(2)
            if (a == 0):
                self.gender = 'M'
            else:
                self.gender = 'F'
        if (first_name is None):
            if (self.gender == 'M'):
                self.first_name = male_first_names[random.randrange(len(male_first_names))]
            else:
                self.first_name = female_first_names[random.randrange(len(female_first_names))]
        else:
            self.first_name = first_name
        if (middle_name is None):
            self.middle_name = ''
        else:
            self.middle_name = middle_name
        if (last_name is None):
            self.last_name = last_names[random.randrange(len(last_names))]
        else:
            self.last_name = last_name
        rand = random.randrange(4)
        if (rand == 0):
            self.card = luhn.AmexCreditCard()
        elif (rand == 1):
            self.card = luhn.VisaCreditCard()
        elif (rand == 2):
            self.card = luhn.MasterCardCreditCard()
        else:
            self.card = luhn.DiscoverCreditCard()
        if (self.middle_name is None):
            print(self.last_name + ", " + self.first_name + " " + "initialized, with " + self.card.short + " number " + self.card.CCnumber)
            additions.append([self.first_name, None, self.last_name, self.card.short, self.card.CCnumber])
        else:
            print(self.last_name + ", " + self.first_name + " " + self.middle_name + " " + "initialized, with " + self.card.short + " number " + self.card.CCnumber)
            additions.append([self.first_name, self.middle_name, self.last_name, self.card.short, self.card.CCnumber])
            



