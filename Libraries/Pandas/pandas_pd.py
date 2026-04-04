import pandas as pd
# # Create a Series from a list
# data = [10, 20, 30, 40, 50]
# s = pd.Series(data)
# print(s)
data={f"Student":["David","Samuel","Terry","Evan"],
      f"Age":[27,24,22,32],
      f"Country":["UK","Canada","China","USA"],
      f"Course":["Python","Data Structures","Machine learning","Web Developement"],
      f"Marks":[85,72,89,76]}
student_record=pd.DataFrame(data)
print(student_record)
# b=student_record["\"Marks\""]
# c=student_record[["\"Country\"","\"Course\""]]
# print(b)
# print(c)
# print(type(b))
# print(student_record.iloc[0,0])
# print(student_record.iloc[0,2])
# print(student_record.loc[0,"\"Marks\""])
# student_record2=student_record
# student_record2.head()
# student_record2=student_record2.set_index("Student")
# print(student_record2)
# print(student_record.iloc[0:2,0:3])
# print(student_record2.loc["David":"Samuel","Age":"Country"])
print(student_record.loc[2:3,"Country":"Marks"])

