#Creates and simulates a circuit consisting out of SwapGates and measurements
import cirq

def main():
    # Pick a qubit.
    q0 = cirq.GridQubit(0, 0)
    q1 = cirq.GridQubit(0, 1)
    
    q2 = cirq.GridQubit(1, 0)
    q3 = cirq.GridQubit(1, 1)
    
    q4 = cirq.GridQubit(2, 0)
    q5 = cirq.GridQubit(2, 1)
    
    Swap = cirq.SwapGate()

    # Create a circuit
    circuit = cirq.Circuit.from_ops(
    
        cirq.measure(q0, key='q0 before swap'),
        cirq.measure(q1, key='q1 before swap'),
        Swap(q0,q1),
        cirq.measure(q0, key='q0 after swap'),
        cirq.measure(q1, key='q1 after swap'),
        
        cirq.X(q2),        
        cirq.measure(q2, key='q2 before swap'),
        cirq.measure(q3, key='q3 before swap'),
        Swap(q2,q3),
        cirq.measure(q2, key='q2 after swap'),
        cirq.measure(q3, key='q3 after swap'),
        
        cirq.X(q5),        
        cirq.measure(q4, key='q4 before swap'),
        cirq.measure(q5, key='q5 before swap'),
        Swap(q4,q5),
        cirq.measure(q4, key='q4 after swap'),
        cirq.measure(q5, key='q5 after swap')
    )
    print("Circuit:")
    print(circuit)

    # Simulate the circuit 50 times.
    simulator = cirq.google.XmonSimulator()
    result = simulator.run(circuit, repetitions=50)
    print("Results of simulation:")
    print(result)
    
    # Run the simulator with direct access to the wave function of the quantum processor
    resultw = simulator.simulate(circuit)   
    print("Result from wave function:")
    print(resultw)

if __name__ == '__main__':
    main()
