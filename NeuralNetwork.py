# This file defines the neuron for the pattern
# matching

class ShapesNeuron:
    def __init__(self, matrix: list[list]):
        self.sum = 0
        
        for line in matrix:
            for val in line:
                if val == 1:
                    self.sum += 1
    
        self.weights = matrix.copy()
    
    def infer(self, mat: list[list]):
        sum = 0
        
        for line1, line2 in zip(self.weights, mat):
            for val1, val2 in zip(line1, line2):
                sum += val1 * val2
        
        return sum == self.sum

class ShapesNet:
    def __init__(self, list_of_matrix: list[list[list]]):
        self.neurons: list[ShapesNeuron] = []
        
        for matrix in list_of_matrix:
            self.neurons.append(ShapesNeuron(matrix))
        
    def infer(self, to_compare: list[list]):
        result = False
        
        for neuron in self.neurons:
            result = neuron.infer(to_compare)
            if result:
                break
        
        return result

# Contains all the dead end sides ShapesNet
DEAD_END_ALL_SIDE_SN = ShapesNet(
    [
        [[ 1, -1,  1],
         [ 1, -1,  1],
         [ 1,  1,  1]],
        
        [[ 1,  1,  1],
         [ 1, -1, -1],
         [ 1,  1,  1]],
        
        [[ 1,  1,  1],
         [ 1, -1,  1],
         [ 1, -1,  1]],
        
        [[ 1,  1,  1],
         [-1, -1,  1],
         [ 1,  1,  1]]
    ]
)

CORRIDOR_ALL_SIDE_SN = ShapesNet(
    [
        [[ 1, -1,  1],
         [ 1, -1,  1],
         [ 1, -1,  1]],
        
        [[ 1,  1,  1],
         [-1, -1, -1],
         [ 1,  1,  1]]
    ]
)

if __name__ == '__main__':
    test_mat = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    result = DEAD_END_ALL_SIDE_SN.infer(test_mat)
    assert result == False
    
    test_mat[2][1] = 0
    
    result = DEAD_END_ALL_SIDE_SN.infer(test_mat)
    assert result == True
    
    result = CORRIDOR_ALL_SIDE_SN.infer(test_mat)
    assert result == False

    test_mat[0][1] = 0
    result = CORRIDOR_ALL_SIDE_SN.infer(test_mat)
    assert result == True
    
    print('All tests passed')