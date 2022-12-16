#  obhod v glubinu


def glub(graph, start, visited=None):
    if visited is None:
        visited = []
    elif start not in visited:
        visited.append(start)

    print(start)

    for n in graph[start]:
        if n not in visited:
            glub(graph, n, visited)
    return visited


def glub2(graph, start, x, visited=None, route=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)

    # print(start)
    if route is None:
        route = []
    route.append(start)

    if start == x:
        print(route)
    else:
        for n in graph[start]:
            if n not in visited:
                glub2(graph, n, x, visited, route)
                route.pop(len(route) - 1)
        return visited


gr = {'0': ['1', '2', '3'],
      '1': ['0', '2'],
      '2': ['0', '1', '4'],
      '3': ['0'],
      '4': ['2']}

life = {'Жизнь': ['Животные', 'Растения'],
        'Животные': ['Млекопитающие', 'Земноводные'],
        'Растения': ['Хвойные', 'Цветковые'],
        'Млекопитающие': ['Хищные', 'Хоботные', 'Парнокопытные'],
        'Земноводные': ['Безхвостые', 'Хвостатые'],
        'Цветковые': ['Розиды', 'Астериды'],
        'Розиды': ['Роза', 'Пион'],
        'Роза': [], 'Пион': [],
        'Астериды': ['Колокольчик'],
        'Колокольчик': [],
        'Безхвостые': ['Лягушка', 'Жаба'],
        'Лягушка': [], 'Жаба': [],
        'Хвостатые': ['Саламандра'],
        'Саламандра': [],
        'Хвойные': ['Сосновые', 'Тисовые'],
        'Сосновые': ['Пихта', 'Ель', 'Кедр', 'Сосна'],
        'Пихта': [], 'Ель': [], 'Кедр': [], 'Сосна': [],
        'Тисовые': ['Тис'],
        'Тис': [],
        'Хищные': ['Волк', 'Рысь', 'Лиса', 'Медведь', 'Тигр'],
        'Волк': [], 'Рысь': [], 'Лиса': [], 'Медведь': [], 'Тигр': [],
        'Хоботные': ['Слон', 'Муравьед'],
        'Слон': [], 'Муравьед': [],
        'Парнокопытные': ['Жираф', 'Конь', 'Верблюд', 'Бегемот'],
        'Жираф': [], 'Конь': [], 'Верблюд': [], 'Бегемот': []}


# glub(gr, '0')
glub2(life, 'Жизнь', 'Сосна')
