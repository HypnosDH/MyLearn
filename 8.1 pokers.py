suits = [u"\u2664", u"\u2661", u"\u2662", u"\u2667"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
pokers = [(i, j) for i in suits for j in ranks]
print(pokers)