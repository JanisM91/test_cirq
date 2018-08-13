#Creates and simulates a circuit consisting out of CNotGates and measurements
import cirq

def main():
    # Pick a qubit.
    q0 = cirq.GridQubit(0, 0)
    q1 = cirq.GridQubit(0, 1)
    
    q2 = cirq.GridQubit(1, 0)
    q3 = cirq.GridQubit(1, 1)
    
    CNot = cirq.CNotGate()

    # Create a circuit
    circuit = cirq.Circuit.from_ops(
        CNot(q0,q1),
        cirq.measure(q0, key='q0'),
        cirq.measure(q1, key='q1'),
        
        cirq.X(q2),
        CNot(q2,q3),
        cirq.measure(q2, key='q2'),
        cirq.measure(q3, key='q3')
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
