import cube
import gui

if __name__ == "__main__":

    rubiks_cube = cube.Cube(3)
    rubiks_cube.rotation("U")
    
    move = ""

    instructions = """Welcome to Rubik's cube v 0.0.1
    
    Only runs a 3x3x3 for now and your available moves are:
    L, L', R, R', U, U', D, D', B, B', F, F'
    
    They can be entered one at a time or as a sequence in the form:
    [move] [another move] [and another one] ...

    Enter "E" to exit
    """

    print(instructions)

    run = True
    while run:

        # Temporary representation
        rubiks_cube._draw()

        """
        gui.draw takes a list of every cube's coordinates and colors tuples.
        Comment the temp. representation and uncomment the following line once gui.draw is completed.
        """
        gui.draw(rubiks_cube.getCube())

        move_sequence = input("Next move(s): ")
        print("\n")

        move_list = move_sequence.split(" ")

# Will do for now but would need to check if all the moves are valid before actually doing them
        for move in move_list:
            if move == "E": # Exit condition
                run = False
                break # Skip the rest of the moves
            try: 
                rubiks_cube.rotation(move)
            except ValueError:
                print("Invalid Move " + move)
                print(instructions)
        