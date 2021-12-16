from pprint import pprint
import csv
import regex as re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


phonebook_all = []
set_names = set()
for item in contacts_list:
  name = item[0] + item[1] + item[2]
  phonebook = re.findall(r'([А-я][а-я]+)', name)
  if item[0] == 'lastname':
    phonebook_all.append(item)
    continue
  elif len(phonebook) < 3:
    phonebook.append('')
  phonebook.append(item[3])
  phonebook.append(item[4])
  numbers = re.findall(r'[^\s-)()+]', item[5])
  if numbers != []:
    numbers.insert(0,'+')
    numbers.insert(2,'(')
    numbers.insert(6,')')
    numbers.insert(10,'-')
    numbers.insert(13,'-')
    if len(numbers) > 16:
      numbers.insert(16,' ')   
  number = ''.join(numbers)
  phonebook.append(number)
  phonebook.append(item[6])
  name_check = phonebook[0]+phonebook[1]
  if name_check in set_names:
    for corr in phonebook_all:
      if corr[0] == phonebook[0] and corr[1] == phonebook [1]:
        for i in range (2,7):
          if corr[i] == '':
            corr[i] = phonebook[i]
  else:
    phonebook_all.append(phonebook)
    set_names.add(phonebook[0]+phonebook[1])
      
  
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')

  datawriter.writerows(phonebook_all)