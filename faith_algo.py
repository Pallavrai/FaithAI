from transformers import pipeline, set_seed

# Set up the pipeline for generating text using GPT-2
generator = pipeline('text-generation', model='gpt2')

# Set the random seed to ensure consistent output
set_seed(42)
logging.getLogger("transformers").setLevel(logging.ERROR)


# Define a function for chatting with the user
def chat():
    # Get the user's input
    user_input = input("You: ")
    
    # Generate a response using GPT-2
    response = generator(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
    
    # Print the response
    print("ChatGPT: " + response)

# Start the chat loop
while True:
    chat()
