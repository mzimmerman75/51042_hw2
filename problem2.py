# Problem 2

def fill_completions(filename):
    #the purpose of this function is to open and read a text file and make a dictionary with the values being the words and the keys being the letters and their respective indices
    #the paramter is a text file 
    #the return value is a dictionary described above using the scrubbed text file

    f = open(filename)
    data = f.read()
    f.close()
    words_dirty = data.split()

    final_dict ={}
    #only use alphanum words
    for word in words_dirty:
        if word.isalpha() == True:
            for k, v in enumerate(word):
                if (k, v) in final_dict:
                    final_dict[(k, v)].add(word.lower())

                else:
                    final_dict[(k, v)] = set([word.lower()])
         
    #return(final_dict)
    return(final_dict)


def find_completions(prefix, c_dict):
    #the purpose of this function is to provide completed words that exactly match the keys from the dict in the above function
    #the paramters is a prefix of a word that is gathered through user input and a dict that is gathered by calling upon the previous function
    #the return value are those completed words from the dict in the previous function if there are any
    
    final_set = set()

    for k, v in enumerate(prefix):
        if k == 0:
            final_set = c_dict.get((k, v), set())
        else:
            final_set = final_set.intersection(c_dict.get((k, v), set()))

    return(final_set)
    

#print(fill_completions("articles.txt"))
#print(find_completions("candidate", fill_completions("articles.txt")))

def main():
    #the purpose of this function is to add user input and call upon the other two above functions
    #there are no direct paramters but inside this function the other two are being called upon
    #the return value is the user input terminal prompt and subsequently a match from the dict if it exists, it keeps repeating until "quit" is entered

    while(True):
        user_input = input("Please enter a prefix for iChat to complete:\n")

        if (user_input.lower() == "quit"):
            break

        #print(fill_completions("articles.txt"))
        #print(find_completions(user_input, fill_completions("articles.txt")))

        output = find_completions(user_input, fill_completions("articles.txt"))
        for element in output:
            print(element)
        else:
            print("No completions")

    print("Goodbye")

if __name__ == "__main__":
    main()