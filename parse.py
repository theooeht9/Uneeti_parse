import re
import datefinder

def front():
    global deco
    deco = "########"
    global keyWord 
    keyWord = ["tâche", "rendez-vous", "appel téléphonique"]
    print(deco)
    print("Your keywords: ",keyWord)
    print(deco)
    yes_or_not = input("Would you enter other keyword ? Yes or Not: ")
    if yes_or_not == "Yes":
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
                    for match in matches:
                        date = match
                        # if i < 2:
                        #     print("DATE: ",date)
                        #     i+=1
                    for i in range(len(keyWord)):
                        if keyWord[i] in test:
                            print (keyWord[i], date) 
                    # if keyWord[0] in test:
                    #     print(keyWord[0],date)
                    # elif keyWord[1] in test:
                    #     print(keyWord[1],date)
                    # elif keyWord[2] in test:
                    #     print(keyWord[2],date)
                    # print(result.group(1))
                    print(deco)
                    return
parse()