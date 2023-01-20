def decompose_amount(amount):
    notes = [100, 50, 10]
    coins = [2, 1]
    decomposition = {}
    for note in notes:
        decomposition[note] = amount // note
        amount = amount % note
    for coin in coins:
        decomposition[coin] = amount // coin
        amount = amount % coin
    return decomposition

amount = int(input("Enter le montant: "))

result = decompose_amount(amount)

print(f"{amount} euros, c'est donc", end=' ')
for note in [100, 50, 10]:
    if result[note] > 0:
        print(f"{result[note]} billets de {note}", end=', ')
for coin in [2, 1]:
    if result[coin] > 0:
        print(f"{result[coin]} pièces de {coin}", end=' ')
