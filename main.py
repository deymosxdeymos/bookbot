import sys
from stats import get_book_text, count_words, count_chars, sort_char_counts


def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]

  try:
    book_text = get_book_text(book_path)
  except FileNotFoundError:
    print(f"Error: File not found at path: {book_path}")
    sys.exit(1)
  except Exception as e:
    print(f"Error: An error occurred while reading the file: {e}")
    sys.exit(1)

  word_count = count_words(book_text)
  char_counts = count_chars(book_text)
  sorted_char_counts = sort_char_counts(char_counts)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for item in sorted_char_counts:
    print(f"{item['char']}: {item['count']}")
  print("============= END ===============")


if __name__ == "__main__":
  main()
