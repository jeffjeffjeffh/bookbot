def count_words(str):
    words = str.split()
    return len(words)

def count_letters(str):
    lower_str = str.lower()
    letters = {}
    for letter in lower_str:
        if not letter.isalpha():
            continue
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(d):
    return d["count"]

def letters_dict_to_list(d):
    sorted_list = []
    for letter in d:
        sorted_list.append({"letter": letter, "count": d[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        letters_dict = count_letters(file_contents)
        sorted_letters_list = letters_dict_to_list(letters_dict)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document\n")

        for item in sorted_letters_list:
            print(f"The '{item['letter']}' character was found {item['count']} times")

main()