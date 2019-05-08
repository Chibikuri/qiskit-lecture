from qiskit import load_qasm_file, load_qasm_string


class QasmReader:
    backend = Aer.get_backend('qasm_simulator')

    def __init__(self, name=None):
        self.name = name

    def StringQasmtoCircuit(self, qasm):
        '''
        input:
            qasm: string(string qasm)
        output:
            qc: object(Quantum Circuit)
        You should use from_qasm_str() but now it's static method.
        So, we can't use.
        '''
        # job = execute(qasm, backend=self.backend, shots=1024)
        qc = load_qasm_string(qasm)
        return self.name, qc

    def FileQasmtoCircuit(self, path):
        '''
        input:
            path: string(file path of qasm file)
        output:
            qc: object(Quantum Circuit)
        You should use from_qasm_file() but now it's static method.
        So, we can't use.
        '''
        qc = load_qasm_file(path)
        return qc

if __name__ == '__main__':
    entangle = QasmReader('Entangle')

    # qasm from string
    qasm = '''
            OPENQASM 2.0;
            include "qelib1.inc";
            qreg q[2];
            x q[0];
            cz q[0],q[1];
            '''

    circuit1 = entangle.StringQasmtoCircuit(qasm)
    print(name1)
    print(circuit1)

    # qasm from file
    qasm = './ex1.qasm'

    name2, circuit2 = entangle.FileQasmtoCircuit(qasm)
    print(name2)
    print(circuit2)
