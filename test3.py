class Personne:
    def __init__ (self, nom, age, ville):
        self.nom= nom
        self.age = age
        self.ville = ville

    def se_présenter(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans et je viens de {self.ville}")

liste_Personne = [Personne("Matteo", 20 , "Reims"),
                  Personne("Bob", 19, "Orléans"),
                  Personne("Eva", 25, "Paris"),
                Personne("Lucas", 24, "Reims"),
                Personne("Lucie", 24, "Fismes")]
for i in liste_Personne :
    print(i.se_présenter())

class Etudiant(Personne):
    nb_etudiant = 0
    def __init__(self,nom, age, ville, matricule):
        nb_etudiant += 1
        super().__init__(nom, age, ville,)
        self.matricule = matricule

    def nombre_total(Etudiant):
         print(f"Le nombre total d'étudiants est {nb_etudiant}")
    def se_presenter(self):
            print(f"Je m'appelle {self.nom}, j'ai {self.age} ans et je viens de {self.ville} et mon matricule est  le {self.matricule}")
etudiants = []

for i in range(10):
    etudiant = Etudiant(f"Etudiant{i+1}", 18 + i, f"Ville{i+1}", f"MAT{i+1}")
    etudiants.append(etudiant)

for etudiant in etudiants:
    etudiant.se_presenter()



nombre_total(Etudiant)
age=25
def valider_age(Personne, age):
    if age < 120 :
        print ("True")
    else :
        print("False")
valider_age(Personne,age)