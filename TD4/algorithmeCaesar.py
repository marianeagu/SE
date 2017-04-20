# Cryptage et dechriptage Caesar
def caesar(plainText, shift): 
        cryptageText = ""
        for ch in plainText:
                ch = ch.lower()
                if ch == ' ':
                    cryptageText += ' '
                if ch.isalpha():
                        stayInAlphabet = ord(ch) + shift 
                        if stayInAlphabet > ord('z'):
                                stayInAlphabet -= 26
                        finalLetter = chr(stayInAlphabet)
                        cryptageTextt += finalLetter
        print "Shift:", shift, cryptageText
        return cryptageText

def decaesar(plainText, shift): 
        cryptageText = ""
        for ch in plainText:
                ch = ch.lower()
                if ch == ' ':
                   cryptageText += ' '
                if ch.isalpha():
                        stayInAlphabet = ord(ch) - shift
                        print stayInAlphabet
                        if stayInAlphabet < ord('a'):
                                diff = stayInAlphabet + shift - ord('a')
                                stayInAlphabet = diff + ord('a') + 26 - shift 
                        if stayInAlphabet > ord('z'):
                                stayInAlphabet -= 26                   
                        finalLetter = chr(stayInAlphabet)
                        cryptageTextt += finalLetter
        print "Shift:", shift, cryptageText
        return cryptageText
