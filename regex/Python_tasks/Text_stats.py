# Create a class that:
#• When creating an instance, it required entering the text for which it will count statistics.
# The first conversion occurred when the instance was initialized.
#Each instance had attributes: - lower_letters_num - which stores the number of all lowercase letters in the text
#- upper_letters_num - holds the number of all uppercase letters in the text
#- punctuation_num - storing the number of punctuation characters in the text.
#- digits_num - the number of digits present in the text.
# stats - a dictionary that stores the statistics of letters, numbers and punctuation in the text.
# Calculate statistics using the calculate_stats method.

import re
class LetterStats():
    def __init__(self, text):
        self.lower_l_num = None
        self.upper_l_num = None
        self.punct_l_num = None
        self.digits_l_num = None
        self.stats = {}
        self.text = text
        self._calculate_stats()

    def _calculate_stats(self):
        self.lower_l_num = len(re.findall(r'[a-ząćęłóżź]', self.text))
        self.upper_l_num = len(re.findall(r'[A-ZĄĆĘŁÓŻŹ]', self.text))
        self.punct_l_num = len(re.findall(r'[.?\-",:;!]', self.text))
        self.digits_l_num = len(re.findall(r'[0-9]', self.text))
        self.stats = {'lower_letters': self.lower_l_num,
                      'upper_letters': self.upper_l_num,
                      'punctuation': self.punct_l_num,
                      'digits': self.digits_l_num}
        return self.stats

    def add_text(self, text):
        self.text = text
        self._calculate_stats()
        return self.stats