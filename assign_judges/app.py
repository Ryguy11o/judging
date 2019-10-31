import csv
import operator
from random import randint

list_of_judges = "@Dave, @Michael, @Garrett Sullivan, @Manik, @Romy Morsy, @Jake, @amazon alexa, @Shane Kramer, @samanthafloyd, @Mohsin Ali, @Amal, @Colin Moran, @Hana, @thepbjain, @kelsie, @granddad, @Julia, @Nitya, @Kyle Z , @Anastasia, @Stan, @Ben, @Chanpreet Singh, @Annie Hinkle, @Alexandra Jung, @Danielle Coscio, @Vansh, @KADIJAH, @Hannah Lugent, @Rahul, @Bhavana, @Thomas Zhao, @Mary Cascio, @Juj, @claytonsulby, @Shawn, @Ryan, Tiffany, Daniel Shurtleff, Kunal, Michael Choi, Jared Cal"
judges = list_of_judges.split(',')

with open('./submissions.csv', errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total_tables = [];
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            #skipHeaders
            line_count += 1
        else:
            total_tables.append(row[2])
    tables = set(total_tables)
    table_numbers = len(tables)

    tables_array = []
    for x in range(table_numbers):
        tables_array.append(x + 1)

    tables_array *= 10

    judges_to_tables = {}
    number_per_judge = 8
    counter = 0

    for judge in judges:


        subset = tables_array[counter:counter+number_per_judge]

        counter += 4

        judges_to_tables[judge] = subset

    for key, value in judges_to_tables.items():
        print(f'Judge Name:{key} --- Tables to Judge: {value}')