import pandas

def vanfelix():
    return "dit komt van felix"


def zoekpokemon(naam):
    df = pandas.read_csv("Pokemon.csv")
    for pok in df["Name"]:
        if pok == naam:
            return naam + "?, ja gevonden"
    return naam + "?, nee niet gevonden"


