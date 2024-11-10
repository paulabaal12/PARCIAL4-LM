from turing_machine import TuringMachine
from file_handler import load_turing_machine_from_txt, save_configurations

def main():
    # Lista de casos de prueba
    test_cases = [
        ('input_accept.txt', 'output_accept.txt'),
        ('input_reject.txt', 'output_reject.txt'),
        ('input_infinite.txt', 'output_infinite.txt')
    ]
    
    for input_file, output_file in test_cases:
        print(f"Ejecutando prueba con {input_file}")
        # Cargar la máquina de Turing desde el archivo de texto
        machine = load_turing_machine_from_txt('machine_definition.txt')
        
        # Cargar la cadena de entrada
        with open(input_file, 'r') as f:
            input_string = f.read().strip()
        
        machine.load_tape(input_string)
        
        # Ejecutar la simulación y guardar configuraciones
        configurations = machine.run()
        save_configurations(output_file, configurations)
        print(f"Resultados guardados en {output_file}\n")

if __name__ == "__main__":
    main()
