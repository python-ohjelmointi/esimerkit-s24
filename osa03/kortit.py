# test card numbers from
# https://docs.adyen.com/development-resources/testing/test-card-numbers/

visa = "4646 4646 4646 4644"
mastercard = "5555 5555 5555 4444"

kortti = visa

# mastercardilla on kaksi lukuväliä korttinumeroiden alussa
is_mastercard = (2221 <= int(kortti[0:4]) <= 2720) or \
    (51 <= int(kortti[0:2]) <= 55)

# jos kortti alkaa numerolla 4, se on visa
is_visa = kortti.startswith("4")

if is_visa:
    print("visa")

elif is_mastercard:
    print("mastercard")

else:
    print('unkown')
