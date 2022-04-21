import random

stimulation_count = 100000
dice = [1, 2, 3, 4, 5, 6]


def main():
    dice_count = int(input("Number of dice: "))
    dice_face = int(input("Dice face: "))
    dice_face_number = int(input("Number of face: "))
    existing_dice_faces = [
        int(i.strip() if i.strip() != "" else "0")
        for i in input("Known Dice faces (CSV): ").split(',')
    ]
    existing_dice_faces = list(filter((0).__ne__, existing_dice_faces))

    p = mcs(dice_count, dice_face, dice_face_number, existing_dice_faces)

    print("- ", end="")
    if p >= 0.9:
        print("Good Bet")
    elif p >= 0.65:
        print("Fair Bet")
    elif p >= 0.5:
        print("50/50")
    elif p >= 0.4:
        print("Risky Bet")
    else:
        print("Bad Bet")

    print(f"- Probability: {p}")


def mcs(dice_count, dice_face, dice_face_number, known_dice_face):
    success = 0
    for i in range(stimulation_count):
        r = known_dice_face.copy()
        for j in range(dice_count - len(known_dice_face)):
            r.append(random.choice(dice))

        if dice_face == 6 and r.count(dice_face) >= dice_face_number:
            success += 1
        elif dice_face != 6 and (r.count(dice_face) + r.count(6)) >= dice_face_number:
            success += 1

    return success / stimulation_count


if __name__ == '__main__':
    print(
        '''
        $$$$$$$\  $$\            $$$$$$\   $$$$$$\  
        $$  __$$\ $$ |          $$  __$$\ $$  __$$\ 
        $$ |  $$ |$$ |$$\   $$\ $$ /  \__|$$ /  \__|
        $$$$$$$\ |$$ |$$ |  $$ |$$$$\     $$$$\     
        $$  __$$\ $$ |$$ |  $$ |$$  _|    $$  _|    
        $$ |  $$ |$$ |$$ |  $$ |$$ |      $$ |      
        $$$$$$$  |$$ |\$$$$$$  |$$ |      $$ |      
        \_______/ \__| \______/ \__|      \__|      
        '''
    )
    print("        Cheating with comp sci :)\n")
    print("Enter 6 for wildcard dice")

    while True:
        print("***********************************")
        main()
