class Eleve:
    def __init__(self, id, nom, prenom, age, genre):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.genre = genre
    
    def afficher_info(self):
        print(f"ID: {self.id}, Nom: {self.nom}, Prénom: {self.prenom}, Age: {self.age}, Genre: {self.genre}")
        
