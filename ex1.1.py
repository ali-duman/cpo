import random, string


def creation_nom():
    letters = string.ascii_lowercase
    text = ''.join(random.choice(letters) for i in range(10))
    return text.title()


def categorie_age(age):
    if age == 9 or age == 10:
        return "Poussin"
    elif age == 11 or age == 12:
        return "Benjamin"
    elif age == 13 or age == 14:
        return "Minime"
    elif age == 15 or age == 16:
        return "Cadet"
    elif age == 17 or age == 18:
        return "Junior"
    elif 19 <= age <= 34:
        return "Senior"
    elif age >= 35:
        return "Vétéran"
    else:
        return "Erreur"


def presentation_personnage(nom, prenom, age, code):
    print("\nNOM \t\t: ", nom)
    print("PRENOM \t\t: ", prenom)
    print("AGE \t\t: ", age)
    print("CATEGORIE \t: ", code)


if __name__ == '__main__':
    for i in range(50):
        # Déclaration de variables
        nom = creation_nom()
        prenom = creation_nom()
        age = random.randint(0, 100)
        code = categorie_age(age)

        # Présentation du personnage
        presentation_personnage(nom, prenom, age, code)
