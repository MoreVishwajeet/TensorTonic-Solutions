import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # ans = []
    # if(type(x) == int) return ans.append(1 / (1 + np.exp(-x)))
    
    # for i in x:
    #     ans.append(1 / (1 + np.exp(-i)))
        
    # return ans
    x = np.array(x)
    return 1 / (1 + np.exp(-x))