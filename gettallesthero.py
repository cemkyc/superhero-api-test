import json
from pathlib import Path

HeroPath = Path(__file__).resolve().parent / "api" / "all.json"

with open(HeroPath, 'r', encoding='utf-8' ) as f:
    Heroes= json.load(f)

# проверяем есть ли работа
def hasWork(hero):
    occup = hero["work"]["occupation"]
    workStatus = (occup != "-" and bool(occup.strip()))
    return workStatus

# приводим все велечины роста к одной системе исчисления
def getHeightHaveSameCount(hero):
    height = hero["appearance"]["height"][1].split()
    if "cm" in height:
        return float(height[0])
    if "meters" in height:
        return float(height[0]) * 100
    # print(hero["name"], "Wrong parametr")
    return 0

# НАходим высокого самого героя
def getTallestHero(gender, workStatus):
    heroesFiltered = []
    for hero in Heroes:
        if hero["appearance"]["gender"] == gender and hasWork(hero) == workStatus:
            heroesFiltered.append(hero)
    if not heroesFiltered:
        return None
    return max(heroesFiltered, key=getHeightHaveSameCount)