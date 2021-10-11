# Problem 2


def fill_completions(filename):

    f = open("articles.txt")
    data = f.read()
    f.close()
    words_dirty = data.split()

    words_clean = []

    #only use alphanum words
    for i in words_dirty:
        if i.isalpha() == True:
            words_clean.append(i)
    #make lowercase
    for i in range(len(words_clean)):
        words_clean[i] = words_clean[i].lower()

    dict ={}

    for i in words_clean:
        for n in i:
            dict[(i.find(n), n)] = i
         
    return(dict)


def find_completions(prefix, c_dict):

    final_set = set()

    #why is this just returning the last char in the prefix input?
    for i in prefix:
        vals = (prefix.index(i), i)

    #this is only returning one value from the dict
    for key, value in dict.items(c_dict):
        if vals == key:
            final_set.add(value)
    

    return(final_set)


#print(fill_completions("articles.txt"))
print(find_completions("he", fill_completions("articles.txt")))