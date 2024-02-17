# Contrôleur
from modele import ListeTaches
from vue import Vue

class Controleur:
    def __init__(self):
        self.liste_taches = ListeTaches()
        self.vue = Vue()

    def run(self):
        self.liste_taches.charger_taches("taches.txt")

        while True:
            self.vue.afficher_liste(str(self.liste_taches))
            choix = self.vue.demander_option()

            if choix == '1':
                description = self.vue.demander_tache()
                self.liste_taches.ajouter(description)

            elif choix == '2':
                index = self.vue.demander_index()
                self.liste_taches.completer(index)

            elif choix == '3':
                #index = self.vue.demander_index()
                print('\n')
                print('=====LISTES DES TÂCHES =====')
                self.liste_taches.__str__()
                print('\n')
                                            
            elif choix == '4':
                index = self.vue.demander_index()
                self.liste_taches.supprimer(index)

            elif choix == '5':
                index = self.vue.demander_index()
                nouvelle_description = self.vue.demander_description_modifiee()
                self.liste_taches.modifier_description(index, nouvelle_description)

            elif choix == '6':
                self.liste_taches.sauvegarder_taches("taches.txt")
                break

            else:
                print("Option non valide. Veuillez choisir une option valide.")


