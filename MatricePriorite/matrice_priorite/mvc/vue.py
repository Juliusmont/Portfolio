# Vue

class Vue:
    @staticmethod
    def afficher_liste(taches):
        print(taches)

    @staticmethod
    def demander_tache() -> str:
        return input("Entrez la description de la tâche : ")

    @staticmethod
    def demander_option() -> str:
        while True:
            print("\n","OPTIONS DISPONIBLES :")
            print("1. Ajouter une tâche")
            print("2. Compléter une tâche")
            print("3. Lister les tâches")
            print("4. Supprimer une tâche")
            print("5. Modifier une tâche")
            print("6. Sauvegarder et Quitter")
            choix = input("===> Choisissez une option (1, 2, 3, 4, 5 ou 6) : ")
            if choix in ['1', '2', '3', '4', '5', '6']:
                return choix
            else:
                print("Veuillez choisir une option valide.")

    @staticmethod
    def demander_index() -> int:
        return int(input("Entrez le numéro de la tâche à compléter : ")) - 1

    @staticmethod
    def demander_description_modifiee() -> str:
        return input("Entrez la nouvelle description de la tâche : ")
