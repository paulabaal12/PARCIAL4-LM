def log_configurations(configurations, output_filename):
    with open(output_filename, 'w') as file:
        for config in configurations:
            file.write(config + '\n')
