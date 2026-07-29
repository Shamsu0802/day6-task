# Integration Report

## Project Overview

In this task, I integrated the solutions I developed during Day 3, Day 4, and Day 5 into a single FastAPI application. Instead of maintaining them as separate projects, I organized everything into one project and exposed each functionality through its own API endpoint.

The application now provides three services:

- Customer Churn Prediction
- Ticket Classification
- Knowledge Base Question Answering (RAG)

---

# Components Used

## Day 3 – Customer Churn Prediction

For the churn prediction endpoint, I reused the model that I trained during Day 3. I loaded the saved `churn_model.pkl` along with the preprocessing pipeline that was created during training.

The endpoint accepts customer information and predicts whether the customer is likely to churn.

**Endpoint**

```
POST /predict/churn
```

I did not use any external model or fallback model for this task. The original Day 3 model was used directly.

---

## Day 4 – Ticket Classification

For ticket classification, I reused my Day 4 implementation. The same zero-shot prompt, validation logic, and Groq Llama model were integrated into the FastAPI application.

The endpoint classifies every support ticket into:

- Category
- Urgency
- Sentiment

**Endpoint**

```
POST /tickets/classify
```

I did not replace the classifier with any other model.

---

## Day 5 – Retrieval Augmented Generation (RAG)

For the RAG endpoint, I reused the retrieval pipeline built during Day 5.

The same Sentence Transformer model, FAISS index, knowledge base documents, and Groq LLM were integrated into the application.

**Endpoint**

```
POST /kb/ask
```

The endpoint retrieves the most relevant documents from the knowledge base and generates an answer using the retrieved context.

---

# Components Reused and Fallbacks

The project mainly uses the original components that I built during the previous tasks.

| Component | Original Component Used | Fallback |
|------------|-------------------------|----------|
| Churn Prediction | Yes | None |
| Ticket Classification | Yes | Default response if API fails |
| RAG Retrieval | Yes | None |
| RAG Answer Generation | Yes | User-friendly error message |

No replacement models or external fallback artifacts were used. Fallbacks were only added to handle runtime failures.

---

# Retry and Fallback Logic

Both the ticket classification endpoint and the RAG endpoint depend on an external LLM service.

To make the application more reliable, I added retry logic. If an API request fails because of temporary issues like network problems or service unavailability, the application retries the request up to **three times**.

If the ticket classification request still fails after all retries, the API returns a default response instead of crashing.

Example fallback:

- Category: General Inquiry
- Urgency: Low
- Sentiment: Neutral

Similarly, if the RAG endpoint cannot generate a response after all retry attempts, it returns a simple message indicating that the language model service is temporarily unavailable.

This ensures that users receive a meaningful response even if the external service is unavailable.

---

# Input Validation

I added request validation using Pydantic models for all API endpoints.

The validations include:

- Required fields
- Positive numeric values
- Valid categorical values
- Non-empty text fields
- Correct input data types

Invalid requests are rejected before reaching the business logic, and FastAPI automatically returns validation errors.

---

# Logging

I added request logging using FastAPI middleware.

The logs include:

- Request path
- HTTP method
- Response status
- Processing time

This makes it easier to debug issues and monitor API requests.

---

# Edge Cases Tested

## Churn Prediction

I tested:

- Missing fields
- Invalid customer age
- Invalid categorical values
- Negative numeric values

These cases are handled through request validation.

---

## Ticket Classification

I tested:

- Empty ticket text
- Invalid request format
- Temporary API failures
- Invalid responses returned by the LLM

These situations are handled using retries, validation, and fallback responses.

---

## RAG Endpoint

I tested:

- Empty questions
- Questions that do not match any relevant document
- Temporary LLM failures

The endpoint either retrieves the best available context or returns a user-friendly fallback message.

---

# Testing

I wrote unit tests for the main API endpoints.

The tests cover:

- Health endpoint
- Churn prediction endpoint
- Ticket classification endpoint
- Knowledge base endpoint

All implemented tests passed successfully.

---

# What I Would Improve

If I had more time, I would improve the project further by adding:

- Authentication and authorization
- Rate limiting
- Better monitoring and logging
- More unit and integration tests
- CI/CD pipeline
- Containerized deployment after resolving my local WSL environment issue
- Better error reporting and monitoring

---

# Incremental Progress

## Day 3

- Built and trained the customer churn prediction model.
- Saved the trained model and preprocessing pipeline.

## Day 4

- Built the ticket classification pipeline using Groq.
- Added prompt engineering and response validation.

## Day 5

- Built the RAG pipeline using Sentence Transformers, FAISS, and Groq.

## Day 6

- Integrated all three previous tasks into a single FastAPI application.
- Created separate API routes for each component.
- Added request validation using Pydantic.
- Added retry and fallback logic for external API calls.
- Added structured logging for incoming requests.
- Wrote unit tests for the API endpoints.
- Organized the project into a reusable and maintainable structure.

---

# Conclusion

This project combines the work completed during Day 3, Day 4, and Day 5 into a single FastAPI application. I reused my original implementations for churn prediction, ticket classification, and the RAG pipeline without replacing them with external alternatives. During the integration, I focused on making the APIs more reliable by adding request validation, retry logic, fallback handling, logging, and unit testing. Overall, the application is now organized as a single service that exposes all three functionalities through separate API endpoints.