#PROGRAM TO REMOVE DUPLICATES FROM A LIST

def remDuplicates(lst):
    A, B= list(), list()        #defining list A for unique items and B for duplicates
    for i in lst:
        if i in A:              #if same item encountered before, put in list B
            B.append(i)
        else:
            A.append(i)         #else put in list of unique items i.e. A
    return A

if __name__=='__main__':
    input_list= input("Enter a space separated list of items: ").split()
    output_list= remDuplicates(input_list)
    print("List after removing duplicates from the given list:", output_list)
