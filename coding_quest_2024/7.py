with open('/Users/jesse/Desktop/python_code/coding_quest_2024/7.txt','r')as f:
   lines = f.readlines()


total = 0


folder_indexes = []
folders = {}
for i in range(len(lines)):
   if "Folder:" in lines[i]:
      folder_indexes.append(i)


for i in range(len(folder_indexes)):
    if i == len(folder_indexes)-1:
       contents = lines[folder_indexes[i]+1:]
    else:
       contents = lines[folder_indexes[i]+1:folder_indexes[i+1]]
    contents.insert(0,"n")
    folders[i] = contents


for i in range(len(folder_indexes)):
  items = folders[i]
  for j in items:
      j = j.split()
      if "[FOLDER" in j:
        if folders[i][0] == 'n':
          if "delete" in j[1] or "temporary" in j[1]:
           
            folders[int(j[-1][0:-1])][0] = 'f'
           
        else:
          folders[int(j[-1][0:-1])][0] = 'f'
         

for i in folders.values():
  if i[0] == 'n':
    for j in i[1:]:
        j = j.split()
        if len(j) == 3:
          if "temporary" in j[1] or "delete" in j[1]:
              total += int(j[2])
  else:
     for j in i[1:]:
        j = j.split()
        if len(j) == 3:
          total += int(j[2])


#for x,y in folders.items():
   #print(x,y)


print(total)
