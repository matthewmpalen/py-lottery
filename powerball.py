from decimal import Decimal
import random

JACKPOT = 1400000000
JACKPOT_PROB = Decimal(1/292201338)
WHITE_MIN = 1
WHITE_MAX = 69
RED_MIN = 1
RED_MAX = 26
TICKET_COST = 2
POWERPLAY = True
if POWERPLAY:
    TICKET_COST += 1

white_balls = tuple(range(WHITE_MIN, WHITE_MAX + 1))
powerballs = tuple(range(RED_MIN, RED_MAX + 1))

winning_white_balls = (5, 17, 33, 35, 61)
winning_powerball = 22

prize_map = {
    # No Powerball
    (0, False): 0, 
    (1, False): 0, 
    (2, False): 0, 
    (3, False): 7, 
    (4, False): 100, 
    (5, False): 1000000, 
    # With Powerball
    (0, True): 4, 
    (1, True): 4, 
    (2, True): 7, 
    (3, True): 100, 
    (4, True): 50000, 
    (5, True): JACKPOT
}

def get_prize(white_balls, powerball):
    white_matched = sum(1 for ball in white_balls if ball in winning_white_balls)
    powerball_matched = powerball == winning_powerball
    return prize_map[(white_matched, powerball_matched)]

def main():
    expected_value = JACKPOT_PROB * JACKPOT
    print('Current EV: {0}, Play: {1}'.format(expected_value, 
        expected_value > 0))
    prize = 0
    ticket_count = 0

    while prize != JACKPOT:
        ticket_count += 1
        chosen_white_balls = random.sample(white_balls, 5)
        chosen_powerball = random.choice(powerballs)

        prize = get_prize(chosen_white_balls, chosen_powerball)
        if ticket_count % 1000000 == 0:
            print('Attempt {0}'.format(ticket_count))

    total_cost = ticket_count * TICKET_COST

    print('Winning Numbers: {0} + {1}'.format(winning_white_balls, 
        winning_powerball))
    print('Attempts: {0}, Prize: {1}, Cost: {2}, Net: {3}'.format(ticket_count, 
        JACKPOT, total_cost, JACKPOT - total_cost))

if __name__ == '__main__':
    main()
