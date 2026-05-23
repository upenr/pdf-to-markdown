import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()

st.set_page_config(page_title="PDF to Markdown", page_icon="📄", layout="centered")

st.title("📄 PDF to Markdown Converter")
st.write("Upload a PDF and convert it into Markdown using a backend PDF extraction API.")

api_key = os.getenv("LLAMA_CLOUD_API_KEY")

if not api_key:
    st.error("Missing LLAMA_CLOUD_API_KEY. Add it to your .env file.")
    st.stop()

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.info(f"Uploaded: {uploaded_file.name}")

    if st.button("Convert to Markdown"):
        with st.spinner("Converting PDF to Markdown..."):
            try:
                # Save uploaded PDF temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name

                # Send PDF to backend API
                parser = LlamaParse(
                    api_key=api_key,
                    result_type="markdown",
                    verbose=True,
                    language="en"
                )

                documents = parser.load_data(tmp_path)

                # Combine pages/chunks into one Markdown string
                markdown_output = "\n\n".join(
                    doc.text for doc in documents if doc.text
                )

                os.remove(tmp_path)

                if not markdown_output.strip():
                    st.warning("No Markdown content was returned.")
                else:
                    st.success("Conversion complete!")

                    st.subheader("Markdown Preview")
                    st.markdown(markdown_output)

                    st.download_button(
                        label="Download Markdown",
                        data=markdown_output,
                        file_name=uploaded_file.name.replace(".pdf", ".md"),
                        mime="text/markdown"
                    )

            except Exception as e:
                st.error(f"Conversion failed: {e}")