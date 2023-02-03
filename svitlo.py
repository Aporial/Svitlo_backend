import re
import os
import csv
import openpyxl
import pandas as pd
from telethon.sync import TelegramClient

api_id = 24303600
api_hash = 'b6610be80c2f967b939419830e9e1863'
phone = '380990500069'

client = TelegramClient(phone, api_id, api_hash)

client.start(password='aporia901')

channel_username = 'https://t.me/svitlosumschina'

data = []
for message in client.get_messages(channel_username, limit=1, search='черга'):
    data.append([message.message])
    print(message.message)
df = pd.DataFrame(data)

df.to_csv('message.csv', encoding='utf-8')

file = open('message.csv', 'r', encoding='utf-8')
text = file.read()
file.close()

text = re.sub(r'\n|\s+', ' ', text).strip()
# 1 turn
res1 = re.search(r'✅1(.*)✅2', text)
with open('meta.txt', 'w', encoding='utf-8') as f:
    f.write(str(res1.group(0)))
file1 = open('meta.txt', 'r', encoding='utf-8')
text1 = file1.read()
file1.close()
text1 = text1[11: -4]
with open('first_res.txt', 'w') as one:
    one.write(text1)
# 2 turn
res2 = re.search(r'✅2(.*)✅3', text)
with open('meta.txt', 'w', encoding='utf-8') as f:
    f.write(str(res2.group(0)))
file2 = open('meta.txt', 'r', encoding='utf-8')
text2 = file2.read()
file2.close()
text2 = text2[11: -4]
with open('second_res.txt', 'w') as two:
    two.write(text2)
# 3 turn
res3 = re.search(r'✅3(.*)00.', text)
with open('meta.txt', 'w', encoding='utf-8') as f:
    f.write(str(res3.group(0)))
file3 = open('meta.txt', 'r', encoding='utf-8')
text3 = file3.read()
file3.close()
text3 = text3[10: -1]
with open('third_res.txt', 'w', encoding='utf-8') as three:
    three.write(text3)

lines = text1, text2, text3
with open("full_res.txt", "w", encoding='utf-8') as full:
    for line in lines:
        full.write(line + '\n')
# FULL

res_one = 'first_res.txt'
res_two = 'second_res.txt'
res_three = 'third_res.txt'
meta = 'meta.txt'
message_file = 'message.csv'
if os.path.exists(res_one):
    os.remove('first_res.txt')
if os.path.exists(res_two):
    os.remove('second_res.txt')
if os.path.exists(res_three):
    os.remove('third_res.txt')
if os.path.exists(meta):
    os.remove('meta.txt')
if os.path.exists(message_file):
    os.remove('message.csv')
# deleting unnecessary files

input_file = 'full_res.txt'
output_file = 'full.xlsx'

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

with open('full_res.txt', 'r', encoding='utf-8') as data:
    reader = csv.reader(data, delimiter=';')
    for row in reader:
        ws.append(row)

wb.save(output_file)
# save base date
full_file = 'full_res.txt'
if os.path.exists(full_file):
    os.remove('full_res.txt')
# deleting unnecessary files
