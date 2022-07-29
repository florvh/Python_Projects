import json

with open("json_data.json", "r") as read_file:
    data = json.load(read_file)

file_object = open('messages.txt','a')

for item in data:
    file_object.write(item['author']['username']+':'+'\n')
    file_object.write(item['content']+'\n')
    file_object.write(item['attachments']['url']+'\n')



