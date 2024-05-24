#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            raise TypeError("Value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
     sentences = self.value.split(".")
     return len([sentence for sentence in sentences if sentence.strip() and sentence.strip().endswith("?")])
  
string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences()) 