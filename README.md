This project is an AI-powered medical assistant designed to provide accurate, human-understandable answers to general health-related questions. It leverages Generative AI, LangChain, and Mistral AI integrated with a semantic search database (Pinecone) to retrieve verified medical knowledge from trusted sources.

The chatbot’s knowledge base is derived from The Gale Encyclopedia of Medicine, a comprehensive resource that explains diseases, diagnoses, treatments, and prevention in language accessible to the general public.

#Purpose
The goal of this project is to make reliable medical information more accessible to everyday users, bridging the gap between professional medical literature and layperson understanding.
###Tech Stack###
	-Languages & Frameworks:
		*Python
		*Flask (for backend & API handling)
		*LangChain (for building the retrieval and generation pipeline)
	-AI & Database Tools:
	  *Mistral AI (LLM for generating responses)
	  *Pinecone (Vector database for semantic search and document retrieval)
      *dotenv (for managing API keys and environment variables)
	-DevOps & Deployment:
		*AWS EC2 (for hosting and inference)
		*AWS ECR (for Docker image management)
		*GitHub Actions (for CI/CD automation)
		*Docker (for containerized deployment)
#Architecture Workflow

-Data Preparation: Extracted and cleaned text data from The Gale Encyclopedia of Medicine.

-Embedding Generation: Converted text into high-dimensional embeddings using download_hugging_face_embedding.

-Vector Storage: Indexed the embeddings in Pinecone for efficient semantic retrieval.

-Retrieval-Augmented Generation (RAG): Used LangChain to combine retrieved knowledge with Mistral AI’s generative capabilities.

-Backend Integration: Built a Flask server to process API requests and deliver chatbot responses in real time.

-CI/CD Deployment:

	-Automated Docker builds via GitHub Actions.
	-Deployed to AWS EC2 for production-level scalability.

#Deployment Workflow:
# Creates and activates the environment
conda create -n medibot python=3.10 -y
conda activate medibot

# Installing dependencies
pip install -r requirements.txt

# Setting my credentials
PINECONE_API_KEY="pinecone_key"
MISTRAL_API_KEY="mistral_key"

# Stores embeddings
python store_index.py

# Running the Flask app
python app.py
