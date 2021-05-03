import sys

#Function where arguments from the command line are sent
def mapping(input_):
    #Dictionary to store Key Value pairs
    mapper = { '0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four", 
                '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"}
    #List to store Result
    result = []
    for i in range(len(input_)):
        str_ = "" #Empty string to store output for each input argument
        for j in range(len(input_[i])):
            #Find Value from dictionary mapper to get 
            str_ += mapper[input_[i][j]]
        result.append(str_)
    return result

if __name__ == "__main__":
    input_ = sys.argv[1:]
    print(mapping(input_))