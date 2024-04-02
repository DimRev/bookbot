def main():
  with open("./books/frankenstein.txt") as f:
    file_content = f.read()
    words_num = count_words(file_content)
    letters_dict = create_letters_dict(file_content)
    aggregate_and_print(words_num, letters_dict)

def count_words(s):
  words = s.split()
  return len(words)

def create_letters_dict(s):
  letters_dict = {}
  for letter in s:
    curr_letter = letter.lower()
    if curr_letter in letters_dict:
      letters_dict[curr_letter] += 1
    else:
      letters_dict[curr_letter] = 1
  return letters_dict

def is_alpha(letter):
  letter_lower = letter.lower()
  letter_upper = letter.upper()
  if letter_lower == letter_upper:
    return False
  return True

def sort_on(dict):
  value = next(iter(dict.values()), None)
  return value

def aggregate_and_print(words_num, letters_dict):
  print(f"{words_num} words found in the document\n")

  list_of_dicts = [{letter: count} for letter, count in letters_dict.items()]
  list_of_dicts.sort(reverse=True, key=sort_on)
  # print(list_of_dicts)
  for dict in list_of_dicts:
    value = next(iter(dict.values()), None)
    key = next(iter(dict.keys()), None)
    if is_alpha(key):
      print(f"The '{key}' character was found {value} times")
  print("--- End report ---")




main()