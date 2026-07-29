import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(
    os.path.join(BASE_DIR, "faiss_index.index")
)

# Load document metadata
with open(os.path.join(BASE_DIR, "documents.pkl"), "rb") as f:
    documents = pickle.load(f)


def retrieve_documents(query, k=3):
    """
    Retrieve top-k most relevant documents for a given query.
    """

    # Convert query into embedding
    query_embedding = model.encode([query], convert_to_numpy=True)

    # Search FAISS
    distances, indices = index.search(query_embedding, k)

    retrieved_docs = []

    for distance, idx in zip(distances[0], indices[0]):
        retrieved_docs.append({
            "doc_id": documents[idx]["doc_id"],
            "title": documents[idx]["title"],
            "content": documents[idx]["content"],
            "distance": float(distance)
        })

    return retrieved_docs


# Test the retriever
if __name__ == "__main__":

    query = input("Enter your question: ")

    results = retrieve_documents(query)

    print("\nTop Retrieved Documents\n")

    for doc in results:
        print("-" * 50)
        print("Document ID :", doc["doc_id"])
        print("Title       :", doc["title"])
        print("Distance    :", round(doc["distance"], 4))
        print("Content     :", doc["content"])