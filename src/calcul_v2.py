class Calcul:
    def generateURL(self, ticker, days, period):
        return "https://www.google.com/finance/getprices?i=" + str(period) + "&p=" + str(days) + "d&f=d,o,h,l,c,v&df=cpct&q=" + ticker

    def traduitSecondes(self, secondes):

        diviseurs = [365*24*60*60, 24*60*60, 60*60, 60, 1]

        resultat = []

        for diviseur in diviseurs:
           resultat.append(secondes // diviseur)
           secondes = secondes % diviseur

        return str(resultat[0]) + " ans " + str(resultat[1]) + " jours " + str(resultat[2]) + " heures " + str(resultat[3]) + " minutes " + str(resultat[4]) + " secondes"
