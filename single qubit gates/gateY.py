#Creates and simulates a circuit consisting out of YGates and measurements
import cirq

def main():
    # Pick a qubit.
    q0 = cirq.GridQubit(0, 0)
    q1 = cirq.GridQubit(0, 1)
    q2 = cirq.GridQubit(0, 2)

    # Create a circuit
    circuit = cirq.Circuit.from_ops(
        cirq.Y(q0),
        cirq.measure(q0, key='m0'),
        
        cirq.Y(q1),        
        cirq.Y(q1),
        cirq.measure(q1, key='m1'),
        
        cirq.Y(q2),        
        cirq.Y(q2),
        cirq.Y(q2),
        cirq.measure(q2, key='m2'),
    )
    print("Circuit:")
    print(circuit)

   # Simulate the circuit 50 times.
    simulator = cirq.google.XmonSimulator()
    result = simulator.run(circuit, repetitions=50)
    print("Results  of simulation:")
    print(result)
    
    # Run the simulator with direct access to the wave function of the quantum processor
    resultw = simulator.simulate(circuit)   
    print("Result from wave function:")
    print(resultw)


if __name__ == '__main__':
    main()
