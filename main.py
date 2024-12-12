"""jjj"""#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    resultat=[]
    occurence=0
    lettre_courante=None

    for lettre in s:
        if lettre_courante == lettre :
            occurence+=1

        else:
            resultat.append((lettre_courante, occurence))
            lettre_courante=lettre
            occurence+=1
    return resultat+[(lettre_courante,occurence)]


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères pas

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
        """
    if not s :
        return []

    lettre_courante=s[0]
    occurence=1
    for lettre in s[1:]:
        if lettre==lettre_courante :
            occurence+=1
        else :
            break

    return [(lettre_courante,occurence)]+artcode_r(s[occurence:])


#### Fonction principale


def main():
    """jjjjjjj"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
