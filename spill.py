class Spiller:
    def __init__(self, navn, balanse, ):
        self.navn = navn
        self.balanse = balanse

    def visInfo(self):
        return print(f"\nNavnet på spilleren er {self.navn}, og har {self.balanse} kroner")


class Spill:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


spiller = Spiller(input(str("Skriv navn: ")), 1000)


def main():
    while spiller.balanse > 0:
        action = input(
            "\n Hva vil du gjøre? \n(Skriv 'hjelp' for å få en liste av ting du kan gjøre) \n: ")

        if action.lower() == "hjelp":
            print("\n Ting du kan gjøre:")
            print("- G: Gå en annen plass.")
            print("- Q: Quit game\n")

        if action.lower() == "Q":
            print("Du har valgt å slutte å spille.")


spiller.visInfo()


main()


# def main():
#     player = Spiller("Spiller", 100)

#     # Main game loop
#     while player.balance > 0:
#         # Prompt the player for an action
#         action = input(
#             "\nWhat would you like to do? \n(Skriv 'hjelp' for å få en liste av ting du kan gjøre. \n: ")

#         # Process the player's action
#         if action.lower() == "hjelp":
#             print("\n Ting du kan gjøre:")
#             print("- A: Gjett nummeret")
#             print("- Q: Quit game\n")


# main()
