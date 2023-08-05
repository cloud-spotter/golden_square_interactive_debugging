# Exercise - identifying bugs with VS Code Python interactive debugger

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0 
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1 
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char] 
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
# Actual output:
# [3, 'D']


## Original, with bugs:
# class LetterCounter:
#     def __init__(self, text):
#         self.text = text

#     def calculate_most_common(self):
#         counter = {}
#         most_common = None
#         most_common_count = 1                         # BUG? Why start a 1?
#         for char in self.text:
#             if not char.isalpha():
#                 continue
#             counter[char] = counter.get(char, 1) + 1  # BUG here, setting default value to 1 rather than 0, in get()
#             if counter[char] > most_common_count:
#                 most_common = char
#                 most_common_count += counter[char]    # BUG here (only need to reset var to counter[char] not add it to existing value)
#         return [most_common_count, most_common]

# Out of curiosity, where joint common letters:
counter = LetterCounter("Mississippi")  # Hmm, only shows 's' not 's' and 'i'
print(counter.calculate_most_common()) 
# Output:
# [4, 's']

# ChatGPT's improved code to address case where there's more than one common letter
# & it also identified a 4th bug -
# code doesn't handle the case where there's no alpha chars in 'text' input.
# Now returns [4, ['i', 's']] for Mississipi 'text' input.

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common_letters = []
        most_common_count = 0
        
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1
            if counter[char] > most_common_count:
                most_common_letters = [char]
                most_common_count = counter[char]
            elif counter[char] == most_common_count:
                most_common_letters.append(char)

        # Handle 'no alphabetical chars found'
        if most_common_count == 0:
            return [0, None]

        return [most_common_count, most_common_letters]

