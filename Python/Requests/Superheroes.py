import requests


superheroes = {'Hulk': 332,
               'Captain America': 149,
               'Thanos': 655}


max_int = 0
for key, val in superheroes.items():
    res = requests.get(f'https://superheroapi.com/api/2619421814940190/{val}')
    if res.status_code == 200:
        intelligence = int(res.json()["powerstats"]["intelligence"])
        print(f'{key}, имеет интеллект равный {intelligence}')
        if intelligence > max_int:
            max_int = intelligence
            hero = key


if __name__ == '__main__':
    print(f'{hero} самый умный!')
