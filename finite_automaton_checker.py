def read_states():
    while True:
        try:
            num_states = int(input("- Number of states: "))
            if num_states < 1:
                print("Error: Number of states must be 1 or more.")
            else:
                states = [input(f"Enter the {i+1} state: ") for i in range(num_states)]
                return states
        except ValueError:
            print("Error: Please enter a valid integer for the number of states.")

def read_inputs():
    while True:
        try:
            num_inputs = int(input("\n- Number of inputs: "))
            if num_inputs < 1:
                print("Error: Number of inputs must be 1 or more.")
            else:
                inputs = [input(f"Enter the {i+1} input: ") for i in range(num_inputs)]
                return inputs
        except ValueError:
            print("Error: Please enter a valid integer for the number of inputs.")

def read_initial_state(states):
    while True:
        initial_state = input("\n- Enter the initial state: ")
        if initial_state in states:
            return initial_state
        else:
            print("Error: Initial state must be one of the entered states. Please try again.")

def read_final_states(states):
    while True:
        try:
            num_final_states = int(input("\n- Number of final states: "))
            if num_final_states < 1:
                print("Error: Number of final states must be 1 or more.")
            elif num_final_states > len(states):
                print("Error: Number of final states must be equal number of states or less.")
            else:
                final_states = [input(f"Enter the {i+1} final state: ") for i in range(num_final_states)]
                if all(state in states for state in final_states):
                    return final_states
                else:
                    print("Error: Final states must be among the entered states. Please try again.")
        except ValueError:
            print("Error: Please enter a valid integer for the number of final states.")

def read_fsm_table(states, inputs):
    fsm_table = {}
    for state in states:
        for inp in inputs:
            while True:
                next_state = input(f"{{{state}, {inp}}} = ")
                if next_state in states:
                    fsm_table[(state, inp)] = next_state
                    break
                else:
                    print("Error: Next state must be one of the entered states. Please try again.")
    return fsm_table

def print_fsm_table(states, inputs, fsm_table):
    print(f"{'δ':<5} {'|':<5} {' '.join(inputs):<10}")
    print("-----------------------------------------")

    for state in states:
        print(f"{state:<5} {'|':<5} {' '.join(fsm_table.get((state, inp), '') for inp in inputs):<10}")

def read_string():
        while True:
            user_input = input("\nEnter a string or type 'exit' to stop the program or enter 'again' to run the program again: ")

            if user_input.lower() == 'exit':
                exit()
            elif user_input.lower() == 'again':
                break
            
            if is_string_acceptable(fsm_table, initial_state, final_states, user_input):
                print("The string is acceptable for the Finite Automaton.")
            else:
                print("The string is not acceptable for the Finite Automaton.")

def is_string_acceptable(fsm_table, initial_state, final_states, input_string):
    current_state = initial_state

    for char in input_string:
        if (current_state, char) in fsm_table:
            current_state = fsm_table[(current_state, char)]
        else:
            return False

    return current_state in final_states

if __name__ == "__main__":
    while True:
        states = read_states()
        inputs = read_inputs()
        initial_state = read_initial_state(states)
        final_states = read_final_states(states)
        fsm_table = read_fsm_table(states, inputs)
        print_fsm_table(states, inputs, fsm_table)
        read_string()