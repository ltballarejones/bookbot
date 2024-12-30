def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_characters_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters_count(text):
    word_dic = {}
    #parse through words
    #if exits update value +1
    #else add to dict with value of 1
    lowered_string = text.lower()
    for x in lowered_string:
        if(x in word_dic):
            word_dic[x] = word_dic[x] + 1
        else:
            word_dic[x] = 1
    return word_dic




main()
#with open("./books/frankenstein.txt") as f:
#   file_contents = f.read()
#  print(len(file_contents.split( )))