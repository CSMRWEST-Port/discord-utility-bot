from random import randint

async def diceroll(diceType: str) -> int:
    match diceType:
        case "d4":
            return randint(1, 4)
        case "d6":
            return randint(1, 6)
        case "d10":
            return randint(1, 10)
        case "d20":
            return randint(1, 20)
        case _:
            return randint(1,4)