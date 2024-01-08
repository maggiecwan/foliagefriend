from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import yaml
# import spacy


# Create a ChatBot instance
bot = ChatBot('PlantBot')

# Create a ListTrainer instance
list_trainer = ListTrainer(bot)

# Load and train the chatbot using the YAML file
with open('plantResponses.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    for category in data['categories']:
        patterns = category['patterns']
        responses = category['responses']
        list_trainer.train(patterns)
        list_trainer.train(responses)


# Train the chatbot using the ChatterBotCorpusTrainer
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.english.greetings', 'chatterbot.corpus.english.conversations')


# with open('plantConversations.yaml') as f:
#     data = yaml.safe_load(f)

# # Start by training the chatterbot with the ListTrainer
# list_trainer = ListTrainer(bot)
# for conversation in data['conversations']:
#     list_trainer.train(conversation)

# # Then, train with the CorpusTrainer to improve the bot's responses
# corpus_trainer = ChatterBotCorpusTrainer(bot)
# corpus_trainer.train('chatterbot.corpus.english')

# Start chatting with the user
print('Welcome to Foliage Friend! Please type your questions or type "exit" to quit.')
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    bot_response = bot.get_response(user_input)
    print('🪴', bot_response)
