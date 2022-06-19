# inputString = "S -> Sa / Sb / c / d".replace(" ", "")
# producer, productionStr = inputString.split('->')
# productions = productionStr.split('/')
# newProductions = [f"{production}{producer}'" for production in productions if production[0] != producer]
# newSubProductions = [f"{production[1:]}{producer}'" for production in productions if production[0] == producer] + ["ε"]
# print(f"{producer}->{'/'.join(newProductions)}" + '\n' + f"{producer}'->{'/'.join(newSubProductions)}")


def left_remove(inputString:str):
    inputString = inputString.replace(" ","")
    producer , productionStr = inputString.split("->")
    productions = productionStr.split("/")

    new_Productions= [
        f"{production}{producer}'"
        for production in productions if production[0] != producer
    ]

    newSubProductions = [
        f"{production[1:]}{producer}'"
        for production in productions if production[0] == producer
    ] + ["E"]
    return producer , new_Productions , newSubProductions

if __name__ == "__main__":
    inputString = input("Input Grammar : ")
    producer,newProductions , newSubProductions = left_remove(inputString)
    print(f"{producer} -> {'/'.join(newProductions)}")
    print(f"{producer} -> {'/'.join(newSubProductions)}")