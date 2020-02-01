import re
import datefinder

# "graphic" interface of program
def front():
    global deco
    deco = "########"
    global keyWord 
    keyWord = ["tâche", "rendez-vous", "appel téléphonique"]
    print(deco)
    print("Your keywords: ",keyWord)
    print(deco)
    yes_or_not = input("Would you enter other keyword ? Yes or Not: ")
    if yes_or_not == "Yes" or yes_or_not == "yes":
        j = 0
        print(deco)
        number_new = int(input("Enter the number to new keyword: "))
        while j < number_new:
            item = input("Add new keyword to the List: ")
            keyWord.append(item)
            j +=1
        print(deco)
    else:
        print(deco)
    print(keyWord)
    global file 
    print(deco)
    file = input("Enter file to parse: ")
    
# parse
def parse():
    i = 1
    front()
    with open(file) as test:
        for line in test:
            result = re.search('CRM(.*)', line)
            if any(ele in line for ele in keyWord):
                print(deco)
                test = result.group(1)
                if any(ele in test for ele in keyWord):
                    t = test.replace('à', '').replace('H', ':').replace('h', ':')
                    
                    matches = datefinder.find_dates(t)
                    listMatchKeyWord=[]
                    for i in range(len(keyWord)):
                        if keyWord[i] in test:
                            listMatchKeyWord.append(keyWord[i])
                    list=[]
                    for date in matches:
                        list.append(date)
                    for i in range(len(listMatchKeyWord)):
                        print (listMatchKeyWord[i], list[i])
                    print(deco)
                    return
parse()