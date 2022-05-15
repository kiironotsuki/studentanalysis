"""
@author Tommy Chen
date May 13, 2022
"""
# import modules
import csv
import operator

# Name of the student data csv file
filePath = 'Studentdata.csv'


def average():
    print('Would you like to display the average GPA for students or programs?\n'
          'Enter 1 to display the average GPA for all students.\n'
          'Enter 2 to display the average GPA by each program.')
    userInput = input('Please enter 1 or 2: ')
    if userInput == '1':
        avgStudents()
    elif userInput == '2':
        avgPrograms()
    else:
        print('You have made an invalid choice.')


def avgStudents():
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        lst = []
        for row in datareader:
            lst.append(float(row[3]))
        print('---------------------------------')
        print('The average student GPA: ' + str(round(sum(lst) / len(lst), 2)))
        print('---------------------------------')


def avgPrograms():
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        mscm = []
        msit = []
        bsit = []
        for row in datareader:
            # Replaced if/else statement with a switch case statement
            match row[4].lower():
                case 'mscm':
                    mscm.append(float(row[3]))
                case 'msit':
                    msit.append(float(row[3]))
                case 'bsit':
                    bsit.append(float(row[3]))
        print('---------------------------------')
        print('Below is the average GPA for the following programs')
        print('MSCM: ' + str(round(sum(mscm) / len(mscm), 2)))
        print('MSIT: ' + str(round(sum(msit) / len(msit), 2)))
        print('BSIT: ' + str(round(sum(bsit) / len(bsit), 2)))
        print('---------------------------------')


def gradeDistrubtion():
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        for row in datareader:
            match float(row[3]):
                case num if 90 <= num:
                    a += 1
                case num if 80 <= num <= 90:
                    b += 1
                case num if 70 <= num <= 80:
                    c += 1
                case num if 60 <= num <= 70:
                    d += 1
                case num if num <= 60:
                    e += 1
        total = sum([a, b, c, d, e])
        print('Grade Distribution')
        print('----------------------------------')
        print('Grade   | Count | Percentage')
        print('A to A- |   ' + str(a) + '   |   ' + str(round(a/total, 2)))
        print('B to B- |   ' + str(b) + '   |   ' + str(round(b/total, 2)))
        print('C to D- |   ' + str(c) + '   |   ' + str(round(c/total, 2)))
        print('D to D- |   ' + str(d) + '   |   ' + str(round(d/total, 2)))
        print('E       |   ' + str(e) + '   |   ' + str(round(e/total, 2)))
        print('----------------------------------')
        print('Total   |  ' + str(total) + '   |')
        print('----------------------------------')


def grade():
    print('Would you like to display the lowest or highest grade?\n'
          'Enter 1 to display highest grade.\n'
          'Enter 2 to display lowest grade.')
    userInput = input('Please enter 1 or 2: ')
    if userInput == '1':
        hGrade()
    elif userInput == '2':
        lGrade()
    else:
        print('You have made an invalid choice.')


def hGrade():
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        lst = []
        for row in datareader:
            lst.append(float(row[3]))
        print('----------------------------')
        print('The highest grade is ' + str(max(lst)))
        print('----------------------------')


def lGrade():
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        lst = []
        for row in datareader:
            lst.append(float(row[3]))
        print('----------------------------')
        print('The lowest grade is ' + str(min(lst)))
        print('----------------------------')


def programRecord():
    print('Which program do you want the count for?\n'
          'Enter 1 to display the count for MSIT students.\n'
          'Enter 2 to display the count for MSCM students.\n'
          'Enter 3 to display the count for BSIT students.')
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        msitCount = 0
        mscmCount = 0
        bsitCount = 0
        for row in datareader:
            match row[4].lower():
                case 'msit':
                    msitCount += 1
                case 'mscm':
                    mscmCount += 1
                case 'bsit':
                    bsitCount += 1
        userInput = input('Please enter 1, 2, or 3: ')
        match userInput:
            case 1:
                print('---------------------------------')
                print('The MSIT program has a total of ' + str(msitCount) + ' students.')
                print('---------------------------------')
            case 2:
                print('---------------------------------')
                print('The MSCM program has a total of ' + str(mscmCount) + ' students.')
                print('---------------------------------')
            case 3:
                print('---------------------------------')
                print('The BSIT program has a total of ' + str(bsitCount) + ' students.')
                print('---------------------------------')
            case _:
                print('You have made an invalid choice.')


def invalidRecord():
    print('Would you like to display the invalid records or create a new file?\n'
          'Enter 1 to display the invalid records.\n'
          'Enter 2 to create a new txt file.')
    userInput = input('Please enter 1 or 2: ')
    match userInput:
        case '1':
            displayInvalid()
        case '2':
            createInvalid()
        case _:
            print('You have made an invalid choice.')


def displayInvalid():
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        lst = []
        unique = []
        count = 0
        for row in datareader:
            lst.append(row)
            for rows in lst:
                for element in rows:
                    if element == '':
                        if rows not in unique:
                            unique.append(rows)
                            count += 1

        print('-----------------------------------------')
        print('There are ' + str(count) + ' count(s) of invalid record(s).')
        print('The records are displayed below.')
        for data in unique:
            print(data)
        print('-----------------------------------------')


def createInvalid():
    with open(filePath, 'r') as csv_file:
        datareader = csv.reader(csv_file, delimiter=',')
        lst = []
        unique = []
        for row in datareader:
            lst.append(row)
            for rows in lst:
                for element in rows:
                    if element == '':
                        if rows not in unique:
                            unique.append(rows)
    with open('BADRECORDS.TXT', 'w') as textfile:
        for row in unique:
            textfile.write(str(row) + '\n')
    print('---------------------------------')
    print('BADRECORDS.TXT file has been created!')
    print('---------------------------------')


def sortedRecord():
    print('Would you like to display the sorted records or create a new sorted file?\n'
          'Enter 1 to display the sorted records by ascending Student ID.\n'
          'Enter 2 to create a new sorted txt file.')
    userInput = input('Please enter 1 or 2: ')
    match userInput:
        case '1':
            displaySorted()
        case '2':
            createSorted()
        case _:
            print('You have made an invalid choice.')


def displaySorted():
    # load csv files
    data = csv.reader(open(filePath), delimiter=',')

    # sort data on by student id
    data = sorted(data, key=operator.itemgetter(0))

    print()
    print('After sorting:')

    # correct the corrupted data
    data[-1][0] = '1001'
    data = sorted(data, key=operator.itemgetter(0))
    print(data)


def createSorted():
    # load csv files
    data = csv.reader(open(filePath), delimiter=',')

    # sort data on by student id
    data = sorted(data, key=operator.itemgetter(0))

    print('---------------------------------')
    print('After sorting:')

    # correct the corrupted data
    data[-1][0] = '1001'
    data = sorted(data, key=operator.itemgetter(0))

    with open('SORTED.TXT', 'w') as textfile:
        for row in data:
            textfile.write(str(row) + '\n')

    print('SORTED.TXT file has been created!')
    print('---------------------------------')


# Start of the program loop
finalInput = input('Would you like to do?\n'
                  'Enter 1 to view the average GPA.\n'
                  'Enter 2 to view the grade distribution.\n'
                  'Enter 3 to view the grade record.\n'
                  'Enter 4 to view the program record.\n'
                  'Enter 5 to view the invalid records.\n'
                  'Enter 6 to view the sorted records.\n'
                  'Enter 7 to display options again.\n'
                  'Enter 8 to exit the program.\n'
                  'Please make a valid selection: ')

while finalInput != "8":
    match finalInput:
        case '1':
            try:
                average()
            except FileNotFoundError as e:
                print('Error Message: ' + str(e))
        case '2':
            try:
                gradeDistrubtion()
            except FileNotFoundError as e:
                print('Error Message: ' + str(e))
        case '3':
            try:
                grade()
            except FileNotFoundError as e:
                print('Error Message: ' + str(e))
        case '4':
            try:
                programRecord()
            except FileNotFoundError as e:
                print('Error Message: ' + str(e))
        case '5':
            try:
                invalidRecord()
            except FileNotFoundError as e:
                print('Error Message: ' + str(e))
        case '6':
            try:
                sortedRecord()
            except FileNotFoundError as e:
                print('Error Message: ' + str(e))
        case '7':
            print('Enter 1 to view the average GPA.\n'
                  'Enter 2 to view the grade distribution.\n'
                  'Enter 3 to view the grade record.\n'
                  'Enter 4 to view the program record.\n'
                  'Enter 5 to view the invalid records.\n'
                  'Enter 6 to view the sorted records.\n'
                  'Enter 7 to display the options again.\n'
                  'Enter 8 to exit the program.\n')
        case '8':
            break
        case _:
            print('You have made an invalid choice.')
    finalInput = input('Please make a valid selection: ')

# exit message
print('---------------------------------\n'
      'The program has successfully exited.\n'
      '---------------------------------')