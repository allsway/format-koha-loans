#!/usr/bin/python
import sys
import csv
import datetime

# turns user names into user ID
def get_user_id(row):
    first_init = ''
    if len(row[1]) > 0:
        first_init = row[1].strip(' ')[0].lower()
    second = row[0].strip()
    return first_init + second

# returns current date in correct format for offline circ file
def get_date():
    day = datetime.datetime.today()
    return day.strftime('%Y%m%d%H%m')

# read file and output offline circ file
def parse_row(row):
    # 201701231123
    transaction_date = get_date()
    transaction = 'L'
    user_id = get_user_id(row)
    barcode = row[5]
    spaces = '                                                                       '
    print (transaction_date + transaction + barcode + spaces + user_id)

# parses loans csv file
def read_loans(loans):
    f  = open(loans,'rt')
    try:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[0] != 'missing':
                parse_row(row)
    finally:
        f.close()

# takes in csv export of Koha user loans
loans = sys.argv[1]
read_loans(loans)
