def main():
    
    with open("books/franksenstein.txt") as f:
       
        file_contents = f.read()
    #print(word_count(file_contents))
    #print(file_contents)
    #character_count(file_contents)
    create_report(file_contents)
   


def word_count(file_contents):
    
    return len(file_contents.split())



def character_count(file_contents):
    char_dict = {}
    lower_case = file_contents.lower()
    for char in lower_case:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def character_alpha_count(file_contents):
    char_dict = {}
    lower_case = file_contents.lower()
    for char in lower_case:
        if char in char_dict and char.isalpha():
            char_dict[char] += 1
        elif char.isalpha():
            char_dict[char] = 1
    return char_dict

def create_report(file_contents):
    char_dict = character_alpha_count(file_contents)
    book_length = word_count(file_contents)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{book_length} words found in the document")

    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    for char, count in sorted_char_dict.items():
        print(f"The '{char}' character was found {count} times")



main()
