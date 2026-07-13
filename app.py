
import os
from dotenv import load_dotenv
from huggingface_hub import login
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import streamlit as st
import tempfile

load_dotenv()
login(os.getenv("HUGGING FACE"))
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text=page.extract_text()
            if page_text:
                text+=page_text
    return text

def get_text_chunks(raw_text):
    text_splitter=CharacterTextSplitter(
        separator='\\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks=text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device":"cpu"}
)
    vectorstore=FAISS.from_texts(
        texts=text_chunks,
        embedding=embeddings
    )
    return vectorstore

template=""" You are a medical assistant. Using the following context, convert the medical report into a friendly summary for a patient.
Context:{context}
Medical Report:{question}
Summary:"""
prompt=PromptTemplate(
    input_variables=["context","question"],
    template=template,
)

llm = ChatGroq(
    temperature=0,
    model="meta-llama/llama-4-scout-17b-16e-instruct"
)

st.set_page_config(page_title="Medical Report Summarizer", page_icon="🩺")

st.title("🩺 Medical Report to Patient-Friendly Summary Generator")

uploaded_file = st.file_uploader("Upload your medical report PDF", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    st.success("✅ PDF uploaded successfully!")

    raw_text = get_pdf_text([pdf_path])
    st.write(f"✅ Extracted text length: {len(raw_text)}")

    text_chunks = get_text_chunks(raw_text)
    st.write(f"✅ Number of text chunks: {len(text_chunks)}")

    vectorstore = get_vectorstore(text_chunks)
    st.write("✅ Vectorstore created.")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

    if st.button("Generate Summary 📝"):
        with st.spinner("Generating summary... Please wait."):
            query = "summarize this medical report in simple terms"
            response = qa_chain.run(query)
        st.subheader("📄 Patient-Friendly Summary")
        st.success(response)

