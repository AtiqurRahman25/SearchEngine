import streamlit as st
import pandas as pd
import math
import re
from collections import defaultdict

st.set_page_config(page_title="PopcornSearch", page_icon="🎬", layout="centered")

@st.cache_resource
def load_and_clean_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    df["overview"] = df["overview"].fillna("")
    df["tagline"] = df["tagline"].fillna("")
    df["keywords"] = df["keywords"].fillna("")
    df["searchable_text"] = (
        df["title"] + " " + df["tagline"] + " " + df["overview"] + " " + df["keywords"]
    )
    return df

df = load_and_clean_data()
N = len(df)

def preprocess_text(text):
    if not isinstance(text, str):
        return []
    return re.findall(r"\b\w+\b", text.lower())

@st.cache_resource
def build_search_structures():
    inverted_index = defaultdict(dict)
    doc_lengths = {}
    doc_frequencies = defaultdict(set)
    
    for _, row in df.iterrows():
        doc_id = int(row["id"])
        tokens = preprocess_text(row["searchable_text"])
        for token in tokens:
            inverted_index[token][doc_id] = inverted_index[token].get(doc_id, 0) + 1
            doc_frequencies[token].add(doc_id)
            
    for _, row in df.iterrows():
        doc_id = int(row["id"])
        tokens = preprocess_text(row["searchable_text"])
        unique_tokens = set(tokens)
        
        length_sq = 0
        for token in unique_tokens:
            if doc_id in inverted_index[token]:
                tf = inverted_index[token][doc_id]
                df_t = len(doc_frequencies[token])
                idf = math.log(N / (1 + df_t))
                length_sq += (tf * idf) ** 2
        doc_lengths[doc_id] = math.sqrt(length_sq) if length_sq > 0 else 1.0
        
    return inverted_index, doc_lengths

inverted_index, doc_lengths = build_search_structures()

def boolean_retrieval(query, operator):
    terms = preprocess_text(query)
    if not terms:
        return set()
    
    doc_sets = [set(inverted_index[term].keys()) for term in terms if term in inverted_index]
    if not doc_sets:
        return set()
        
    return set.intersection(*doc_sets) if operator == "AND" else set.union(*doc_sets)

def search_engine(query, operator):
    query_terms = preprocess_text(query)
    matched_docs = boolean_retrieval(query, operator)
    if not matched_docs:
        return []
        
    query_tf = {term: query_terms.count(term) for term in query_terms}
    scores = defaultdict(float)
    
    for term in query_terms:
        if term in inverted_index:
            df_t = len(inverted_index[term])
            idf = math.log(N / (1 + df_t))
            q_weight = query_tf[term] * idf
            
            for doc_id in matched_docs:
                if doc_id in inverted_index[term]:
                    scores[doc_id] += q_weight * (inverted_index[term][doc_id] * idf)
                    
    ranked_results = []
    for doc_id, score in scores.items():
        normalized_score = score / doc_lengths[doc_id]
        movie_row = df[df["id"] == doc_id].iloc[0]
        
        raw_overview = movie_row["overview"]
        snippet = raw_overview[:150] + "..." if len(raw_overview) > 150 else raw_overview
        
        ranked_results.append({
            "title": movie_row["title"],
            "tagline": movie_row["tagline"],
            "snippet": snippet,
            "score": round(normalized_score, 4)
        })
        
    return sorted(ranked_results, key=lambda x: x["score"], reverse=True)

st.title("🎬 PopcornSearch Dashboard")
st.write("A professional movie query system powered entirely by Md. Atiqur Rahman Sifat.")

query = st.text_input("", placeholder="Type keywords here (e.g., interstellar space black hole)...")

col1, _ = st.columns([2, 3])
with col1:
    operator = st.selectbox("Match Strategy", ["OR", "AND"])

st.markdown("---")

if query:
    results = search_engine(query, operator)
    
    if results:
        st.success(f"Found {len(results)} matching results ordered by ranking relevance:")
        
        for movie in results[:10]:
            snippet = movie["snippet"]
            
            for term in query.split():
                if len(term) > 2:
                    snippet = re.sub(f"({term})", r"**\1**", snippet, flags=re.IGNORECASE)
            
            st.markdown(f"### 🍿 {movie['title']}")
            if movie["tagline"]:
                st.markdown(f"*“{movie['tagline']}”*")
            st.markdown(snippet)
            st.caption(f"Relevance Similarity Score: {movie['score']}")
            st.markdown("---")
    else:
        st.warning("No matched records discovered. Try alternative terms or switch to 'OR' mode.")