import cube

if __name__ == "__main__":

    rubiks_cube = cube.Cube(3)
    
    move = ""

    print("""Welcome to Rubik's cube v 0.0.1
    
    Only runs a 3x3x3 for now and your available moves are:
    L, L', R, R', U, U', D, D', B, B', F, F'
    
    They can be entered one at a time or as a sequence in the form:
    [move] [another move] [and another one] ...
    
    """)

    run = True
    while run:

        rubiks_cube.draw()

        move_sequence = input("Next move(s): ")
        print("\n")

        move_list = move_sequence.split(" ")

# Will do for now but would need to check if all the moves are valid before actually doing them
        for move in move_list:
            rubiks_cube.rotation(move)
        