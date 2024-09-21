N, M = map(int, input().split(' '))

pokemon_dict = {}

for i in range(N):
    pokemon = input()
    pokemon_dict[str(i+1)] = pokemon
    pokemon_dict[pokemon] = str(i + 1)

for i in range(M):
    print(pokemon_dict[input()])