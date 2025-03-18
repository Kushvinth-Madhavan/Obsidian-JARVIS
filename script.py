import os
import time
import git
import chromadb
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Configurations
OBSIDIAN_VAULT = "/Users/MacbookPro/localStorage/Mastering"
GITHUB_REPO = "/Users/MacbookPro/localStorage/DevDirectory/OBSIDIAN-RAG"
MODEL_NAME = "all-MiniLM-L6-v2"
DB_PATH = "./chroma_db"

# Initialize ChromaDB and Embedding Model
chroma_client = chromadb.PersistentClient(DB_PATH)
collection = chroma_client.get_or_create_collection(name="obsidian_notes", embedding_function=SentenceTransformerEmbeddingFunction(MODEL_NAME))
embedder = SentenceTransformer(MODEL_NAME)

# FastAPI Setup
app = FastAPI()

# GitHub Sync Function
def sync_with_github():
    repo = git.Repo(GITHUB_REPO)
    repo.git.add(A=True)
    repo.index.commit("Auto-update Obsidian notes")
    origin = repo.remote(name="origin")
    origin.push()
    print("Synced with GitHub")

# Function to Process and Index Notes
def process_notes():
    for root, _, files in os.walk(OBSIDIAN_VAULT):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                embedding = embedder.encode(content).tolist()
                collection.add(ids=[file], embeddings=[embedding], documents=[content])
    print("Notes indexed in ChromaDB")

# Watchdog Event Handler
class ObsidianEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            print(f"File modified: {event.src_path}")
            process_notes()
            sync_with_github()

# FastAPI Route for Chatbot
@app.get("/query")
def query_notes(query: str):
    query_embedding = embedder.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=5)
    return {"results": results["documents"][0] if results else "No relevant notes found"}

# Start File Watcher
def start_watcher():
    event_handler = ObsidianEventHandler()
    observer = Observer()
    observer.schedule(event_handler, OBSIDIAN_VAULT, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    process_notes()  # Initial Indexing
    sync_with_github()
    start_watcher()


