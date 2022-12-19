import time
import random as r

print(u"{}[2J{}[;H".format(chr(27), chr(27)))


# class Spiller:
#     def __init__(self, navn, balanse):
#         self.navn = navn
#         self.balanse(balanse)

#     def balanse(self, balanse):
#         self.new_method(balanse)

#     def new_method(self, balanse):
#         self.balanse = balanse

#     def visInfo(self):
#         return print(f"\n Hei {self.navn}. Du har {self.balanse} kroner å spille med.")


# spillernavn = input(str("Velg et navn: "))

# spiller = Spiller(spillernavn, 1000)

# spiller.visInfo()

# time.sleep(1)

# spiller_balanse = spiller.balanse


def myntkast():
    playing = True

    poeng = 0

    while playing == True:
        print("\n\nPrøv å gjett det riktige nummeret (fra 1 til 10).")
        nummer = r.randint(1, 10)
        time.sleep(0.5)
        valgtnummer = int(input("\n Skriv et nummer mellom 1 og 10 \n: "))
        time.sleep(0.5)
        print(f"\nDu valgte {valgtnummer}.")
        time.sleep(1)
        if valgtnummer == nummer:
            print(f"\nNummeret var {nummer}! Du vant!")
            poeng += 1

            time.sleep(1)
            print(f"\nDu har nå {poeng} poeng.")
            time.sleep(2)

        elif valgtnummer != nummer and valgtnummer in range(11):
            print(
                f"\nNummeret var {nummer}. Du tapte og mistet alle poengene.")
            poeng = 0

            time.sleep(1)
            print(f"\nDu har nå {poeng} poeng.")
            time.sleep(2)
        else:
            print(f"\nDu skrev ikke inn et nummer mellom 1 og 10. Prøv igjen.")
        myntigjen = input(f"\nVil du spille igjen? (Ja [J] eller Nei [N]\n: ")

        if myntigjen.lower() == "nei" or "n":
            break

        elif myntigjen.lower() != "ja" or myntigjen.lower() != "j" and myntigjen.lower() != "nei" or myntigjen.lower() != "n":
            time.sleep(1)
            print(f"Du skrev ikke enten ja eller nei.")

        else:
            print(f"Starter spillet på nytt ... ")


myntkast()


# def main():
#     while spiller_balanse > 0:
#         action = input(
#             "\n Hva vil du gjøre? \n(Skriv 'hjelp' eller 'h' for å få en liste av ting du kan gjøre) \n: ")

#         if action.lower() == "hjelp" or "h":
#             print("\n Ting du kan gjøre:")
#             print("- BJ: Spill blackjack")
#             print("- Q: Quit game\n")

#         if action.lower() == "bj" or "blackjack":
#             bet = input(
#                 f"Hvor mye vil du legge inn? \n   Du har {spiller_balanse} kroner.")
#         else:
#             break

#             # BLACKJACK

# time.sleep(1.5)

# main()
