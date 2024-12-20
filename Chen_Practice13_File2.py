import os
import zipfile
from collections import defaultdict

with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    zip_ref.extractall('names_data')

male_names = defaultdict(int)
female_names = defaultdict(int)

folder_path = 'names_data'
files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'r') as file:
        male_max = ('', 0)  
        female_max = ('', 0)
        
        for line in file:
            name, sex, occurrences = line.strip().split(',')
            occurrences = int(occurrences)
            
            if sex == 'M' and occurrences > male_max[1]:
                male_max = (name, occurrences)
            elif sex == 'F' and occurrences > female_max[1]:
                female_max = (name, occurrences)
        

        if male_max[0]:
            male_names[male_max[0]] += 1
        if female_max[0]:
            female_names[female_max[0]] += 1

sorted_male_names = sorted(male_names.items(), key=lambda x: x[1], reverse=True)
sorted_female_names = sorted(female_names.items(), key=lambda x: x[1], reverse=True)


print("\nMale Names:")
for name, count in sorted_male_names:
    print(f"{name} {count}")

print("\nFemale Names:")
for name, count in sorted_female_names:
    print(f"{name} {count}")
