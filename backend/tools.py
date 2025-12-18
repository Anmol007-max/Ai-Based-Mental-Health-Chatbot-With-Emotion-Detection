# Step1: Setup Ollama with Medgemma tool
import ollama

def query_medgemma(prompt: str) -> str:
    """Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
    Respond to patients with:

    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...") 

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of patients problem
    """
    
    try:
        # Merge system prompt with user message for better compatibility
        
        full_prompt = f"{system_prompt}\n\nPatient: {prompt}\n\nDr. Emily Hartman:"
        
        
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "user", "content": full_prompt}
            ],
            options={
                'num_predict': 350,
                'temperature': 0.7,
                'top_p': 0.9
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly. Error: {str(e)}"

# Step2: Setup Twilio calling API tool
from twilio.rest import Client
from backend.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def call_emergency():
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=EMERGENCY_CONTACT,
            from_=TWILIO_FROM_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml"  # Can customize message
        )
        print(f"✅ Emergency call initiated successfully!")
        print(f"Call SID: {call.sid}")
        print(f"Status: {call.status}")
        return {"success": True, "call_sid": call.sid, "status": call.status}
    except Exception as e:
        print(f"❌ Emergency call failed: {str(e)}")
        return {"success": False, "error": str(e)}


