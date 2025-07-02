# Frontend Testing Setup and Usage

This document explains how to run the frontend tests for the Job Application Automation project.

## Setup

1. Navigate to the frontend directory:

```bash
cd job_application_assistant/frontend
```

2. Install dependencies:

```bash
npm install
```

## Running Tests

Run the tests using the following command:

```bash
npm test
```

This will launch the test runner in watch mode.

## Test Details

- Tests are written using Jest and React Testing Library.
- Example test is provided for the main `App` component in `src/__tests__/App.test.jsx`.
- The test checks that the main heading "Job Application Automation" renders correctly.

## Adding More Tests

- Add new test files under `src/__tests__/`.
- Use React Testing Library for component rendering and interaction.
- Follow Jest conventions for test naming and structure.

## Notes

- Ensure you have Node.js and npm installed.
- The frontend uses React and react-scripts for build and test scripts.

This setup provides a foundation for frontend UI testing to ensure component correctness and UI stability.
