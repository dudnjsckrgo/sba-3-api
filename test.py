import numpy as np
aa = np.array(range(20)).reshape((2,2,5))
print(aa)
bb=aa.reshape(-1,2*10)
print(bb)