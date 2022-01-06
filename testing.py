from Game_of_life import render
from Game_of_life import next_board_state
from Game_of_life import next_state

init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

next_s1 = next_board_state(init_state1)

if next_s1 == expected_next_state1:
    print("Passed")
    print("Expected:", expected_next_state1)
    print("Rendered:", next_s1)
else:
    print("Failed")
    print("Expected:", expected_next_state1)
    print("Rendered:", next_s1)

init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]

expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]

next_s2 =  next_board_state(init_state2)

if next_s2 == expected_next_state2:
    print("Passed")
    print("Expected:", expected_next_state2)
    print("Rendered:", next_s2)
else:
    print("Failed")
    print("Expected:", expected_next_state2)
    print("Rendered:", next_s2)




