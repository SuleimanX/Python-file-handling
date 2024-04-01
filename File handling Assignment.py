from pathlib import Path


try:
    working_directory = Path(__file__).absolute().parent

    with open(working_directory/"my_file.txt", "w") as x:
        x.write("This is a cool string")
        x.write("\nThis is a cool string\n")
        x.write(str(10)+"\n")
        x.write(str(20)+"\n")
    
        


    with open(working_directory/ "my_file.txt", "a") as x:
        x.write("\nI went to watch World Rally Championship this weekend")
        x.write("\nNaivasha is a beautiful place full of laughter and joy")

    

    with open(working_directory/ "my_file.txt", "r") as x:
        for line in x:
            print(line, end="")

except FileNotFoundError as e:
    print(e)

finally:
    print("Executing finally...")