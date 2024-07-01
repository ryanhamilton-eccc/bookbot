

def read_book(path):
    with open(path, 'r') as fh:
        contents = fh.read()
    return contents


def count_words(data):
    return len(data.split())

def count_chars(data):
    counts = {}
    for char in data:
        char = char.lower()
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts


def sanitize_and_transpose_char_counts(char_counts):
    counts = [
        {'char': x, 'counts': y} for x,y in char_counts.items() if x.isalpha()
    ]
    counts.sort(reverse=True, key=lambda x: x['counts'])
    return counts


def print_report(fpath, total_words, char_counts):
    print(f"--- Begin report of {fpath} ---")
    print(f"{total_words} words found in the document", end="\n\n")
    for data in char_counts:
        counts = data['counts']
        char = data['char']
        print(f"The '{char}' character was found {counts} times")
    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    word_count = count_words(contents)
    char_count = sanitize_and_transpose_char_counts(count_chars(contents))
 
    print_report(
        fpath=book_path,
        total_words=word_count,
        char_counts=char_count
    )
    

if __name__ == '__main__':
    main()
