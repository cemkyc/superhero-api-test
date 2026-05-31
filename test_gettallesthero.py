from gettallesthero import (
    getTallestHero,
    hasWork,
    getHeightHaveSameCount,
)

def test_tallestMaleWithWork():
    hero = getTallestHero("Male", True)

    assert hero is not None
    assert hero["appearance"]["gender"] == "Male"
    assert hasWork(hero) is True

def test_tallestMaleWithoutWork():
    hero = getTallestHero("Male", False)

    assert hero is not None
    assert hero["appearance"]["gender"] == "Male"
    assert hasWork(hero) is False

def test_tallestFemaleWithWork():
    hero = getTallestHero("Female", True)

    assert hero is not None
    assert hero["appearance"]["gender"] == "Female"
    assert hasWork(hero) is True

def test_tallestFemaleWithoutWork():
    hero = getTallestHero("Female", False)

    assert hero is not None
    assert hero["appearance"]["gender"] == "Female"
    assert hasWork(hero) is False

def test_invalidGender():
    hero = getTallestHero("Robot", True)

    assert hero is None

def test_hasWorkTrue():
    hero = {
        "work": {
            "occupation": "Photographer"
        }
    }

    assert hasWork(hero) is True

def test_hasWorkFalse():
    hero = {
        "work": {
            "occupation": "-"
        }
    }

    assert hasWork(hero) is False

def test_hasWorkEmptyString():
    hero = {
        "work": {
            "occupation": ""
        }
    }

    assert hasWork(hero) is False

def test_heightEmpty():
    hero = {
        "appearance": {
            "height": ["-", "-"]
        }
    }

    assert getHeightHaveSameCount(hero) == 0

def test_heightCm():
    hero = {
        "appearance": {
            "height": ["5'7", "170 cm"]
        }
    }

    assert getHeightHaveSameCount(hero) == 170

def test_heightMeters():
    hero = {
        "appearance": {
            "height": ["1000", "304.8 meters"]
        }
    }

    assert getHeightHaveSameCount(hero) == 30480

def test_heightInvalidUnit():
    hero = {
        "appearance": {
            "height": ["-", "0 kg"]
        }
    }

    assert getHeightHaveSameCount(hero) == 0



