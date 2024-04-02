import card

look_up_table = {}

def calc_hand_values(card_list: list[card.card]):
    if len(card_list)!=7:
        raise Exception("the number of cards should be 7")
    result = 1
    for i in card_list:
        result*=i
    return look_up_table[result]

if __name__ == "__main__":
# do something