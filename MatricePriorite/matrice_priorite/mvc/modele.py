# Modèle

class Tache:
    def __init__(self, description):
        self.description = description
        self.est_completee = False

    def completer(self):
        self.est_completee = True

    def __str__(self):
        etat = "complétée" if self.est_completee else "non complétée"
        return f"Tâche : {self.description} ({etat})"


class ListeTaches:
    def __init__(self):
        self.liste = []

    def ajouter(self, description):
        nouvelle_tache = Tache(description)
        self.liste.append(nouvelle_tache)

    def completer(self, index):
        if 0 <= index < len(self.liste):
            self.liste[index].completer()

    def __str__(self):
        if not self.liste:
            return "Aucune tâche dans la liste."
        else:
            liste_taches_str = "\n".join([f"{i + 1}. {tache}" for i, tache in enumerate(self.liste)])
            return f"\nLISTE DES TÂCHES :\n{liste_taches_str}"
    
    def supprimer(self, index):
        if 0 <= index < len(self.liste):
            del self.liste[index]

    def modifier_description(self, index, nouvelle_description):
        if 0 <= index < len(self.liste):
            self.liste[index].description = nouvelle_description

    def sauvegarder_taches(self, nom_fichier):
        with open(nom_fichier, 'w') as file:
            for tache in self.liste:
                file.write(f"{tache.description},{tache.est_completee}\n")

    def charger_taches(self, nom_fichier):
        self.liste = []
        try:
            with open(nom_fichier, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    description, est_completee_str = line.strip().split(',')
                    est_completee = est_completee_str == 'True'
                    nouvelle_tache = Tache(description)
                    nouvelle_tache.est_completee = est_completee
                    self.liste.append(nouvelle_tache)
        except FileNotFoundError:
            print("Fichier introuvable. Commencez avec une nouvelle liste de tâches.")
    