import numpy as np
from beautifultable import BeautifulTable

table = BeautifulTable()

temp_c = np.arange(0, 101, 5)
print(temp_c)

temp_f = (temp_c * 9 / 5) + 32
print(temp_f)

table.columns.header = ["Celcius", "Fahrenheit"]

for i in range(len(temp_c)):
    table.append_row([temp_c[i], temp_f[i]])


table.columns.alignment["Celcius"] = BeautifulTable.ALIGN_LEFT
print(table)
