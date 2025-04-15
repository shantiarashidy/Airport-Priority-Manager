# Airport Priority Manager

## About
The **Airport Priority Manager** is a Python program designed to simulate and manage the priority of airplanes landing at an airport. The program calculates the priority of each airplane based on several factors, including the level of emergency, remaining fuel, and time. By using a **max-heap** (priority queue), the program efficiently processes airplanes and determines which plane should land first.

This system can be particularly useful for airport control towers to make informed decisions during emergency situations, ensuring that airplanes with the highest priority are handled first.

## Features
- **Priority Calculation**: Each airplane’s priority is determined by its emergency level, remaining fuel, and the time it has been waiting.
- **Efficient Sorting**: The program uses a heap-based priority queue to process planes in order of their urgency.
- **Customizable Input**: You can easily add new airplanes with varying priorities based on emergency, fuel, and time.
- **Clear Output**: Detailed information about each airplane, including its flight number, emergency level, fuel level, time waiting, and priority, is displayed.

## Installation
To get started with the **Airport Priority Manager**, you'll need to have Python installed on your machine.

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/shantiarashidy/airport-priority-manager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd airport-priority-manager
    ```


## Usage
To use the **Airport Priority Manager**:

1. Ensure that your Python environment is properly set up.
2. Run the Python script:
    ```bash
    python airport_priority_manager.py
    ```

The program will process the airplanes based on their priority and print the sorted list, showing which airplane should land first.

## Example Output
```text
Processing airplanes with details:
Flight: GN-SH-004, Emergency: 1, Fuel: 10, Time: 20, Priority: 101.01
Flight: GN-MH-001, Emergency: 1, Fuel: 20, Time: 30, Priority: 45.13
Flight: GN-ES-003, Emergency: 0, Fuel: 15, Time: 45, Priority: 20.19
Flight: GN-TH-002, Emergency: 0, Fuel: 50, Time: 60, Priority: 10.17
