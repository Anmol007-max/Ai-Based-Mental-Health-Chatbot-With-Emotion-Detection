# MindBot 🧠💬  
### AI-Powered Mental Health Support Chatbot (Agent-Based | Gemini API)

MindBot is an **AI-powered mental health support chatbot** designed as a **first-level emotional support system**. It uses an **agent-based architecture** to analyze user conversations, detect emotional intent, and provide empathetic, safe, and context-aware responses using the **Google Gemini API**.

The chatbot dynamically routes user inputs to specialized tools such as **crisis handling**, **therapist search**, and **medical reasoning (MedGemma)**, ensuring appropriate support across normal, emotional, and high-risk situations.

> ⚠️ **Disclaimer:** MindBot is not a licensed therapist and does not provide medical diagnosis or treatment. It is intended only for educational and supportive purposes.

---

## ✨ Features

- 🧠 **Emotion & Intent Detection**  
  Detects emotional intent from user text using NLP techniques and LLM-based contextual inference.

- 🤖 **Agent-Based Decision Routing**  
  Routes user queries intelligently based on severity and intent.

- 🚨 **Crisis Handling Module**  
  Activates safety-focused responses and emergency support workflows for high-risk inputs.

- 📍 **Therapist Search Tool**  
  Helps users locate nearby mental health professionals.

- 🩺 **Medical Reasoning (MedGemma)**  
  Handles health-related queries with safety-aligned medical guidance.

- 💬 **Empathetic Conversations**  
  Provides supportive responses using CBT-inspired coping strategies.

- 🔐 **Ethical & Safety-Oriented Design**  
  No diagnosis, clear AI disclosure, and emphasis on user safety.

---

## 🏗️ System Architecture

MindBot follows an **agentic AI workflow**:

1. User inputs a text message  
2. Text preprocessing and normalization  
3. Emotion & intent detection  
4. Agent-based decision routing  
5. Tool invocation (if required):  
   - Crisis handling  
   - Therapist search  
   - MedGemma medical reasoning  
6. Response generation using **Google Gemini API**  
7. Safe and personalized response delivered to the user  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **LLM:** Google Gemini API  
- **AI Design:** Agent-based architecture  
- **Medical Reasoning:** MedGemma  
- **Frontend:** Web-based chatbot interface  
- **Domain:** Mental Health Support (Educational Project)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Google Gemini API Key

### Installation

```bash
git clone https://github.com/your-username/mindbot.git
cd mindbot
pip install -r requirements.txt

Environment Setup

Create a .env file and add:
GEMINI_API_KEY=your_api_key_here

Run the Project
python app.py

```

### 🧪 Testing
##The system was tested using:

 *Simulated emotional conversations
 *Pilot user interactions
 *Predefined test cases (neutral, emotional, crisis-level)
 Evaluation focused on:
 *Emotion detection accuracy
 *Correct tool routing
 *Response safety and empathy

---

## 📈 Results Summary

Correct differentiation between normal, emotional, and crisis inputs
 *Reliable crisis detection and safety handling
 *Consistent and empathetic responses
 *Accurate routing to appropriate tools
MindBot performs effectively as a first-level mental health support chatbot.

---

## 🔮 Future Scope

Full-scale web application with authentication and session history
 *Voice-based emotion recognition
 *Facial expression analysis using computer vision
 *Multimodal Emotion Recognition (text + voice + facial cues)
 *Native Android and iOS applications
 *Clinical validation with mental health professionals

---

## 🙏 Acknowledgements
 *Inspired by agentic AI workflows
 *Tutorial foundation by AI with Hassan
 *Google Gemini & MedGemma research contributions

---

## 📜 License
This project is for educational purposes only.
You are free to explore, modify, and learn from the code.

---

## 🤝 Contributions
Contributions, suggestions, and feedback are welcome.
Feel free to open an issue or submit a pull request.

---

## ⭐ If you found this project useful, consider giving it a star!
