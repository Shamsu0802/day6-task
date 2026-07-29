from app.retriever import retrieve_documents
from app.generator import generate_answer


def ask_kb(request):
    retrieved_docs = retrieve_documents(request.question)

    answer = generate_answer(
        request.question,
        retrieved_docs
    )

    return {
        "question": request.question,
        "answer": answer,
        "retrieved_doc_ids": [
            doc["doc_id"]
            for doc in retrieved_docs
        ]
    }