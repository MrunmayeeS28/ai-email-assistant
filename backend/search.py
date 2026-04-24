from sentence_transformers import SentenceTransformer, util

# 🔥 load model once (lazy loading)
model = None

def load_model():
    global model
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model


# 🔖 Tagging function
def get_tag(email):
    subject = email.get("subject", "").lower()
    body = email.get("body", "").lower()

    job_keywords = ["job", "opportunity", "hiring"]
    internship_keywords = ["internship", "intern"]
    shopping_keywords = ["order", "delivery", "shipment"]

    if any(word in subject for word in internship_keywords):
        return "Internship"
    elif any(word in subject for word in job_keywords):
        return "Job"
    elif any(word in subject for word in shopping_keywords):
        return "Shopping"

    if any(word in body for word in internship_keywords):
        return "Internship"
    elif any(word in body for word in job_keywords):
        return "Job"
    elif any(word in body for word in shopping_keywords):
        return "Shopping"

    return "General"


# 🔍 MAIN SEARCH FUNCTION
def search_emails(query_data, emails):
    query = query_data.get("raw_query", "")
    important_keywords = query_data.get("keywords", [])

    model = load_model()

    # 🔥 Encode query
    query_embedding = model.encode(query, convert_to_tensor=True)

    # 🔥 Prepare email text
    email_texts = [
        (email.get("subject", "") + " " + email.get("body", ""))
        for email in emails
    ]

    # 🔥 Encode all emails
    email_embeddings = model.encode(email_texts, convert_to_tensor=True)

    results = []

    # 🔥 Define word categories
    generic_words = {"developer", "engineer", "job", "internship", "candidate"}
    ignore_words = {"year", "years", "experience"}

    for i, email in enumerate(emails):
        score = util.cos_sim(query_embedding, email_embeddings[i]).item()

        text = email_texts[i].lower()

        # 🔥 clean keywords
        specific_keywords = [
            k for k in important_keywords
            if k not in generic_words
            and k not in ignore_words
            and not k.isdigit()
        ]

        # 🔥 strict only for important keywords
        if specific_keywords:
            keyword_match = all(k in text for k in specific_keywords)
        else:
            keyword_match = True   # no strict filtering

        # 🔥 boost if keyword present
        if any(k in text for k in important_keywords):
            score += 0.2

        # 🔥 final filter
        if score > 0.4 and keyword_match:

            body = email.get("body", "")
            preview = body[:150] + "..." if len(body) > 150 else body

            email["preview"] = preview
            email["tag"] = get_tag(email)

            results.append((score, email))

    # 🔥 sort by best match
    results.sort(reverse=True, key=lambda x: x[0])

    return [r[1] for r in results]