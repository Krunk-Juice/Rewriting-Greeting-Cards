# CPSC 535 Advanced Algorithms
# Project 1: Rewriting greeting cards
# Christopher Ta     cta002@csu.fullerton.edu
# Sicheng Long       xlongx@csu.fullerton.edu

'''
Read the text file, 
get S[], and split the sentence to words
get LS[]
'''
def split_text(filename):
    # read the 1st line
    file_object = open(filename)
    text_content = file_object.readline()
    # output S[]
    print("S[] = \"", text_content[:-1], "\"")
    print("N =", len(text_content) - 1)
    
    #read the 2nd line, and get LS[]
    LS_content = file_object.readline()
    LS = []
    
    in_word = False
    replace_list = []
    for a in LS_content:
        if a == "\"":  # a == "
            if in_word == False:    # reach the beginning of a new word
                word = ""
                in_word = True
            else: # in_word == True, and it's the end of the word
                replace_list.append(word)
                in_word = False
        else:   # a != "
            if in_word == True:   # in_word == True, add the letter to the current word
                word += a
            
    #print(replace_list)
    for j in range(len(replace_list)//2):
        word_pair = (replace_list[2*j], replace_list[2*j + 1])
        LS.append(word_pair)
    
    # output LS[]
    print("M =", len(LS))
    print("LS[] =", LS)
    
    # split the file and return the words list
    text_list = text_content.split()
    
    file_object.close()
    return (text_list, LS)

'''
The punctuation
'''
def punctuation(a):
    if a == "," or a == "." or a == "?" or a == "!" or a == ":":
        return 1
    else:
        return -1
    
def replace_word(text_list, LS):
    new_word_list = []
    for word in text_list:
        
        '''
        # first_upper store the first letter of word, if it is uppercase, first_upper = True
        w = word[0]
        first_upper = False
        if w.isupper():
            first_upper = True
        '''
            
        p = ""
        changed = False
        
        # seperate the word and punctuation
        if punctuation(word[-1]) == 1:
            p = word[-1]
            word = word[:-1]
        
        # compare the elements in LS with word
        # if the same replace the word
        for word_pair in LS:
            if word_pair[0] in word and changed == False:
                #i = len(word_pair[0])
                #x = word[i : ]
                #word = word_pair[1] + x
                word = word.replace(word_pair[0], word_pair[1])
                changed = True
        '''
        # if the first letter is uppercase, change it to upper() after the replacement 
        if first_upper:
            W = str(word)[0].upper()
            word = W + str(word)[1:]
        '''        
        
        # add the punctuation back
        word = word + str(p)
        new_word_list.append(word)
    return new_word_list
    
'''
Rewrite the new word list to a string
'''
def new_string(new_word_list):
    string = ""
    for word in new_word_list:
        word += " "
        string += word
    return string


if __name__ == '__main__':
    filename = input("Please enter the file name:")
    print()
    print("Input:")
    text_list = split_text(filename)
    new_text_list = replace_word(text_list[0], text_list[1])
    R = new_string(new_text_list)
    print()
    print("Output:")
    print("R[] = \"", R[:-1], "\"")
