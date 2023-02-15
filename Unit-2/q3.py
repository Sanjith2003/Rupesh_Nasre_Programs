price = int(input('Price: '))
denominations = list(map(int, input('Denominations: ').split()))
num_notes = list(map(int, input('Number of notes for each denomination: ').split()))

# check if there are enough notes for each denomination
if len(denominations) != len(num_notes):
    print('Error: number of denominations and number of notes must match.')
else:
    print("Can you form", price, "exactly using", denominations, "?")
    sum = 0
    for i in range(len(denominations)):
        sum += denominations[i] * num_notes[i]
    if sum < price:
        print('No, there are not enough notes to form the required amount.')
    else:
        for i in range(len(denominations)):
            if num_notes[i] * denominations[i] >= price:
                # we have enough notes of this denomination to form the required amount
                num_used = price // denominations[i]
                print('Use', num_used, 'notes of denomination', denominations[i])
                break
            else:
                # use as many notes of this denomination as possible and move on to the next denomination
                num_used = num_notes[i]
                print('Use', num_used, 'notes of denomination', denominations[i])
                price -= num_used * denominations[i]
        if price > 0:
            print('There are not enough notes to form the required amount.')
