import discord, os, random, asyncio, datetime
from discord.ext import commands, tasks
from dotenv import load_dotenv

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '$', intents = intents)


# Rock Paper Scissors parts

options = ['rock', 'paper', 'scissors']
rockS = ['✊', '✊🏿', '✊🏾', '✊🏽', '✊🏼', '✊🏻']
paperS = ['✋', '✋🏿', '✋🏾', '✋🏽', '✋🏼', '✋🏻']
scissorsS = ['✌️', '✌️', '✌️', '✌️', '✌️', '✌️']
f = open("wordList.txt", "r")
wordList = f.read()
f.close()

wordList = wordList.split()


# .env parts

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
tchan = os.getenv('TEST_CHANNEL')
tchan = int(tchan)
bchan = os.getenv('BOT_CHANNEL')
bchan = int(bchan)


# Test command

@bot.comman()
async def test(ctx):
    await.ctx.send('This is a test!')
    
    
# Getting the Bot ready

@bot.event
async def on_ready():
    print('\n{0.user} is ready for action'.format(bot))


@ Hangman command

@bot.command()
asynd def hangman(ctx):
    print('Someone is playing Hangman\n\n')
    misses = ['zero.png', 'one.png', 'two.png', 'three.png', 'four.png', 'five.png', 'six.png']
    usedLetters = []
    fails = 0
    wordChosen = random.choice(wordList)
    print(f"The word is {wordChosen}\n\n")
    await ctx.send('Welcome to my Hangman game!')
    await asyncio.sleep(1)
    await ctx.send(file = discord.File9misses[fails]))
    while True:
        allLetters = True
        output = ''
        for i in wordChosen:
            if i in usedLetters:
                output += i
            else:
                output += '-'
                allLetters = False
        await ctx.send(f" The Word -> {output}")
        await asyncio.sleep(.3)
        if allLetters:
            print(f"""Nice, someone just beat Hangman with only {fails} incorrect!""")
            await ctx.send(f"You won with {fails} misses")
            break
        await ctx.send('What is yhour guess?')
        try:
            guess = await bot.wait_for('message', check = lambda message: message.author == ctx.author, timeout = 180)
        except asyncio.TimeoutError:
            await ctx.send('Sorry, you didn't reply in time!')
        if guess.content.lower() in usedLetters:
            await ctx.send('You've already used this letter.')
            await asyncio.sleep(.3)
        if guess.content.lower() in wordChosen and guess.content.lower() not in usedLetters:
            await ctx.send('Good Job!')
            await asyncio.sleep(.3)
            usedLetters.append(guess.content.lower())
        elif guess.content.lower() not in wordChosen and guess.content.lower() not in usedLetters:
            await ctx.send('Dang, that wasn't it...')
            usedLetters.append(guess.content.lower())
            await asyncio.sleep(.3)
            fails += 1
        
        await ctx.send(file = discord.File(misses[fails]))
        await asyncio.sleep(1)
        await ctx.send(f"Letters used -> {usedLetters}")
        await asyncio.sleep(.3)
        
        if fails == 6:
            await ctx.send(f"""The answer was {wordChosen}.
            You have lost the game!""")
            print('Someone just lost in Hangman\n\n')
            await asyncio.sleep(.3)
            break
        else:
            await ctx.send(f"{fails} misses out of 6")
            await asyncio.sleep(.3)



# Rock Paper Scissors commands

@bot.command()
async def rock(ctx):
    while True:
        rockR = random.choice(rockS)
        paperR = random.choice(paperS)
        scissorsR = random.choice(scissorsS)
        botMove = random.choice(options)
        await ctx.send(botMove)
        if botMove == 'rock':
            await ctx.send("It's a tie")
            print('There was a tie\n\n')
            await asyncio.sleep(1)
        elif botMove == 'paper':
            await ctx.send(f"""{paperR} beats {rockR}
            Bot wins""")
            print('Bot wins\n\n')
            await.asyncio.sleep(1)
        elif botMove == 'scissors':
            await ctx.send(f"""{rockR} beats {scissorsR}
            You win""")
            print('Beat the bot\n\n')
        break


@bot.command()
async def paper(ctx):
    while True:
        rockP = random.choice(rockS)
        paperP = random.choice(paperS)
        scissorsP = random.choice(scissorsS)
        botMove = random.choice(options)
        await ctx.send(botMove)
        if botMove == 'rock':
            await ctx.send(f"""{paperP} beats {rockP}
            You win""")
            print('Beat the bot\n\n')
            await asyncio.sleep(1)
        elif botMove == 'paper':
            await ctx.send("It's a tie")
            print('There was a tie')
            await asyncio.sleep(1)
        elif botMove == 'scissors':
            await ctx.send(f"""{scissorsP} beats {paperP}
            Bot wins""")
            print('Bot wins\n\n')
        break


@bot.command()
async def scissors(ctx):
    while True:
        rockX = random.choice(rockS)
        paperX = random.choice(paperS)
        scissorsX = random.choice(options)
        botMove = random.choice(options)
        await ctx.send(botMove)
        if botMove == 'rock':
            await ctx.send(f"""{rockX} beats {scissorsX}
            Bot wins""")
            print('Bot wins\n\n')
            await asynio.sleep(1)
        elif botMove == 'paper':
            await ctx.send(f"""{scissorsX} beats {paperX}
            You win""")
            print('Beat the bot\n\n')
            await asyncio.sleep(1)
        elif botMove == 'scissors':
            await ctx.send("It's a tie")
            print('There was a tie\n\n')
        break



# Runs the Bot

try:
    bot.run(TOKEN)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e