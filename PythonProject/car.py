class Car:
    #on a besoin du init pour construire un objet
    # self represente l'objet qu"on souhaite creer = car
    # apres on ajoute des parametres pour les attributs de la voiture
    # une methode est une action que l'object peut faire
    def __init__(self, model, year, color, for_sale):
        # pour acceder l'attribut donnee
        # quand on recoit le modele on va assigner a l'object self.model
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.color} {self.model} car")

    def stop(self):
        print(f"you stop the {self.color} {self.model} car ")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")