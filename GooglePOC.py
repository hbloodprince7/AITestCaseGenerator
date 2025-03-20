import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Replace "gemini-2.0-flash-exp" with your model name
MODEL_NAME = "gemini-2.0-flash-exp" 

@st.cache_resource
def load_llm(model_name):
    return ChatGoogleGenerativeAI(model=model_name, google_api_key=os.getenv("GOOGLE_API_KEY"))

llm = load_llm(MODEL_NAME)

st.title(f"Generate Unit Tests with {MODEL_NAME}")

st.subheader("Enter Code or Upload File")

uploaded_file = st.file_uploader("Choose a code file (Python, C#, Java)", type=["py", "cs", "java"])

manual_code = st.text_area("Or enter code directly:")

code = None

if uploaded_file is not None:
    try:
        bytes_data = uploaded_file.getvalue()
        code = bytes_data.decode("utf-8")
        st.write("Uploaded code:")
        st.code(code)
    except UnicodeDecodeError:
        st.error("Error: Could not decode file with UTF-8 encoding.")
    except Exception as e:
        st.error(f"An error occurred during file processing: {e}")

elif manual_code:
    code = manual_code
    st.write("Entered code:")
    st.code(code)

if code:
    if st.button("Generate Unit Tests"):
        user_message_content = f"Generate 5 unit tests for the following code:\n```\n{code}\n```\nOutput the tests in the same programming language as the input code."

        messages = [HumanMessage(content=user_message_content)]

        try:
            response = llm.invoke(messages)
            test_code = response.content

            file_extension = "py"

            if "public class" in code:
                file_extension = "java"
            elif "namespace" in code:
                file_extension = "cs"
            elif "def " in code: #Check for python functions
                file_extension = "py"
            elif "class " in code: # Check for python classes
                if "def __init__" in code: # Check for python constructor.
                    file_extension = "py"
                else:
                    file_extension = "java" #if not python, we can assume java.

            st.download_button(
                label="Download Unit Tests",
                data=test_code.encode("utf-8"),
                file_name=f"unit_tests.{file_extension}",
                mime=f"text/{file_extension}",
            )

            st.write("Generated Unit Tests:")
            st.code(test_code)

        except Exception as e:
            st.error(f"An error occurred: {e}")