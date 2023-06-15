# CPSC 535 Advanced Algorithms
# Project 1: Rewriting greeting cards
# Christopher Ta     cta002@csu.fullerton.edu
# Sicheng Long       xlongx@csu.fullerton.edu
# William Lee        leewilliam4@csu.fullerton.edu

'''
Read the text file, 
get S[]
get LS[]
'''
def get_text(filename):
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
        if a == "\"" or a == "\'":  # a == " or '
            if in_word == False:    # reach the beginning of a word
                word = ""
                in_word = True
            else: # in_word == True, and it's the end of a word
                replace_list.append(word)
                in_word = False
        else:   # a != "
            if in_word == True:   # in_word == True, add the letter to t word
                word += a
            
    #print(replace_list)
    for j in range(len(replace_list)//2):
        word_pair = (replace_list[2*j], replace_list[2*j + 1])
        LS.append(word_pair)
    
    # output LS[]
    print("M =", len(LS))
    print("LS[] =", LS)
    
    file_object.close()
    return (text_content, LS)

# get the appeared index of the word need to be replaced
def find_index(text_content, word):
    index_list = []
    index = text_content.find(word) # 1st index word appears in text_content
    while index != -1:
        index_list.append(index)
        index = text_content.find(word, index+1) # get the rest index
    
    return index_list

# replace 1 word
def replace_word(text_content, word_pair, boolean_array):    
    index_list = find_index(text_content, word_pair[0])  # the indices of word need to be replaced
    #print(index_list)   # for debug
    if len(index_list) != 0:
        for i in reversed(range(len(index_list))):
            if boolean_array[index_list[i]] == "0":   # if word here is not replaced, replace it, else do nothing
                text_content = text_content[:index_list[i]] + word_pair[1] + text_content[index_list[i] + len(word_pair[0]):]   # replace the word
                boolean_chunk = ""
                for j in range(len(word_pair[1])):
                    boolean_chunk += "1"
                boolean_array = boolean_array[:index_list[i]] + boolean_chunk + boolean_array[index_list[i] + len(word_pair[0]):]   # replace the positions with 1, to mark this word has been replaced
    #print(text_content[:-1])   # for debug
    #print(boolean_array)   # for debug
    #print()   # for debug
    return (text_content, boolean_array)

def replace(text_content, LS):
    boolean_array = ""
    for i in range(len(text_content)-1):
        boolean_array += "0"        # begin with all places are not replaced
    for word_pair in LS:
        replace_1_word = replace_word(text_content, word_pair, boolean_array)
        text_content = replace_1_word[0]       # update text_content after 1 word replacement
        boolean_array = replace_1_word[1]       # update boolean_array
    
    return text_content

if __name__ == '__main__':
    filename = input("Please enter the file name:")
    print()
    print("Input:")
    text_list = get_text(filename)
    new_text = replace(text_list[0], text_list[1])
    print()
    print("Output:")
    print("R[] = \"", new_text[:-1], "\"")

