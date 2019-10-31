import csv
import operator

def Average(lst): 
    return sum(lst) / len(lst) 

with open('./attendance.csv', errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    f=open("attendance.txt", "a+")

    attendance_count = {};
    date_count = {};
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            print(row[7] + " -- " + row[8] + " -- " + row[9]);
            attendance_count.setdefault(row[7], []).append(row[9])
            if(row[9] == 'absent'):
                date_count.setdefault(row[7], []).append(row[8]);
            line_count += 1

# print(attendance_count)
    use_me = {}
    for key, value in attendance_count.items():
        if(value.count('absent') > 3):
            f.write('Name: ' + key + ' -- present: ' + str(value.count('present')) + ' -- absent : ' + str(value.count('absent')) + "\r\n")
            f.write(str(date_count[key]) + "\r\n")