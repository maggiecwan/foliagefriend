from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import yaml
import nltk
from nltk.tokenize import word_tokenize
import WordToDigits

GREEN = '\033[92m'
WHITE = '\033[0m'

# Load the data from the YAML file
with open('plantConversations.yaml') as f:
    data = yaml.safe_load(f)

# Create a new chat bot
bot = ChatBot('PlantBot')

# Train the bot using the ListTrainer
list_trainer = ListTrainer(bot)
for conversation in data['conversations']:
    list_trainer.train(conversation)

# Define a function to recommend a plant based on user preferences
def recommend_plant(size, pets, sunlight, effort, purpose, time):
    size = wordtodigits.convert(size)
    size_tokens = word_tokenize(size)
    #nltk.download('stopwords')
    sz = []
    min = 0
    max = 0
    for i in size_tokens:
        if i.isdigit():
            sz.append(int(i))
    if len(sz) == 0:
        max = 20
    elif len(sz) == 1:
        min = sz[0] - 5
        max = sz[0] + 5
    else:
        sz.sort
        min = sz[0]
        max = sz[-1]
    
    yesses = ["yes", "yeah", "y", "correct", "yup"]
    pets_tokens = word_tokenize(pets)
    ispets = False
    for i in pets_tokens:
        for y in yesses:
            if i == y:
                ispets = True
    
    light_tokens = word_tokenize(sunlight)
    lt = 5
    for i in light_tokens:
        if i.isdigit():
            lt = int(i)

    purpose_tokens = word_tokenize(purpose)
    flower = ["flowers", "decoration", "color", "bloom", "pretty", "decor"]
    food = ["food", "eating", "crops", "herbs"]
    food_fruit = ["fruit", "fruits"]
    food_veg = ["veg", "vegetables", "vegetable", "veggie", "veggies"]
    picked = False
    use = [False, False, True]
    eating_params = []
    for i in purpose_tokens:
        if not picked:
            for j in flower:
                if i == j:
                    use = [True, False, False]
                    picked = True
        if not picked:
            for j in food:
                if i == j:
                    use = [False, True, False]
                    picked = True
    if use == [False, True, False]:
        for i in purpose_tokens:
            for j in food_fruit:
                if i == j:
                    eating_params = [False, True, []]
    


    plant = "PLANT"
    return plant


# Chatbot

print('Welcome to Foliage Friend! Please answer some of our questions to find the right plant for you!')
print('If you would like to leave, type "exit".\n\n')
while True:
    try:
        # Ask the user questions to gather information about their preferences
        #climate = input(GREEN + '🪴 What are the climate conditions like?\n' + WHITE + 'You: ')
        # area = input(GREEN + '🪴 Do you live in a rural or urban area?\n' + WHITE + 'You: ')
        size = input(GREEN + '🪴 About how large would you like your plant to be (in cm)?\n' + WHITE + 'You: ')
        pets = input(GREEN + '🪴 Do you have any pets or small children?\n' + WHITE + 'You: ')
        sunlight = input(GREEN + '🪴 On a scale of 1 to 10, how much sunlight do you have?\n' + WHITE + 'You: ')
        effort = input(GREEN + '🪴 How much effort do you expect to put in?\n' + WHITE + 'You: ')
        purpose = input(GREEN + '🪴 What is the purpose of this plant?\n' + WHITE + 'You: ')
        time = input(GREEN + '🪴 How long do you want your plant to last (annual, biannual, perennial)?\n' + WHITE + 'You: ')

        # Recommend a plant based on the user's answers
        recommended_plant = recommend_plant(size, pets, sunlight, effort, purpose, time)

        # Respond to the user with the recommended plant
        bot_response = GREEN +' Based on your preferences, I would recommend the ' + recommended_plant
        print(GREEN +'🪴', bot_response)
        print(GREEN +'There you go! To ask about another plant, type anything.')
        print(GREEN +'If not, type "exit" to quit.')


        user_input = input('You: ')
        if user_input.lower() == 'exit':
            print('Goodbye!')
            break
        

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
