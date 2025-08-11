import re
import string
from sentence_transformers import SentenceTransformer, util
from difflib import SequenceMatcher

model = SentenceTransformer("all-MiniLM-L6-v2")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[()\/\-]", " ", text)  # unify separators
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

def load_skill_list(filepath="data/skills.txt"):
    with open(filepath, "r") as f:
        return [clean_text(line.strip()) for line in f if line.strip()]

def split_into_chunks(text):
    raw_chunks = re.split(r"[/,.\n]", text)
    return [clean_text(chunk) for chunk in raw_chunks if chunk.strip()]

def fuzzy_match(a, b, threshold=0.85):
    """Simple fuzzy match using ratio."""
    return SequenceMatcher(None, a, b).ratio() >= threshold

def extract_skills_semantic(text, top_n=30, threshold=0.4):
    skills = load_skill_list()
    chunks = split_into_chunks(text)
    if not chunks:
        return []

    # Step 1: Exact or fuzzy matches
    exact_matches = set()
    remaining_skills = []
    for skill in skills:
        if any(skill in chunk or fuzzy_match(skill, chunk) for chunk in chunks):
            exact_matches.add(skill)
        else:
            remaining_skills.append(skill)

    # Step 2: Semantic matching only on unmatched skills
    matched_semantic = []
    if remaining_skills:
        skill_embeddings = model.encode(remaining_skills, convert_to_tensor=True)
        chunk_embeddings = model.encode(chunks, convert_to_tensor=True)
        for i, skill_embedding in enumerate(skill_embeddings):
            scores = util.cos_sim(skill_embedding, chunk_embeddings)[0]
            max_score = scores.max().item()
            if max_score >= threshold:
                matched_semantic.append(remaining_skills[i])

    # Combine & sort
    final_matches = sorted(exact_matches.union(matched_semantic))
    return final_matches[:top_n]
