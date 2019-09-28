import numpy as np


def difference(old_joints, new_joints, imp_joints):
    diff = np.subtract(old_joints, new_joints)
    print(diff)
    squared = np.square(diff)
    print(squared)
    return_val = np.array(np.sum(squared[imp_joints]))


# inp1 = np.array(input("ini 1"))
# inp2 = np.array(input("ini 2"))
# inp3 = np.array(input("ini 3"))

# print(difference(inp1, inp2, inp3))
