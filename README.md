# PopcornSearch: Specialized Movie Search Engine

An architecture-focused specialized search engine built from scratch in Python using a custom-implemented Inverted Index, Boolean Retrieval framework, and TF-IDF Vector Space Model ranking. This project indexes and queries the classical TMDB 5000 Movies dataset over a dynamic web interface without relying on any pre-built search or indexing libraries (such as Elasticsearch, Lucene, or Whoosh).

## 🚀 Features

* **Custom Inverted Index:** Maps unique terms dynamically extracted from text fields to their respective Document IDs and local frequencies.
* **Dual-Pass Optimization:** Precomputes structural document vector lengths efficiently to avoid expensive runtime calculations, optimizing multi-word query scalability.
* **Boolean Filtering Engine:** Supports structural logic routing for multi-word queries via Set Intersections (AND clauses) or Set Unions (OR clauses).
* **TF-IDF Vector Space Model Ranking:** Computes Cosine Similarity scores between query vectors and document vectors to ensure high-precision ranking relevance.
* **Modern Web GUI Dashboard:** A Google-inspired interface engineered using Streamlit, featuring title rendering, descriptive context snippets, relevance metadata, and keyword highlighting.

---

## 🛠️ System Architecture

The search platform separates pipeline execution into three decoupled stages:

1.  **Ingestion & Preprocessing:** Reads the TMDB 5000 Movies dataset. Text attributes (title, tagline, overview, and keywords) are cleaned, low-cased, and converted into clean alphanumeric tokens via regular expressions.
2.  **Indexing Engine:** Builds map structures using a Python nested Hash Map (dict). It tracks local term frequency alongside aggregate document tracking bounds for computing inverse document frequencies.
3.  **Matching & Evaluation:** Intersects or joins index sets based on user settings, scores candidates via TF-IDF, and divides by pre-calculated Euclidean lengths to ensure document length normalization.

---

## 📦 Implementation Constraints & Libraries

Developed completely in compliance with strict academic framework constraints:
* **Language:** Python 3.8+
* **Allowed Frameworks:** Pandas, NumPy, Streamlit (for GUI delivery), and native re / math libraries.
* **Prohibited Implementations:** Zero pre-packaged indexing, text search, or token classification frameworks were utilized.

---

## 💻 Getting Started & Execution

### 1. Prerequisites
Ensure you have the required dependencies installed on your local setup:
```bash
pip install streamlit pandas numpy
