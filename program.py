#MAIN_MENU=======================================================
def get_input(string: str, valid_options: list) -> str:
    user_input = input(string)
    
    is_number = False
    while not is_number:    
        try:
            user_input = int(user_input)

            if user_input in valid_options:
                return user_input
            
        except ValueError:
            print(f"{user_input} is not an integer. Re-enter choice: ")
            user_input = input(string)        
        
        
#FILE_HANDLING===================================================
def writeToFile(filename, data):
    try:
        file = open(filename, "a")
        for sub_array in data:
            tmp = ""
            for index, element in enumerate(sub_array):
                if (index == len(sub_array)-1):
                    tmp += element
                else:
                    tmp += element + ", "
            
            file.write(tmp + '\n')
            
        return True
    
    except Exception as e:
        print(e)
        
def openFile(filename, mode, split_=","):
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
            
def return_output(list):
    for sub_array in list:
        for value in sub_array:
            print(value, end="")
        

if __name__ == "__main__":
    print(("1) Display,\n2) Edit, \n3) Exit"))
    choice = get_input("> ", [1, 2, 3])
    
    while choice != 3:
        fileNAME = input("Filename: ")
        if choice == 1:
            print()
            return_output(openFile(fileNAME, "r"))
            
        elif choice == 2:
            output = openFile(fileNAME, "a+")
            sub_array = []
            for i in range(2):
                sub_array.append(input(f"Index {i}: "))
            output.append(sub_array)
            
            writeToFile(fileNAME, output)
        
        choice = get_input("\n> ", [1, 2, 3])
            
            
    print("Exited program")
    