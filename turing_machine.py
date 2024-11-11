class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transitions, initial_state, accept_state, reject_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tape = []
        self.head_position = 0 #Posición de la cabeza de lectura/escritura

    # Metodo para cargar la cinta con la cadena de entrada
    def load_tape(self, input_string):
        # Verificar que todos los caracteres de la cinta estén en el alfabeto de entrada
        for symbol in input_string:
            if symbol not in self.tape_alphabet:
                raise ValueError(f"Símbolo '{symbol}' en la entrada no está en el alfabeto de la cinta.")
        self.tape = list(input_string) + ['_']  # Cambiar ' ' por '_'
        self.head_position = 0

    # Metodo para ejecutar un paso de la maquina de Turing
    def step(self):
        current_symbol = self.tape[self.head_position]
        # Verificar si hay una transicion definida para el estado actual y el símbolo actual
        if (self.current_state, current_symbol) in self.transitions:
            new_state, new_symbol, direction = self.transitions[(self.current_state, current_symbol)]
            self.tape[self.head_position] = new_symbol
            self.current_state = new_state
            if direction == 'R':
                self.head_position += 1
                if self.head_position >= len(self.tape):
                    self.tape.append('_')  # Añadir símbolo blanco si es necesario
            elif direction == 'L':
                if self.head_position > 0:
                    self.head_position -= 1
                else:
                    # Si intentamos movernos a la izquierda de la posición 0, mantenemos la posición
                    pass
        else:
            print(f"No se encontró transición para el estado '{self.current_state}' y símbolo '{current_symbol}'")
            raise ValueError("Transición no definida para el estado actual y símbolo")

    # Metodo para ejecutar la maquina de Turing
    def run(self, max_steps=1000):
        configurations = []
        steps = 0
        # Ejecutar la máquina de Turing hasta que llegue a un estado de aceptación o rechazo
        while self.current_state not in {self.accept_state, self.reject_state}:
            configurations.append(self.get_configuration())
            self.step()
            steps += 1
            if steps >= max_steps:
                print("La máquina ha superado el número máximo de pasos y probablemente está en un ciclo infinito.")
                break
        else:
            configurations.append(self.get_configuration())
            # Indicar si la cadena es aceptada o rechazada
            if self.current_state == self.accept_state:
                print("Cadena aceptada.")
            elif self.current_state == self.reject_state:
                print("Cadena rechazada.")
        return configurations

    # obtener la configuración actual de la maquina de Turing
    def get_configuration(self):
        # Obtener u y v
        u = ''.join(self.tape[:self.head_position])
        v = ''.join(self.tape[self.head_position:])
        # Estado actual
        q = self.current_state
        # Formato de la configuración: u q v
        return f"{u}{q}{v}"

