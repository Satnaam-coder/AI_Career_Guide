import google.generativeai as genai
genai.configure(api_key="AIzaSyAxtiIbwh0Sfif1cCV8hT9EDAHxG79Xtzg")

# Stable model
model = genai.GenerativeModel("gemini-2.5-flash")

def chatbot_response(user_input):
    if not user_input.strip():
        return "Please ask something."

    try:
        prompt = f"""
        You are a career guidance AI.
        Help students after 12th.
        Give clear, simple, and practical answers.

        Question: {user_input}
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
    
"""print("--- Career Guidance AI Started (Type 'exit' to stop) ---")
while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit" , "quit" , "bye"]:
        print("AI: Goodbye! Good luck with your career.")
        break
    result = chatbot_response(user_query)
    print(f"AI: {result}\n")"""