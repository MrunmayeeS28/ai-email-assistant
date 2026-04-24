# import re

# def extract_query(query):
#     original_query = query
#     query = query.lower()

#     # remove special characters
#     query = re.sub(r'[^a-z0-9\s]', '', query)

#     words = query.split()

#     stop_words = {
#         "show","me","give","all","mails","emails",
#         "related","about","with","and","the","a","an",
#         "for","of","to","who","are","in","on"
#     }

#     # 🔥 keep meaningful words only
#     keywords = [w for w in words if w not in stop_words and len(w) > 2]

#     return {
#         "keywords": keywords,
#         "raw_query": original_query
#     }

import re

def extract_query(query):
    original_query = query
    query = query.lower()

    # remove special characters
    query = re.sub(r'[^a-z0-9\s]', '', query)

    words = query.split()

    stop_words = {
        "show","me","give","all","mails","emails",
        "related","about","with","and","the","a","an",
        "for","of","to","who","are","in","on"
    }

    # 🔥 keywords (your original logic)
    keywords = [w for w in words if w not in stop_words and len(w) > 2]

    # -------------------------------
    # 🔥 SIMPLE STRUCTURED NLP
    # -------------------------------

    # Role (very basic)
    role = None
    if "developer" in words:
        idx = words.index("developer")
        if idx > 0:
            role = words[idx-1] + " developer"
        else:
            role = "developer"

    # Skills (dynamic — no hardcoding list)
    skills = [w for w in keywords if w not in ["developer", "experience", "years"]]

    # Experience
    experience = None
    match = re.search(r'(\d+)\s*(year|years)', query)
    if match:
        experience = match.group(1)

    # -------------------------------

    return {
        "role": role,
        "skills": skills,
        "experience": experience,
        "keywords": keywords,
        "raw_query": original_query
    }