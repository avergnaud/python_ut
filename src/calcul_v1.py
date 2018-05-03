class Calcul:
    
    def traduitSecondes(self, nombre_total):

        # Ecrivez un programme qui convertit un nombre entier de secondes fourni
        # au départ en un nombre d'années, de jours, de minutes et de secondes (utilisez l'opérateur %)

        une_seconde = 1
        une_minute = 60
        une_heure = 3600
        un_jour = 86400
        un_an = 31536000
        modulo = 1

        # nombre_total = int(input("Entrez un nombre de secondes à convertir an/mois/heure etc: "))

        while modulo > 0:

            nombre_année = nombre_total // un_an
            modulo = nombre_total % un_an

            nombre_jour = modulo // un_jour
            modulo = modulo % un_jour

            nombre_heure = modulo // une_heure
            modulo = modulo % une_heure

            nombre_minute = modulo // une_minute
            modulo = modulo % une_minute

            nombre_seconde = modulo // une_seconde
            modulo = modulo % une_seconde

        return str(nombre_année) + " ans " + str(nombre_jour) + " jours " + str(nombre_heure) + " heures " + str(nombre_minute) + " minutes " + str(nombre_seconde) + " secondes"
