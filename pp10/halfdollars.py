#uzywamy list do przechowywania wiadomości o wyptodukowanyh monetach

denver = [1_700_000, 4_600_000, 2_100_000]

philadelphia = []

philadelphia.append(1_800_000)
philadelphia.append(5_000_000)
philadelphia.append(2_500_000)

total = [0, 0, 0]

total[0] = philadelphia[0] + denver[0]
total[1] = philadelphia[1] + denver[1]
total[2] = philadelphia[2] + denver[2]

average = (total[0] + total[1] + total[2]) / len(total)


print(denver)
print(philadelphia)
print(total)
print(average)