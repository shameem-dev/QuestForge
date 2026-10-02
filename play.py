from domain.character import Character


if __name__ == "__main__":
    P1 = Character("P1", 100 , 5)
    P2 = Character("P2",  100,  10)
    P3 = Character("P3",  100,  15)
    P4 = Character("P4",  100,  20)

    print(P1.describe())
    print(P2.describe())
    print(P3.describe())
    print(P4.describe())


    P1.attack(P3)
    P3.attack(P2)
    P2.attack(P4)
    P4.attack(P2)

    print(P1.describe())
    print(P2.describe())
    print(P3.describe())
    print(P4.describe())





    