class EnglishToNATO:

    def __init__(self):
        return

class EnglishToNATO:

    def __init__(self):
        self.NATO = {'A':'Alfa', 'B':'Bravo', 'C':'Charlie', 'D':'Delta', 'E':'Echo', \
                     'F':'Foxtrot','G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliett', \
                     'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', \
                     'Q':'Quebec', 'R':'Romeo', 'S':'Sierra','T':'Tango', 'U':'Uniform', \
                     'V':'Victor', 'W':'Whiskey', 'X':'X-ray', 'Y':'Yankee', 'Z':'Zulu', \
                     ',':'Comma', ' ':'Space', ';':'Semi-colon', '.':'Period'}

    def chat_bot(self):
        usr = input("what would you like to spell?\n")
        for i in usr:
            letter = str(i[0]).upper()
            # print(letter)
            # print(self.NATO[letter])
            if letter in self.NATO:
                print(letter + " as in " + str(self.NATO[letter]))
            else:
                print(letter + " as in " + "Not Translatable")

class NATOtoEnglish:

    def __init__(self):
        self.NATO = {'Alfa':'A','Bravo':'B','Charlie':'C','Delta':'D','Echo':'E','Foxtrot':'F',
                     'Golf':'G','Hotel':'H','India':'I','Juliett':'J','Kilo':'K','Lima':'L',
                     'Mike':'M','November':'N','Oscar':'O','Papa':'P','Quebec':'Q','Romeo':'R',
                     'Sierra':'S','Tango':'T','Uniform':'U','Victor':'V','Whiskey':'W','X-ray':'X',
                     'Yankee':'Y','Zulu':'Z','Comma':',','Space':' ','Semi-colon':';','Period':'.'}

    def chat_bot(self):
        usr = input("what would you like to spell?\n")
        return_str = ''
        for i in usr.split():
            str_fixer = i[0].upper() + i[1:len(i)].lower()
            return_str += self.NATO[str_fixer]
        print(return_str)

class EnglishToLetters:

    def __init__(self):
        self.Letters = {'A':'ae','B':'bee','C':'cee','D':'dee','E':'ee','F':'eff','G':'gee',
                        'H':'aitch','I':'i','J':'jay','K':'kay','L':'el','M':'em','N':'en',
                        'O':'oh','P':'pee','Q':'queue','R':'ar','S':'ess','T':'tee','U':'you',
                        'V':'vee','W':'double-you','X':'ex','Y':'why','Z':'zee',',':'Comma',
                        ' ':'Space',';':'Semi-colon','.':'Period'}

    def chat_bot(self):
        usr = input("what would you like to spell?\n")
        for i in usr:
            letter = str(i[0]).upper()
            if letter in self.Letters:
                print(letter + " as in " + str(self.Letters[letter]))
            else:
                print(letter + " as in " + "Not Translatable")

class LettersToEnglish:

    def __init__(self):
        self.Letters = {'ae': 'A', 'bee': 'B', 'cee': 'C', 'dee': 'D', 'ee': 'E', 'eff': 'F',
                    'gee': 'G', 'aitch': 'H', 'i': 'I', 'jay': 'J', 'kay': 'K', 'el': 'L',
                    'em': 'M', 'en': 'N', 'oh': 'O', 'pee': 'P', 'queue': 'Q', 'ar': 'R',
                    'ess': 'S', 'tee': 'T', 'you': 'U', 'vee': 'V', 'double-you': 'W', 'ex': 'X',
                    'why': 'Y', 'zee': 'Z', 'Comma': ',', 'Space': ' ', 'Semi-colon': ';',
                    'Period': '.'}

    def chat_bot(self):
        usr = input("what would you like to spell?\n")
        return_str = ''
        for i in usr.split():
            str_fixer = i[0].lower() + i[1:len(i)].lower()
            return_str += self.Letters[str_fixer]
        print(return_str)


if __name__ == "__main__":
    # e2n = EnglishToNATO()
    # print(e2n.NATO['A'])
    # e2n.chat_bot()
    # self.NATO = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', \
    #              'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', \
    #              'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', \
    #              'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', \
    #              'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu', \
    #              ',': 'Comma', ' ': 'Space', ';': 'Semi-colon', '.': 'Period'}
    # for i in e2n.NATO:
    #     print('\''+e2n.NATO[i]+'\''+':'+'\''+i+'\''+',', end = '')
    # Letters = {'ae': 'A', 'bee': 'B', 'cee': 'C', 'dee': 'D', 'ee': 'E', 'eff': 'F',
    #                 'gee': 'G', 'aitch': 'H', 'i': 'I', 'jay': 'J', 'kay': 'K', 'el': 'L',
    #                 'em': 'M', 'en': 'N', 'oh': 'O', 'pee': 'P', 'queue': 'Q', 'ar': 'R',
    #                 'ess': 'S', 'tee': 'T', 'you': 'U', 'vee': 'V', 'double-you': 'W', 'ex': 'X',
    #                 'why': 'Y', 'zee': 'Z', 'Comma': ',', 'Space': ' ', 'Semi-colon': ';',
    #                 'Period': '.'}
    # for i in Letters:
    #     print('\''+Letters[i]+'\''+':'+'\''+i+'\''+',', end = '')
    # n2e = NATOtoEnglish()
    # n2e.chat_bot()
    # e2l = EnglishToLetters()
    # e2l.chat_bot()
    l2e = LettersToEnglish()
    l2e.chat_bot()




