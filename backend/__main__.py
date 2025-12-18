"""
Entry point for running the backend as a module.
Usage: python -m backend.ai_agent
"""
import warnings
import os

# Suppress all warnings
warnings.filterwarnings("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"

from backend.ai_agent import graph, SYSTEM_PROMPT, parse_response

print("🤖 AI Mental Health Therapist - Command Line Interface")
print("=" * 60)
print("Type your message and press Enter. Type 'quit' to exit.\n")

while True:
    try:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Take care! Remember, you're not alone.")
            break
        
        if not user_input:
            continue
        
        print("\n🔄 Processing...\n")
        
        inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_input)]}
        stream = graph.stream(inputs, stream_mode="updates")
        tool_called_name, final_response = parse_response(stream)
        
        # Show which tool was used (if any)
        if tool_called_name != "None":
            print(f"🔧 Tool Used: {tool_called_name}\n")
        
        # Display the response
        print(f"Dr. Emily: {final_response}\n")
        print("-" * 60 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 Session ended. Take care!")
        break
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
        import traceback
        traceback.print_exc()
