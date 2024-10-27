import pandas as pd
import numpy as np
import matplotlib as plt


data = {'names': ['Alice', 'Bob', 'Charlie','David'],
        'age': [20,21,22,23],
        'gender': ['F','M','M','M']}

df=pd.DataFrame(data)

df1=pd.read_excel("D:/Downloads/student.xlsx")
df1.head()

print(df.describe())


#MATPLOTLIB EXAMPLE
# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

#NUMPY EXAMPLE
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
#
# print(arr)
#
# print(type(arr))

#SCIPY EXAMPLE
# from scipy import constants
#
# print(constants.liter)
#.......................
# import scipy
#
# print(scipy.__version__)

#PANDAS EXAMPLE
# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)
#..................................

# import pandas as pd

# data = {'Names': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [20,21,22,23],
#         'Sex': ['F', 'M', 'M', 'M']}
# df = pd.DataFrame(data)
# print (df)