# PopcornSearch: Specialized Movie Search Engine

[cite_start]An architecture-focused specialized search engine built from scratch in Python using a custom-implemented Inverted Index, Boolean Retrieval framework, and TF-IDF Vector Space Model ranking[cite: 1, 2, 4, 16, 23, 27]. [cite_start]This project indexes and queries the classical TMDB 5000 Movies dataset over a dynamic web interface without relying on any pre-built search or indexing libraries (such as Elasticsearch, Lucene, or Whoosh)[cite: 18, 39, 40, 69].

## 🚀 Features

* [cite_start]**Custom Inverted Index:** Maps unique terms dynamically extracted from text fields to their respective Document IDs and local frequencies[cite: 19, 20].
* **Dual-Pass Optimization:** Precomputes structural document vector lengths efficiently to avoid expensive runtime calculations, optimizing multi-word query scalability.
* [cite_start]**Boolean Filtering Engine:** Supports structural logic routing for multi-word queries via Set Intersections (`AND` clauses) or Set Unions (`OR` clauses)[cite: 22, 23, 31].
* [cite_start]**TF-IDF Vector Space Model Ranking:** Computes Cosine Similarity scores between query vectors and document vectors to ensure high-precision ranking relevance[cite: 27, 59].
* [cite_start]**Modern Web GUI Dashboard:** A Google-inspired interface engineered using Streamlit, featuring title rendering, descriptive context snippets, relevance metadata, and keyword highlighting[cite: 25, 28, 69, 70, 71, 74, 75, 76].

---

## 🛠️ System Architecture

The search platform separates pipeline execution into three decoupled stages:

1.  [cite_start]**Ingestion & Preprocessing:** Reads the TMDB 5000 Movies dataset[cite: 37]. [cite_start]Text attributes (`title`, `tagline`, `overview`, and `keywords`) are cleaned, low-cased, and converted into clean alphanumeric tokens via regular expressions[cite: 33, 38].
2.  **Indexing Engine:** Builds a map structures using a Python nested Hash Map (`dict`). It tracking local term frequency $tf_{t,d}$ alongside aggregate document tracking bounds for computing inverse document frequencies ($idf_t$).
3.  [cite_start]**Matching & Evaluation:** Intersects or joins index sets based on user settings[cite: 23], scores candidates via $\text{TF-IDF}$, and divides by pre-calculated Euclidean lengths to ensure document length normalization.

---

## 📦 Implementation Constraints & Libraries

[cite_start]Developed completely in compliance with strict academic framework constraints[cite: 32]:
* [cite_start]**Language:** Python 3.8+ [cite: 33]
* [cite_start]**Allowed Frameworks:** `Pandas`, `NumPy`, `Streamlit` (for GUI delivery), and native `re` / `math` libraries[cite: 34, 35, 37, 69].
* [cite_start]**Prohibited Implementations:** Zero pre-packaged indexing, text search, or token classification frameworks were utilized[cite: 18, 39, 40].

---

## 💻 Getting Started & Execution

### 1. Prerequisites
Ensure you have the required dependencies installed on your local setup:
```bash
pip install streamlit pandas numpy
