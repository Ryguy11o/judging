import csv
import operator

with open('./submissions.csv', errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    # challenge_tables = {
    #     "HackPSU Overall - Tech": [],
    #     "HackPSU Overall - Design": [],
    #     "HackPSU - IoT Workshop Challenge": [],
    #     "Nittany AI Alliance - AI Challenge": [],
    #     "GM - Autonomous RC Car Challenge": [],
    #     "Capital One - Best Financial Hack": [],
    #     "KCF - Hack the Waiting Room Challenge": [],
    #     "Vanguard - Reducing Student Debt": [],
    #     "JPMC - Best Social Good Hack": [],
    #     "Booz Allen Hamilton - Best Machine Learning Hack": [],
    #     "Accuweather Challenge": [],
    #     "Best use of Authorize.net": [],
    #     "Best Social Good Hack from Fidelity Weekly Challenge": [],
    #     "Snap Kit Weekly Challenge": [],
    #     "Best use of Clarifai’s API Weekly Challenge": [],
    #     "Best use of HERE.com": [],
    #     "Best Chat Bot using Botkit & Cisco Webex Teams": [],
    #     "Best IoT Hack Using a Qualcomm Device": [],
    #     "Best Domain Name from Domain.com": [],
    #     "Best use of Google Cloud Platform": [],
    #     "Best use of Algolia": [],
    #     "AWS Challenge": []
    # }

    challenge_tables = {
        "HackPSU Overall - Tech": [],
        "Geico - AI Challenge": [],
        "Lion LaunchPad SLO - Inventory Innovation": [],
        "EY Tech Challenge": [],
        "HackPSU - IoT Workshop Challenge": [],
        "Best Use of Snapkit (MLH)": [],
        "Best IoT Hack using a Qualcomm Device (MLH)": [],
        "Best Use of Google Cloud Platform (MLH)": [],
        "Best Domain Registered with Domain.com (MLH)": []
    }

    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            #skipHeaders
            line_count += 1
        else:
            #row[3] is total score
            challenge = row[0]
            if challenge in challenge_tables:
                challenge_tables[challenge].append(row[2])

    for key, value in challenge_tables.items():
        print(f'Challenge: {key}  --- Participating Tables: {value}')


