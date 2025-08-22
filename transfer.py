import numpy as np
input = np.array([-0.28, 0.0, 0.0, 0.669, -0.363, 0.0,
                    -0.28, 0.0, 0.0, 0.669, -0.363, 0.0,
                    0.0, 0.0, 0.0,
                    0.2,  0.2, 0.0, 0.6, 0.0, 0.0, 0.0,
                    0.2, -0.2, 0.0, 0.6, 0.0, 0.0, 0.0])
joint_mapping = [0, 3, 6, 9, 13, 17, 
                      1, 4, 7, 10, 14, 18, 
                      2, 5, 8, 
                      11, 15, 19, 21, 23, 25, 27, 
                      12, 16, 20, 22, 24, 26, 28]
output = np.zeros_like(input)
for i in range(29):
    output[joint_mapping[i]] = input[i]
strr = ""
for i in range(29):
    strr += str(output[i])
    strr += ', '
print(strr)