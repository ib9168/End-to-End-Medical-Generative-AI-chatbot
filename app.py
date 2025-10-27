
#Updating the file for deployement on Render from AWS
print("Starting Flask...")

from flask import Flask,render_template,jsonify,request
from src.helper import download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone
from langchain_mistralai import ChatMistralAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

#initialising the flask

app=Flask(__name__)
#loads environment variable from the .env file
load_dotenv()

#initialising api keys for the DB and LLM
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
MISTRAL_API_KEY=os.environ.get('MISTRAL_API_KEY')

os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY
os.environ["MISTRAL_API_KEY"]=MISTRAL_API_KEY

embeddings=download_hugging_face_embedding()

#Loading existing index:
#Embed each chunk and upsert the embeddings into Pinecone
docsearch=Pinecone.from_existing_index(index_name="medicalbot",embedding=embeddings)

#To retrive info from the knowledge base--the vector store
retriever=docsearch.as_retriever(search_type="similarity",search_kwargs={"k":3})#It will show 3 relevant answers to the query

llm = ChatMistralAI(
    model="open-mistral-7b",  # or "mistral-medium" / "mistral-large" if available
    mistral_api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.4,
    max_tokens=500
)

prompt=ChatPromptTemplate.from_messages(
    [
    ("system",system_prompt),
    ("human","{input}"),
    ]

)

question_answer_chain=create_stuff_documents_chain(llm,prompt)
rag_chain=create_retrieval_chain(retriever,question_answer_chain)

#Default route:for the user to get the interface of the app
@app.route("/")
def index():
    return render_template('chat.html')

#route for chat operation:
@app.route("/ask",methods=["POST"])
def ask():
    # msg=request.form["msg"]#the query
    # input=msg
    # print(input)
    # response=rag_chain.invoke({"input:":msg})
    # print("Response : ",response["answer"])
    # return str(response["answer"])
    data = request.get_json()  # 🔹 Extract JSON from request body
    user_input = data.get("query", "")  # 🔹 Get 'query' key from the JSON
    
    if not user_input:
        return jsonify({"answer": "⚠️ Please provide a valid question."})  # 🛑 Handles empty queries

    print("User:", user_input)

    #  Passes the user query to the RAG chain to get a response
    response = rag_chain.invoke({"input": user_input})
    print("Response:", response["answer"])

    return jsonify({"answer": response["answer"]})  # ✅ Return answer as JSON for frontend

#running app on local host.Disabling debug on production in Render
if __name__=='__main__':
    #app.run(host="0.0.0.0",port=8080,debug=True)
    import os
    port=int(ps.environ.get('PORT',8080))
    app.run(host='0.0.0',port=port,debug=False)
