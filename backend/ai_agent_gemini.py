if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        print(f"Received user input: {user_input[:200]}...")
        inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_input)]}
        
        # Use invoke instead of stream for simpler output
        result = graph.invoke(inputs, config={"recursion_limit": 50})
        
        # Get the last message from the agent
        if result and 'messages' in result:
            last_message = result['messages'][-1]
            if hasattr(last_message, 'content'):
                print(f"\nASSISTANT: {last_message.content}\n")
            else:
                print(f"\nASSISTANT: {last_message}\n")
