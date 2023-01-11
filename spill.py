import random  # Importerer "random" for å kunne velge et tilfeldig kort fra kortstokken
import time  # Importerer "time" for å kunne bruke "time.sleep" for å få en pause i tekstutskriften


class Spiller:
    """Bruker klassen "spiller" til å definere blant annet balanse og hånd, og hva som vil skje når spilleren dør eller blir frigjort. Dette gjør det lettere senere i programmet for å gjøre det mer ryddig."""

    def __init__(self):
        self.penger = 1000  # Spilleren starter med 1000 dollar
        self.hånd = []  # Spillerens hånd er tom ved oppstart

    def vedd(self, beløp):   # Metode for å vedde et beløp
        if beløp > self.penger:    # Sjekker om spilleren har nok penger til å vedde beløpet
            print("Du har ikke nok penger!")
            return False
        self.penger -= beløp    # Trekker beløpet fra spillerens penger
        return True

    def vinner(self, beløp):   # Metode for å legge til penger når spilleren vinner
        self.penger += beløp

    def dør(self):    # Metode for når spilleren taper alt
        print("Du er død. Spillet er over.")
        return False

    def fri(self):    # Metode for når spilleren vinner spillet
        print("\n\nGratulerer! Du har vunnet spillet og er løslatt. \n---------------------\nDu kommer deg trygt hjem til familien, med ingen minner om at noe av dette har skjedd. \n---------------------\n\n")
        return False


class Blackjack:
    """Blackjack klassen er klassen hvor selve rundgangen og reglene i spillet blir definert."""

    def __init__(self):
        # Lager en kortstokk med kortene 2-11, fire av hver. Her er bildekortene representert som de fire forskjellige 10-erne.
        self.kortstokk = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        self.dealer_hånd = []

    def spill(self, spiller):
        print("\nHei.")
        time.sleep(1)
        print("I dette spillet har du blitt kidnappet og er fanget i en kasino. Målet er å tjene penger til organisjonen som kidnappet deg..")
        time.sleep(5)
        print("Du må vinne i blackjack, men vær forsiktig.. ")
        time.sleep(2)
        print("Dersom du mister alle pengene dine blir du aldri sluppet fri.")
        time.sleep(3)
        print("Du har fått 1000 dollar fra organisasjonen.")
        time.sleep(1.5)
        print("Dersom du klarer å gamble deg til 2000 dollar, blir du sluppet fri.")
        time.sleep(3)

        while spiller.penger < 2000:
            if spiller.penger == 0:
                return spiller.dør()  # Spillet er over dersom spilleren taper alt
            print("\n\nDine penger: $" + str(spiller.penger))
            # Spør spilleren om hvor mye han vil vedde
            beløp = int(input("\nHvor mye vil du vedde? "))
            # Sjekker om spilleren har nok penger til å vedde dette beløpet
            if not spiller.vedd(beløp):
                continue
            spiller.hånd = [random.choice(
                self.kortstokk), random.choice(self.kortstokk)]  # Spilleren får utdelt to tilfeldige kort
            print("\nDu har fått utdelt: " + str(spiller.hånd))
            self.dealer_hånd = [random.choice(
                self.kortstokk), random.choice(self.kortstokk)]  # Dealeren får utdelt to tilfeldige kort
            print("Dealeren viser: " + str(self.dealer_hånd[0]))
            time.sleep(1)
            while True:
                valg = input(
                    "\nVil du ta (k)ort eller (s)tå? \n Dersom du trenger en forklaring på hvordan blackjack fungerer, skriv 'hjelp'.\n: ")  # Spør spilleren om hva han vil gjøre
                if valg == "k":
                    # Spilleren tar et nytt kort
                    spiller.hånd.append(random.choice(self.kortstokk))
                    print("\nDu har: " + str(spiller.hånd))
                    if sum(spiller.hånd) > 21:  # Sjekker om spilleren har gått over 21 poeng
                        print("\nDu har tapt spillet.\n")
                        time.sleep(1)
                        return spiller.dør()  # Spillet er over dersom spilleren taper
                elif valg == "s":
                    break
                else:
                    print("\n-----------------------\nHer er en kort forklaring: \n\n\nBlackjack starter med at spilleren og dealeren får utdelt to kort hver. \nKortene til dealeren er plassert på bordet, det ene kortet med bildesiden ned, og den andre med bildesiden opp. \nSpilleren skal velge om han ønsker å få flere kort eller å beholde kortene som er utdelt. \nNår dette er bestemt og spilleren er komfortabel med sine kort, snur dealeren det siste kortet på bordet og avslører vinneren. \n\nHer har du en kort oppsummering av noen Blackjack spilleregler: \n - A er verdt enten 11 eller 1.\n - Konge, dame og knekt er verdt 10\n - Tallkort har samme verdi som kortet. \n - Spilleren starter alltid med to kort. \n - Er kortene over 21 har du tapt. \n - Om dealeren får 17 eller høyere må han stå. \n - Spilleren kan vinne på flere måter: \n    1. 'Ekte blackjack': A + et bildekort som de to første kortene\n    2. Oppnå høyere hånd enn dealeren \n    3. Hvis spillerens hånd er under 21, mens dealerens går over.\n-----------------------")

                time.sleep(1)
            # Sjekker om dealeren må ta flere kort.
            while sum(self.dealer_hånd) < 17:
                self.dealer_hånd.append(random.choice(self.kortstokk))
            # Sjekker om dealeren har gått over 21.
            if sum(self.dealer_hånd) > 21:
                print("\nDealeren har tapt. Du vinner!")

                # Spilleren vinner dobbelt så mye som han veddet
                spiller.vinner(beløp * 2)
            # Sjekker om dealerens sum er høyere enn spillerens
            elif sum(spiller.hånd) > sum(self.dealer_hånd):
                print("\nDu vinner!")
                # Spilleren vinner dobbelt så mye som han veddet
                spiller.vinner(beløp * 2)
            elif sum(spiller.hånd) == sum(self.dealer_hånd):
                print("\nUavgjort.")
                spiller.vinner(beløp)
            else:
                print("\nDu taper.")
            time.sleep(1)
        return spiller.fri()  # Spillet er over dersom spilleren vinner spillet


def hovedprogram():
    """Definerer en funksjon hovedprogram som får spillet til å starte."""
    spiller = Spiller()
    spill = Blackjack()
    spill.spill(spiller)


hovedprogram()  # Starter spillet.
