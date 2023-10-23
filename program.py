import random
import datetime

#MAIN_MENU=======================================================
def get_input(string: str, valid_options: list) -> str:
    user_input = input(string)
    
    while True:
        try:
            user_input = int(user_input)

            if user_input in valid_options:
                return user_input

            else:
                print("Input not in valid choices. Re-enter choice: ")
                user_input = input(string)
            
        except ValueError:
            print(f"{user_input} is not an integer. Re-enter choice: ")
            user_input = input(string)        
        
        
#FILE_HANDLING===================================================
def writeToFile(filename, data, mode="a"):
    try:
        file = open(filename, mode)
        for sub_array in data:
            tmp = ""
            for index, element in enumerate(sub_array):
                if (index == len(sub_array)-1):
                    tmp += element
                else:
                    tmp += element + ", "
            
            file.write(tmp + '\n')
            
        file.close()
        
        return True
    
    except Exception as e:
        print(e)
        
def openFile(filename, mode="r", split_=","):
    file_open = False
    while not file_open:
        try:
            output = []
            with open(filename, mode) as file:
                for line in file:
                    compliment = line.split(split_)
                    output.append(compliment)
            file.close()
            return output
        
        except IOError as e:
            print(f"Could not open {filename}. Error: {e}")
            filename = input("Re-enter filename: ")


#TESTING-FUNCTION====================================================
def test_knowledge(filename):
    test_file = openFile(filename)

    score = 0
    questions_asked = 0

    while questions_asked != len(test_file):
        # definition_or_keyword = random.randint(0, 1)
        definition_or_keyword = 0

        if definition_or_keyword == 0:
            choices = []
            chosen = []
            already = []
            for i in range(4):
                random_ = random.randint(0, len(test_file)-1)
                already.append(random_)
                while random_ in already:
                    random_ = random.randint(0, len(test_file)-1)
                already.append(random_)

                

                choices.append([(test_file[random_][1]).strip("\n"), random_])

            indexes = []
            for sub_array in choices:
                indexes.append(sub_array[1])

            rand_index = random.choice(indexes)
            question_number = questions_asked + 1

            print(f"\n{question_number}) The random keyword is '{test_file[rand_index][0]}'. What is the corresponding defintion?")
            printList(choices)
            choice = get_input("> ", [0, 1, 2, 3])

            if (test_file[rand_index][1]).strip("\n") == (choices[choice][0]):
                print("Correct answer. Score += 1")
                score += 1
                questions_asked += 1

            else:
                print("Incorrect answer.")
                questions_asked += 1

    username = input(f"You reached a score of: {score}. Enter a username: ")
    current_time = datetime.datetime.now()
    writeToFile("High_Scores.txt", [[str(current_time)[:10], username+" - "+str(score)]], "w+")
    

#RETURN_OUTPUT_FUNC======================================================
def return_output(given_list):
    lens = []
     
    for i in range(len(given_list)):
        for j in range(len(given_list[i])):
                lens.append(len(given_list[i][0]))

    for i in range(len(given_list)):
        output2 = []

        for j in range(len(given_list[i])):
                output = f"{given_list[i][j]}"
                output2.append(output)

        calc = ((max(lens)+min(lens))-len(given_list[i][0]))
        dots = '.'*calc
        info = f'{dots}: '.join(output2)

        print(f"{info}", end="") 

#PRINT_2D_LIST==========================================================
def printList(list_):
    for index, element in enumerate(list_):
        print(f"{index}){element[0]}")
    

#MAIN_MENU==============================================================
def main(fileNAME):
    print(("1) Display,\n2) Edit, \n3) Test, \n4) View Scoreboard \n5) Exit"))
    choice = get_input("> ", [1, 2, 3, 4, 5])

    while choice != 5:  
        if choice == 1:
            print()
            return_output(openFile(fileNAME))
            
        elif choice == 2:
            output = openFile(fileNAME, "a+")
            sub_array = []
            for i in range(2):
                sub_array.append(input(f"Index {i}: "))
            output.append(sub_array)
            
            writeToFile(fileNAME, output)

        elif choice == 3:
            test_knowledge(fileNAME)

        elif choice == 4:
            print()
            return_output(openFile("High_Scores.txt"))
        
        choice = get_input("\n> ", [1, 2, 3, 4, 5])
    
    print("Exited program")
    

main(input("Filename: "))