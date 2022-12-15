from random import randrange
print(u"{}[2J{}[;H".format(chr(27), chr(27)))


def blackjack():
    print_intro()
    player_win, dealer_win, game = play_multiple_game()
    final_result(player_win, dealer_win, game)


def print_intro():
    print("------ Velkommen til Blackjack ! -----")
    print("   Blackjack er et kasinospill som spilles med kort. \n   Målet med spillet er å trekke kort som i sum blir så nærme 21 som mulig. \n   Dersom du får over 21, 'buster' du. \n   Alle bildekort teller som 10 poeng. \n   'A' teller 1 eller 11 poeng. \n   Alle andre kort tilsvarer deres numeriske verdi. \n   ")
    print("Først er det din tur:")
    return None


def play_multiple_game():
    player_win = 0
    dealer_win = 0
    game = 0
    play_again = "yes"
    # Ask user whether continue another game or stop
    # Condition True, if user want to play.
    while (play_again[0] == "y" or play_again[0] == "Y"):
        player_hand = player_turn()
        dealer_hand = dealer_turn()
        player_score, dealer_score = compare_between(player_hand, dealer_hand)
        result_of_this_game(player_hand, dealer_hand)
        if (player_score > dealer_score):
            print("\nPlayer win!")
            player_win += 1

        elif (dealer_score > player_score):
            print("\nDealer win!")
            dealer_win += 1

        else:
            print("\nThis game end in a tie!")
            player_win == dealer_win
        game += 1
        play_again = input("\nDo you want to continue (Y or N)? ")
    return player_win, dealer_win, game


def player_turn():
    hand = []
    ans = "hit"
    hand.append(take_card())
    # Ask user whether Hit or Stand?
    # Condition True, if user want to Hit.
    while (ans[0] == "h" or ans[0] == "H"):
        hand.append(take_card())
        hand = eval_ace(hand)
        print("\nYour hand: {0} total = {1}".format(hand, sum(hand)))
        if (is_bust(hand) or
                is_blackjack(hand)):
            break
        ans = input("Do you want to Hit or Stand (H or S)?")
    return hand


def take_card():
    # get arbitrary card from 2 to 11.
    shuffle_card = randrange(2, 11 + 1)
    return shuffle_card


def eval_ace(hand):
    # Determine Ace = 1 or 11, relying on total hand.
    total = sum(hand)
    for ace in hand:
        if (ace == 11 and total > 21):
            # at position, where Ace == 11, replace by Ace == 1.
            position_ace = hand.index(11)
            hand[position_ace] = 1
    return hand


def is_bust(hand):
    # Condition True: if the hand of player (or dealer) > 21.
    total = sum(hand)
    if total > 21:
        return True
    return None


def is_blackjack(hand):
    # Condition True: if the hand of player (or dealer) == 21.
    total = sum(hand)
    if total == 21:
        return True
    return None


def dealer_turn():
    hand = []
    while sum(hand) < 18:
        hand.append(take_card())
        hand = eval_ace(hand)
    return hand


def compare_between(player, dealer):
    total_player = sum(player)
    total_dealer = sum(dealer)
    player_bust = is_bust(player)
    dealer_bust = is_bust(dealer)
    player_blackjack = is_blackjack(player)
    dearler_blackjack = is_blackjack(dealer)
    player_score = 0
    dealer_score = 0
    # when player (dealer) is_bust.
    if player_bust:
        if (not dearler_blackjack and
                total_dealer < 21):
            dealer_score += 1
    if dealer_bust:
        if (not player_blackjack and
                total_player < 21):
            player_score += 1
    if (player_bust and
            dealer_bust):
        if (total_player > total_dealer):
            player_score += 1
        elif (total_dealer > total_player):
            dealer_score += 1
        else:
            player_score == dealer_score
    # when player (dealer) get blackjack.
    if player_blackjack:
        player_score += 1
    if dearler_blackjack:
        dealer_score += 1
    if (player_blackjack and
            dearler_blackjack):
        player_score == dealer_score
    # when total hand of player (dealer) < 21.
    if (total_player < 21 and
            total_dealer < 21):
        if (total_player > total_dealer):
            player_score += 1
        elif (total_dealer > total_player):
            dealer_score += 1
        else:
            player_score == dealer_score
    return player_score, dealer_score


def result_of_this_game(player_hand, dealer_hand):
    print("\nWe have the result: ")
    print("Player has: {0} total = {1}".format(
        player_hand, sum(player_hand)))
    print("Dealer has: {0} total = {1}".format(
        dealer_hand, sum(dealer_hand)))
    return None


def final_result(player_win, dealer_win, game):
    print("\nThe Final after {} games:".format(game))
    print("player: {} | dealer: {}".format(
        player_win, dealer_win))
    return None


blackjack()
