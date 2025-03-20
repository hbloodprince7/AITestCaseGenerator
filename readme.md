# Gemini Unit Test Generator

This Streamlit application allows you to generate unit tests for your code using the Google Gemini model. You can either upload a code file (Python, C#, or Java) or enter code directly into the application.

## Features

* **Code Input:** Upload code files or manually enter code snippets.
* **Unit Test Generation:** Generates 5 unit tests for your provided code using Google's Gemini model.
* **Language Detection:** Attempts to detect the programming language of your code to generate tests in the correct language.
* **File Download:** Downloads the generated unit tests as a file (e.g., `unit_tests.py`, `unit_tests.java`, `unit_tests.cs`).
* **Streamlit Interface:** User-friendly web interface for easy interaction.

## Prerequisites

* Python 3.6+
* Google Gemini API Key
* Required Python packages (install using ``)

## Installation

1.  **Clone the repository (or download the Python script).**
2.  **Install the required Python packages:**

    ```bash
    pip -r requirements.txt
    ```

3.  **Set up your Google Gemini API Key:**
    * Create a `.env` file in the same directory as your Python script.
    * Add your API key to the `.env` file in the following format:

        ```
        GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY
        ```

    * Replace `YOUR_ACTUAL_API_KEY` with your actual API key.

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run your_script_name.py
    ```

    (Replace `your_script_name.py` with the name of your Python script.)

2.  **Open the application in your web browser:**
    * A local URL will be displayed in your terminal. Open this URL in your browser.

3.  **Enter your code:**
    * You can either upload a code file or enter code directly into the text area.

4.  **Click the "Generate Unit Tests" button:**
    * The application will send your code to the Gemini model and generate unit tests.

5.  **Download the unit tests:**
    * A download button will appear, allowing you to download the generated unit tests as a file.

## Example

1.  Upload a python file called `add_numbers.py` or paste the following code into the text area:

    ```python
    def add_numbers(a, b):
        return a + b
    ```

2.  Click the "Generate Unit Tests" button.

3.  Download the generated `unit_tests.py` file.

## Notes

* The language detection is basic. Please verify that the tests are generated in the correct language.
* The quality of the generated tests depends on the complexity and clarity of your code.
* Ensure that your Google Gemini API key is properly set up in the `.env` file.