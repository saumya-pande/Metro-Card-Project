from sys import argv

def main():
    
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    with  open(file_path , 'r')  as file   :
        for  i in  file  :
            print(i)

    
if __name__ == "__main__":
    main()