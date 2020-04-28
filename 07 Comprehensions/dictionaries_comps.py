# Demonstrate how to use dictionary comprehensions


def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # TODO: Use a comprehension to build a dictionary, converts into degress F and any less than 100F
    tempDict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])

    # TODO: Merge two dictionaries with a comprehension
    # Key: LastName Value: JerseyNumber
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    # Merge them into one team, avoid anything more complex than this, if you need more items turn that into a Function
    newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)


if __name__ == "__main__":
    main()
