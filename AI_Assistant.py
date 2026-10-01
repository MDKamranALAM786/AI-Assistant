from groq import Groq

class AI_Assistant :
    def __init__(self, api_key) :
        print("Loading Assistant...")
        self.client = Groq(api_key=api_key)
        self.model = "openai/gpt-oss-120b"
        print("Assistant Ready!")

    def answer_query(self, query) :
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.6,
            # max_tokens=1024,
            messages=[
                {"role" : "system", "content" : "Act like a professional assistant"},
                {"role" : "user", "content" : query}
            ]
        )

        return(response.choices[0].message.content.strip())

    def summarize_email(self, email) :
        prompt = f"Summarize the email in 2-3 sentences. Email : {email}"

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.3,
            max_tokens=512,
            messages=[
                {"role" : "system", "content" : "Act like an expert email assistant"},
                {"role" : "user", "content" : prompt}
            ]
        )

        return(response.choices[0].message.content)

