import time
from eleve import Eleve
from note import Note

eleves = []
notes = []

def afficher_menu():
    print("******************************************************")
    print("BIENVENU DANS L’APPLICATION ETAB v1.0")
    print("******************************************************")
    print("MENU:")
    print("1: Ajouter un élève")
    print("2: Supprimer un élève")
    print("3: Modifier les informations de l'élève")
    print("4: Lister les élèves")
    print("5: Gérer les notes")
    print("6: Quitter")
    print("Date système :", time.strftime("%H:%M"))

def ajouter_eleve():
    id = input("Entrez l'identifiant de l'élève: ")
    nom = input("Entrez le nom de l'élève: ")
    prenom = input("Entrez le prénom de l'élève: ")
    age = int(input("Entrez l'âge de l'élève: "))
    genre = input("Entrez le genre de l'élève: ")
    eleve = Eleve(id, nom, prenom, age, genre)
    eleves.append(eleve)
    eleve.afficher_info()
    choix = input("1. Ajouter un autre élève\n2. Revenir au menu\n")
    if choix == "1":
        ajouter_eleve()
    else:
        afficher_menu()

def supprimer_eleve():
    id = input("Entrez l'identifiant de l'élève à supprimer: ")
    for eleve in eleves:
        if eleve.id == id:
            eleves.remove(eleve)
            print(f"Élève {eleve.nom} {eleve.prenom} supprimé.")
            choix = input("1. Supprimer un autre élève\n2. Revenir au menu\n")
            if choix == "1":
                supprimer_eleve()
            else:
                afficher_menu()
            return
    else:
        print("Aucun élève trouvé avec cet identifiant.")
        afficher_menu()

def lister_eleve():
    for eleve in eleves:
        print(f"ID: {eleve.id}, Nom: {eleve.nom}, Prénom: {eleve.prenom}, Age: {eleve.age}, Genre: {eleve.genre}")
    afficher_menu()

def modifier_eleve():
    id = input("Entrez l'identifiant de l'élève à modifier: ")
    for eleve in eleves:
        if eleve.id == id:
            while True:
                print("1. Modifier le nom")
                print("2. Modifier le prénom")
                print("3. Modifier l'âge")
                print("4. Modifier l'identifiant")
                print("5. Retour")
                print("6. Accueil")
                choix = input("Entrez votre choix: ")
                if choix == "1":
                    eleve.nom = input("Entrez le nouveau nom: ")
                elif choix == "2":
                    eleve.prenom = input("Entrez le nouveau prénom: ")
                elif choix == "3":
                    eleve.age = int(input("Entrez le nouvel âge: "))
                elif choix == "4":
                    eleve.id = input("Entrez le nouvel identifiant: ")
                elif choix == "5":
                    return
                elif choix == "6":
                    afficher_menu()
                    return
                else:
                    print("Choix invalide. Réessayez.")
            break
    else:
        print("Aucun élève trouvé avec cet identifiant.")
        afficher_menu()

def gerer_notes():
    while True:
        print("1. Ajouter une note")
        print("2. Modifier une note")
        print("3. Supprimer une note")
        print("4. Afficher les notes")
        print("5. Retour")
        print("6. Accueil")
        choix = input("Entrez votre choix: ")
        if choix == "1":
            ajouter_note()
        elif choix == "2":
            modifier_note()
        elif choix == "3":
            supprimer_note()
        elif choix == "4":
            afficher_notes()
        elif choix == "5":
            return
        elif choix == "6":
            afficher_menu()
            return
        else:
            print("Choix invalide. Réessayez.")

def ajouter_note():
    id = input("Entrez l'identifiant de la note: ")
    valeur = input("Entrez la valeur de la note: ")
    eleve_id = input("Entrez l'identifiant de l'élève: ")
    matiere = input("Entrez la matière: ")
    eleve = next((e for e in eleves if e.id == eleve_id), None)
    if eleve:
        note = Note(id, valeur, eleve, matiere)
        notes.append(note)
    else:
        print("Élève non trouvé.")
    afficher_menu()

def modifier_note():
    id = input("Entrez l'identifiant de la note à modifier: ")
    for note in notes:
        if note.id == id:
            note.valeur = input("Entrez la nouvelle valeur de la note: ")
            break
    else:
        print("Note non trouvée.")
    afficher_menu()

def supprimer_note():
    id = input("Entrez l'identifiant de la note à supprimer: ")
    for note in notes:
        if note.id == id:
            notes.remove(note)
            print("Note supprimée.")
            choix = input("1. Supprimer une autre note\n2. Revenir au menu\n")
            if choix == "1":
                supprimer_note()
            else:
                afficher_menu()
            return
    else:
        print("Note non trouvée.")
        afficher_menu()

def afficher_notes():
    for note in notes:
        print(f"ID: {note.id}, Valeur: {note.valeur}, Élève: {note.eleve.nom} {note.eleve.prenom}, Matière: {note.matiere}")
    afficher_menu()

def quitter_application():
    print("Au revoir !")
    print("Durée de la session :", time.strftime("%H:%M"))

def main():
    start_time = time.time()
    afficher_menu()
    while True:
        choix = input("Entrez votre choix: ")
        if choix == "1":
            ajouter_eleve()
        elif choix == "2":
            supprimer_eleve()
        elif choix == "3":
            modifier_eleve()
        elif choix == "4":
            lister_eleve()
        elif choix == "5":
            gerer_notes()
        elif choix == "6":
            quitter_application()
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
