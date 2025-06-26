import subprocess
import os
import time
import google.generativeai as genai

def test_open_app():
    try:
        subprocess.Popen(["open", "-a", "Brave Browser"])
        print("✅ Open Brave Browser - PASSED")
    except Exception as e:
        print(f"❌ Open Brave Browser - FAILED: {e}")

def test_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ API Key missing. Please set the GEMINI_API_KEY environment variable.")
        return
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello")
        if response.text:
            print("✅ Gemini API Call - PASSED")
        else:
            print("❌ Gemini API Call - FAILED: No response text")
    except Exception as e:
        print(f"❌ Gemini API Call - FAILED: {e}")

def test_shutdown_command():
    # This is a placeholder for shutdown command test
    # Actual implementation would require integration testing or mocking
    print("⚠️ Shutdown command test requires manual verification.")

def main():
    print("Starting automated tests for Jarvis AI Voice Assistant...\n")
    test_open_app()
    time.sleep(2)  # Wait for app to open
    test_api_key()
    test_shutdown_command()
    print("\nAutomated tests completed.")

if __name__ == "__main__":
    main()
