# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {value.letter: value.code for (key, value) in nato_phonetic.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

ask = True
while ask:
    user_value = input("Enter a word: ").upper()
    try:
        input_value = [nato_alphabet[letter] for letter in user_value]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(input_value)
        ask = False

