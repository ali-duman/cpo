class Palindrome:
    def estPalindrome(self):
        if str(self) == str(self[::-1]):
            return 1
        else:
            return 0


mot = input("Veuillez saisir un mot : ")
result = Palindrome.estPalindrome(mot)

if result == 1:
    print("Le mot", mot, "est un palindrome.")
else:
    print("Le mot", mot, "n'est pas un palindrome.")
