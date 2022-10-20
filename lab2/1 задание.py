
def create(p, q):
    F = open(p, encoding="utf8")
    Names = []
    facts = {}
    for u in range(8):
        facts[str(u)] = []
    l = list((F.readline()[:-1]).split())
    i = 0
    while l != ['0']:
        Names.append(l[0] + ' ' + l[1])
        for t in range(2, 10):
            if int(l[t]):
                facts[str(t - 2)] = facts[str(t - 2)] + [i]
        l = list((F.readline()[:-1]).split())
        i += 1
    F.close()
    D = open(q, encoding="utf8")
    quess = [D.readline()[:-1] for k in range(8)]
    D.close()
    return Names, facts, quess


names, facts, quess = create('names.txt', 'ques.txt')


def mainn(facts, quess, names):
    j = int(input(quess[0] + "\n 1 - да, 0 - нет \n"))
    if j:
        act = facts['0']
    else:
        act = set(i for i in range(len(names)) if i not in facts['0'])

    m = 1
    while len(act) != 1:
        j = int(input(quess[m] + "\n 1 - да, 0 - нет \n"))
        if j:
            act = set(i for i in act if i in facts[str(m)])
        else:
            act = set(i for i in act if i not in facts[str(m)])
        m += 1
        if len(act) == 0:
            return 'Такого человека нет'
    return names[act.pop()]


print(mainn(facts, quess, names))