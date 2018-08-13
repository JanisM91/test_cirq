#Creates and simulates a circuit consisting out of ToffoliGates (CCNOT) and measurements
import cirq

def main():
    # Pick a qubit.
    q0 = cirq.GridQubit(0, 0)
    q1 = cirq.GridQubit(0, 1)
    q2 = cirq.GridQubit(0, 2)
    
    q3 = cirq.GridQubit(1, 0)
    q4 = cirq.GridQubit(1, 1)
    q5 = cirq.GridQubit(1, 2)
    
    q6 = cirq.GridQubit(2, 0)
    q7 = cirq.GridQubit(2, 1)
    q8 = cirq.GridQubit(2, 2)
    
    q9 = cirq.GridQubit(3, 0)
    q10 = cirq.GridQubit(3, 1)
    q11 = cirq.GridQubit(3, 2)
    
    q12 = cirq.GridQubit(4, 0)
    q13 = cirq.GridQubit(4, 1)
    q14 = cirq.GridQubit(4, 2)
    

    # Create a circuit
    circuit = cirq.Circuit.from_ops(
    
		cirq.TOFFOLI(q0,q1,q2),
        cirq.measure(q0, key='q0'),
        cirq.measure(q1, key='q1'),
        cirq.measure(q2, key='q2'),
        
        cirq.X(q3),
        cirq.TOFFOLI(q3,q4,q5),
        cirq.measure(q3, key='q3'),
        cirq.measure(q4, key='q4'),
        cirq.measure(q5, key='q5'),
        
        cirq.X(q6),
        cirq.X(q7),
        cirq.TOFFOLI(q6,q7,q8),
        cirq.measure(q6, key='q6'),
        cirq.measure(q7, key='q7'),
        cirq.measure(q8, key='q8'),
        
        cirq.X(q9),
        cirq.X(q10),
        cirq.X(q11),
        cirq.TOFFOLI(q9,q10,q11),
        cirq.measure(q9, key='q9'),
        cirq.measure(q10, key='q10'),
        cirq.measure(q11, key='q11'),
        
        cirq.X(q13),
        cirq.X(q14),
        cirq.TOFFOLI(q12,q13,q14),
        cirq.measure(q12, key='q12'),
        cirq.measure(q13, key='q13'),
        cirq.measure(q14, key='q14'),
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
