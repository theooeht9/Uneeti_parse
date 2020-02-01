import re
import datefinder

# "graphic" interface of program
def front():
    global deco
    deco = "########"
    #Default KeyWord
    global keyWord 
    keyWord = ["tâche", "rendez-vous", "appel téléphonique"]
    print(deco)
    print("Your keywords: ",keyWord)
    print(deco)
    #
    
    #Enter or not new KeyWord
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
        
    #final KeyWord before parsing
    print(keyWord)
    
    #Enter file to parse
    global file 
    print(deco)
    file = input("Enter file to parse: ")
    
# parse
def parse():
    front()
    #open the file
    with open(file) as myfile:
        for line in myfile:
            # Search what is after 'CRM' 
            result = re.search('CRM(.*)', line)
            if any(ele in line for ele in keyWord):
                print(deco)
                #String of all after CRM
                strAftCrm = result.group(1)
                if any(ele in strAftCrm for ele in keyWord):
                    #To take off if for exemple string = 00/00/0000 à 00H00 will become 00/00/0000 00:00
                    t = strAftCrm.replace('à', '').replace('H', ':').replace('h', ':')
                    
                    #search if there is date in the string t
                    matches = datefinder.find_dates(t)
                    
                    #create list containing matching word between keyWord list and strAftCrm String
                    matchKeyWord_list=[]
                    for i in range(len(keyWord)):
                        if keyWord[i] in strAftCrm:
                            matchKeyWord_list.append(keyWord[i])
                    
                    #create list containing date from string t
                    date_list=[]
                    for date in matches:
                        date_list.append(date)
                    
                    #print corresponding keyword and date
                    for i in range(len(matchKeyWord_list)):
                        print (matchKeyWord_list[i], date_list[i])
                        
                    print(deco)
                    return
parse()