import csv
import operator

def Average(lst): 
    return sum(lst) / len(lst) 

def get_average(item):
    return item[1]['average']

def get_table_num(item):
    return item[0]

with open('./testing.csv', errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    team_num_to_score = {};
    team_table_to_name = {};
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #row[3] is total score
            total = int(row[3])

            if total < 51 and total > 4:

                team_num_to_score.setdefault(int(row[2]), []).append(total)

                team_table_to_name.setdefault(int(row[2]), []).append(row[1])
                #print(f'\t Team Name: {row[1]} Table Number: {row[2]}, Total: {total}')
            line_count += 1

    print("########-- Team Table Number to Judges Submitted Names --#########")
    use_me = {}
    for key, value in team_num_to_score.items():
        use_me[key] = { "average": Average(value), "length": len(value) };
        #print(f' Team Number: {key}, Average Score: {Average(value)}, Number of Hits: {len(value)}')

    sorted_x = sorted(use_me.items(), key=get_average, reverse=True)

    sorted_table_numbers = sorted(team_table_to_name.items(), key=get_table_num, reverse=True)

    for key,value in sorted_table_numbers:
        print(f' Table Number: {key}, Team Name(s): {value} )')
    print()
    print()
    print("########-- Sorted Scores by highest average score --#########")

    for key, value in sorted_x:
        print(f' Table Number: {key}, Average Score: {value["average"]}, Number of Hits: {value["length"]}')





