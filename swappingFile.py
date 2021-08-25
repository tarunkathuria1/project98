def swapfile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file =  open(fileName, 'r')
    print("this is the text from file1")
    print(thisisthetextfromfile1)


    file =  open(fileName, 'r')
    print("this is the text from file2")
    print(thisisthetextfromfile2)

    file =  open(fileName, 'w')
    print("this is the text from file2")
    print(thisisthetextfromfile2)


    file =  open(fileName, 'w')
    print("this is the text from file1")
    print(thisisthetextfromfile1)

swapfile()
