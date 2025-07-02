from job_application_assistant.backend.services import workflow_service

def main():
    try:
        result = workflow_service.run_workflow()
        print("Workflow run result:", result)
    except Exception as e:
        print("Error running workflow:", e)

if __name__ == "__main__":
    main()
