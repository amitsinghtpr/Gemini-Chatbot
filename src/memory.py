class Memory:
    def __init__(self):
        self.memory_storage = []

    def add_memory(self, user_input, bot_response):
        self.memory_storage.append({'user_input': user_input, 'bot_response': bot_response})

    def retrieve_memory(self):
        # Format memory as a conversation string
        conversation = ""
        for item in self.memory_storage:
            conversation += f"Human: {item['user_input']}\nAI: {item['bot_response']}\n"
        return conversation.strip()

    def clear_memory(self):
        self.memory_storage.clear()