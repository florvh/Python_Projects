from http import client
from urllib import response
import discord
import os
import sqlite3

conn = sqlite3.connect('Leden.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Leden (
    username text NOT NULL,
    punten integer NOT NULL
    )""")



client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as user {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'monke-bot':
        if user_message.lower() == '!help':
            await message.channel.send('type !add to add points to your total')
            return
        elif user_message.lower() == '!points':
            await message.channel.send(f'{username}: ')
            return
        elif user_message.lower() == '!add':
            c.execute(f"INSERT INTO Leden VALUES ('{username}', 10)")
            conn.commit()
            response = f'{username} added 10 points to their total'
            await message.channel.send(response)
            return


#commit de commands
conn.commit()

#sluit de connection
#conn.close()

client.run(os.getenv("TOKEN"))