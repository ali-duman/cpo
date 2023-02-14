import os
import random


def clear():
    os.system('cls')


class Pendu:
    def __init__(self):
        self.nbr_essai = 1
        self.mots = ['python', 'amusant', 'instanciation', 'oiseau', 'girafe', 'fenetre', 'nombril', 'odoo']
        self.tentative = ""
        self.mot_recherche = self.mots[random.randint(0, len(self.mots))] # random.choice
        self.resultat = '_' * len(self.mot_recherche)

    def affichage_jeu(self):
        print("LE PENDU - Trouver le mot")
        print(f"\t\t{' '.join(self.resultat)}\n")
        print(f"Vos essais : {' '.join(self.tentative)}")

    def recherche(self):
        est_trouve = False
        while not est_trouve and self.nbr_essai <= 10:
            self.affichage_jeu()

            print(f"Essai n°{self.nbr_essai}\n")
            proposition = input("Tappe une lettre : ")

            self.tentative += proposition[0]
            self.nbr_essai += 1
            self.resultat = "".join([(c if c in self.tentative else "_") for c in self.mot_recherche])

            est_trouve = (self.resultat == self.mot_recherche)

        if est_trouve:
            print("Vous avez gagné ! ")
        else:
            print(f"Perdu ! Le mot était '{self.mot_recherche}'")


if __name__ == '__main__':
    mot = Pendu()
    mot.recherche()
