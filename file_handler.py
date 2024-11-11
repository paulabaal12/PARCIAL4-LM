from turing_machine import TuringMachine

# Metodo para cargar una maquina de turing desde un archivo de texto
def load_turing_machine_from_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()


    states = []
    input_alphabet = []
    tape_alphabet = []
    transitions = {}
    initial_state = None
    accept_state = None
    reject_state = None

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line == "# Estados" and i + 1 < len(lines):
            states = lines[i + 1].strip().split(',')
            i += 1
        elif line == "# Alfabeto de entrada" and i + 1 < len(lines):
            input_alphabet = lines[i + 1].strip().split(',')
            i += 1
        elif line == "# Alfabeto de la cinta" and i + 1 < len(lines):
            tape_alphabet = lines[i + 1].strip().split(',')
            i += 1
        elif line == "# Estado inicial" and i + 1 < len(lines):
            initial_state = lines[i + 1].strip()
            i += 1
        elif line == "# Estado de aceptación" and i + 1 < len(lines):
            accept_state = lines[i + 1].strip()
            i += 1
        elif line == "# Estado de rechazo" and i + 1 < len(lines):
            reject_state = lines[i + 1].strip()
            i += 1
        elif line == "# Transiciones":
            i += 1
            while i < len(lines) and "->" in lines[i]:
                transition_line = lines[i].strip()
                parts = transition_line.split(" -> ")
                if len(parts) == 2:
                    (current_state, read_symbol) = parts[0].split(',')
                    (new_state, write_symbol, direction) = parts[1].split(',')
                    transitions[(current_state, read_symbol)] = (new_state, write_symbol, direction)
                i += 1
            continue
        i += 1

    # Verificación final de la configuración
    if not states or not input_alphabet or not tape_alphabet or initial_state is None or accept_state is None or reject_state is None or not transitions:
        raise ValueError("Especificaciones incompletas en el archivo de texto")

    return TuringMachine(states, input_alphabet, tape_alphabet, transitions, initial_state, accept_state, reject_state)

# metodo para guardar las configuraciones en un archivo de texto
def save_configurations(filename, configurations):
    with open(filename, 'w') as file:
        for config in configurations:
            file.write(config + '\n')
