class MockGenai:
    def configure(self, api_key):
        pass

genai = MockGenai()

def ask_gemini(prompt):
    return '{"intent": "open_app", "target": "brave"}'
