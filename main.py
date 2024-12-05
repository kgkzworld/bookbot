def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    print(file_contents)
    words(file_contents)
    count_characters(file_contents)

def words(text):
    print(len(text.split()))

def count_characters(text):
    split_text = text.split()
    character_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    for word in split_text:
        for character in word:
            new_character = character.lower()
            if new_character in character_dict:
                character_dict[new_character] += 1

    print(character_dict)

main()