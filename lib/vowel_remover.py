class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        result=''
        length = len(self.text)
        for i in range(0,length):
            if self.text[i].lower() not in self.vowels:
                result += self.text[i]
        return result
    