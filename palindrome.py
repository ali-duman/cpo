class Palindrome:
    def __init__(self, mot):
        self.mot = str

    def est_palindrome(self):
        if str(self) == str(self[::-1]):
            return 1
        else:
            return 0


if __name__ == '__main__':
    mot = input("Veuillez saisir un mot : ")
    result = Palindrome.est_palindrome(mot)

    if result == 1:
        print("Le mot", mot, "est un palindrome.")
    else:
        print("Le mot", mot, "n'est pas un palindrome.")
