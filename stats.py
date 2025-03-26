def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)

def count_words(text):
    words = text.split()
    return f"{len(words)}"

def count_chars(text):
    count = {}
    chars = text.lower()

    for char in chars:
        if char in count:
             count[char] += 1
        else:
            count[char] = 1
    return count

def sort_char_counts(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({'char': char, 'count': count})
    sorted_chars.sort(key=lambda x: x['count'], reverse=True)
    return sorted_chars

