
def house_robber_suboptimal_dp(values):
    pass

def house_robber_optimal(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]

    m1 = m2 = values[0]
    for i in range(1, len(values)):
        m1, m2 = m2, max(m1 + values[i], m2)
    return m2

print(house_robber_optimal([2,4,6,2,5]))