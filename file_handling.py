# Yenesis Rabelo, login and new user creation code --------------------------------------------------------------------

import csv

def save(users):
    with open("users.csv", 'w') as file:
        csv_writer = csv.writer(file)
        for user in users:
            write_user = [user['name'], user['password'], user['balance']]
            for entry in user['record']:
                for i in entry['date']:
                    write_user.append(i)
                write_user.append(entry['amount'])
                write_user.append(entry['location'])
            csv_writer.writerow(write_user)

def load():
    users = []
    date = []
    entry = {}
    with open("users.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for i in csv_reader:
            if i != []:
                user = {'name': i[0], 'password': i[1], 'balance': float(i[2]), 'record': []}
                for j in i:
                    if i.index(j) not in range(0, 3):
                    
                        match i.index(j) % 5:
                            case 3:
                                date.append(int(j))
                            case 4:
                                date.append(int(j))
                            case 0:
                                date.append(int(j))
                            case 1:
                                entry['date'] = date
                                entry['amount'] = float(j)
                            case 2:
                                entry['location'] = j
                                user['record'].append(entry)
                                date = []
                                entry = {}
                users.append(user)                
    return users

# End of Yenesis' code ------------------------------------------------------------------------------------------------
