#################
#agendas:->
#appending student record
#searching student record
#updating student record
#reading students record
#deleting a students record
#################
#file name students.dat

import pickle

def append_record()->str:#qc check-> passed
    with open('students.dat', 'ab') as file:
        x = 'y'
        while x=='y':
            name = str(input('enter name: '))
            rollno = int(input('enter rollno: '))
            marks = int(input('enter marks: '))
            main_sol = [name, rollno, marks]
            pickle.dump(main_sol, file)

            x = input('enter n to stop and y to proceed: ')


def search_record()->str:#qc check-> passed
    with open('students.dat', 'rb') as file:
        main_list = list()
        try:
            while True:
                a = pickle.load(file)
                main_list.append(a)
        except:
            print('data sacking was successful')

        rollno = int(input('enter the rollno: '))
        for i in main_list:
            if i[1]==rollno:
                print(F"""
found results for your search:
name = {i[0]}
rollno = {i[1]}
marks = {i[2]}""")
            found = True
        
        if not found:
            print("Ooopsss... no such data could be found")




def name_update_record()->str:
    with open('students.dat', 'rb') as file:
        main_list = list()
        try:
            while True:
                a = pickle.load(file)
                main_list.append(a)
        except:
            pass

    #------------------------------------------------------------------------------------------------------->
    rollno = int(input('enter the rollno whose name should be updated: '))

    found = False
    count=0
    for i in main_list:
        if i[1]==rollno:
            name = str(input('enter the new name: '))
            main_list[count][0] = name
            found = True
        count+=1

    if not found:
        print('no such record with that rollno. was detectable')
    
    else:
        with open('students.dat', 'wb') as file:            
            try:
                for i in main_list:
                    pickle.dump(i, file)
            except:
                print("Goodness... i'm so sorry ya got a fatal error to be dealt with")

            print('updated succesfully')




def delete_record()->str:#qc check-> passed

    with open('students.dat', 'rb') as file:
        main_list = list()
        try:
            while True:
                a = pickle.load(file)
                main_list.append(a)
        except:
            pass

    #------------------------------------------------------------------------------------------------------->
    rollno = int(input('enter the rollno whose name should be deleted: '))

    found = False
    
    for i in main_list:
        if i[1]==rollno:
            main_list.remove(i)
            found = True

    if not found:
        print('no such record with that rollno. was detectable')
    
    else:
        with open('students.dat', 'wb') as file:            
            try:
                for i in main_list:
                    pickle.dump(i, file)
            except:
                print('Dangg.. a glitch has cuffed ya!')

            print('deleted successfully')


def read_record()->str:#qc check-> passed
    with open('students.dat', 'rb') as file:
        main_list = list()
        try:
            while True:
                a = pickle.load(file)
                main_list.append(a)
        except:
            pass
        
        for i in main_list:
            print(i)



print('''
ya got 5 assortments. Just grab one:
(1. append new elements to record)
(2. search the info of a row from the record)
(3. delete a row from the record)
(4. to update the name of a row from the record)
(5. to read the entire record in a single go)
(6. to exit the program)''')
while True:

    x = int(input('''
(engrave your choice right here)->>> '''))

    if x == 1:
        append_record()

    elif x == 2:
        search_record()

    elif x == 3:
        delete_record()

    elif x == 4:
        name_update_record()

    elif x == 5:
        read_record()

    elif x ==6:
        print('thanks for choosing us... catch ya soon')
        break

    else:
        print("hey.. dont make me yell... please give a valid input")
