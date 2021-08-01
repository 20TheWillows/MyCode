import pandas as pd
import numpy as np
import timeit as ti
from guppy import hpy

EXCEL_FILE = r'C:\Users\Simon\Desktop\Simon\ROSEN\MyCode\Python\Data\StudentList.xlsx'

def convert_string_to_boolean(cell):
    if isinstance(cell,str):
        if cell.lower().strip() == 'yes':
            return True
        elif cell.lower().strip() == 'no':
            return False
        else:
            return None
    elif isinstance(cell,int):
        if cell == 1:
            return True
        else:
            return False
    elif isinstance(cell, float):
        if cell > 0.0:
            return True
        else:
            return False
    return None


# Start
start = ti.timeit()
df = pd.read_excel(EXCEL_FILE, sheet_name='Sheet1')
end = ti.timeit()
print(end - start)
print("--------------------------------------")
s = """\
df['Repaired Flag'] = df['Repaired Flag'].apply(convert_string_to_boolean)
"""
t = """\
df['Repaired Flag']= df['Repaired Flag'].map({"Yes":True, "No":False})    
    """
u = """\
df['Repaired Flag']= df['Repaired Flag'].map(lambda x: True if x.lower().strip()=='yes' else False, na_action='ignore')    
    """
start = ti.timeit()
df['Repaired Flag']= df['Repaired Flag'].map(convert_string_to_boolean, na_action='ignore')    
end = ti.timeit()
print(end-start)
df.rename(columns={"Repaired Flag":"Repaired"},inplace=True)
print(df)

h = hpy()
print(h.heap())