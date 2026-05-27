from Handler import ai_handler, debugger

# Example usage of the ChatBot class
if __name__ == "__main__":
    # Example usage of the ChatBot class
    bot = ai_handler.ChatBot(name="Alice", desc="A friendly assistant", task="Help the user with their queries")
    
    # Simulate a user input and get a response from the bot
    user_input = "Hello, how are you?"
    bot.response = bot.get_response(user_input)  # This would typically be set by the get_response method after processing the user input
    sanatised_response = bot._sanatise_response()  # This method would need to be implemented in the ChatBot class to process the user input and generate a response
    bot.show_output(sanatised_response)  # This method would need to be implemented in the ChatBot class to process the user input and generate a response


    # Here you would typically call a method to get a response from the bot based on the user input
    # For example: bot.show_output()
    bot.get_response() # Get user input and process it to generate a response and store it in bot.response
    sanatised_response = bot._sanatise_response()  # This method would need to be implemented in the ChatBot class to process the user input and generate a response
    bot.show_output(sanatised_response)  # This method would need to be implemented in the ChatBot class to process the user input and generate a response
    
    # For demonstration, let's just print the current history
    for entry in bot.history:
        print(entry)
