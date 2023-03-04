# задание 1
import requests


def super_hero_intelligence():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    r = requests.get(url)
    list_json = r.json()
    the_smartest_hero = None
    heroes = ['Hulk', 'Captain America', 'Thanos']
    for hero in heroes:
        for elem in list_json:
            if elem['name'] == hero:
                if the_smartest_hero is None:
                    the_smartest_hero = (elem['name'], int(elem['powerstats']['intelligence']))
                else:
                    if the_smartest_hero[1] < elem['powerstats']['intelligence']:
                        the_smartest_hero = (elem['name'], int(elem['powerstats']['intelligence']))
    print('Самый умный супергерой:', the_smartest_hero[0])


if __name__ == '__main__':
    super_hero_intelligence()

