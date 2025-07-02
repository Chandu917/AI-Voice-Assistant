import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def check_job_eligibility(job_description, user_profile):
    prompt = f"""
You are a job eligibility checker AI. Based on the following job description and my profile details, check if I am eligible.

### My Profile:
{user_profile}

### Job Description:
{job_description}

### Output Format:
Eligible: Yes/No
Reason: [Explain why I am eligible or not]
Suggestions: [If not eligible, suggest improvements]
"""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
            n=1,
            stop=None,
        )
        text = response.choices[0].text.strip()
        eligible = "yes" in text.lower()
        return eligible, text
    except Exception as e:
        return False, f"Error during eligibility check: {str(e)}"
