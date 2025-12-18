import warnings
import os

# Suppress all warnings including LangGraph deprecation
warnings.filterwarnings("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"

from langchain_core.tools import tool
from backend.tools import call_emergency
from backend.config import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

@tool
def emergency_call_tool() -> str:
    """
    Place an emergency call to the safety helpline's phone number via Twilio.
    Use this ONLY if the user expresses suicidal ideation, intent to self-harm,
    or describes a mental health emergency requiring immediate help.
    """
    result = call_emergency()
    return str(result)


@tool
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.

    Args:
        location (str): The name of the city or area in which the user is seeking therapy support.

    Returns:
        str: A newline-separated string containing therapist names and contact info.
    """
    return (
        f"Here are some therapists near {location}:\n"
        "- Dr. Ayesha Kapoor - +1 (555) 123-4567\n"
        "- Dr. James Patel - +1 (555) 987-6543\n"
        "- MindCare Counseling Center - +1 (555) 222-3333"
    )


# Emergency keywords for safety
EMERGENCY_KEYWORDS = [
    'suicide', 'kill myself', 'end my life', 'want to die', 
    'better off dead', 'harm myself', 'cut myself', 'overdose',
    'jump off', 'hang myself', 'shoot myself', 'end it all'
]

# Create LangChain ReAct Agent with Google Gemini - only emergency and therapist finder tools
tools = [emergency_call_tool, find_nearby_therapists_by_location]
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Current stable model (Gemini 1.5 was retired April 2025)
    temperature=0.7,
    google_api_key=GEMINI_API_KEY
)

graph = create_react_agent(llm, tools=tools)

SYSTEM_PROMPT = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist specializing in mental health therapy.

Your role is to provide compassionate, evidence-based mental health support. Respond with:
- Emotional attunement and empathy
- Gentle normalization of feelings
- Practical therapeutic guidance
- Strengths-focused support

You have access to two specialized tools:

1. `find_nearby_therapists_by_location`: Use this if the user asks about nearby therapists or when recommending local professional help would be beneficial.
2. `emergency_call_tool`: Use this IMMEDIATELY if the user expresses suicidal thoughts, self-harm intentions, or is in crisis.

For all other mental health queries, respond DIRECTLY with therapeutic guidance - do NOT use a tool.
Always be kind, clear, and supportive."""

def parse_response(stream):
    tool_called_name = "None"
    final_response = None

    for s in stream:
        # Check if a tool was called
        tool_data = s.get('tools')
        if tool_data:
            tool_messages = tool_data.get('messages')
            if tool_messages and isinstance(tool_messages, list):
                for msg in tool_messages:
                    tool_called_name = getattr(msg, 'name', 'None')

        # Check if agent returned a message
        agent_data = s.get('agent')
        if agent_data:
            messages = agent_data.get('messages')
            if messages and isinstance(messages, list):
                for msg in messages:
                    # Only capture AIMessage content, not ToolMessage
                    if hasattr(msg, 'content') and msg.content:
                        # Filter out tool call artifacts from the response
                        if not (hasattr(msg, 'type') and msg.type == 'tool'):
                            # Handle content that might be a list of dicts or a string
                            content = msg.content
                            
                            # If content is a list, extract text from it
                            if isinstance(content, list):
                                text_parts = []
                                for item in content:
                                    if isinstance(item, dict) and 'text' in item:
                                        text_parts.append(item['text'])
                                    elif isinstance(item, str):
                                        text_parts.append(item)
                                content_str = ' '.join(text_parts)
                            else:
                                content_str = str(content)
                            
                            # Check if content doesn't start with function call syntax
                            if not content_str.strip().startswith('<function='):
                                final_response = content_str

    return tool_called_name, final_response

'''if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        print(f"Received user input: {user_input[:200]}...")
        inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_input)]}
        stream = graph.stream(inputs, stream_mode="updates")
        tool_called_name, final_response = parse_response(stream)
        
        # Show which model/tool is being used
        if tool_called_name == "ask_mental_health_specialist":
            print(f"\n🔧 TOOL: {tool_called_name}")
            print(f"🤖 MODEL: Groq (llama-3.3-70b-versatile) - Therapeutic Mode")
        elif tool_called_name != "None":
            print(f"\n🔧 TOOL: {tool_called_name}")
        else:
            print(f"\n🤖 MODEL: Groq (llama-3.3-70b-versatile)")
        
        print(f"ANSWER: {final_response}\n")'''