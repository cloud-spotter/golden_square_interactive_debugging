class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:] 
            else:
                i += 1  # BUG here in original code (no else: before this line so code skipped consecutive vowels)
        return self.text
    
remover = VowelRemover("aeiou")
print(remover.remove_vowels())
