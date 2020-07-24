import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, .1)

def function1(x):
  return abs(x)

plt.plot(function1(x), "g")
plt.show()


# import numpy as np

# nums = np.array( [ [1,2], [3, 4]] )

# foods = np.array([1,2,3])
# trash = np.array([1,2,3])


# for i in range(nums.shape[0]):
#   for j in range(nums.shape[1]):
#     print(nums[i][j])

# nums = np.append(nums, [17, 18, 19 ,20])
# print(nums)

