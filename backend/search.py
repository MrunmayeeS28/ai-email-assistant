import re

def get_tag(email):
    text = email["body"].lower()
    
    if "experience" in text or "developer" in text:
        return "Candidate"
    elif "internship" in text:
        return "Internship"
    else:
        return "General"


def search_emails(query_data, emails):
    results = []
    
    #Get raw query
    query_text = query_data.get("raw_query", "").lower()
    
    #Clean query (remove punctuation)
    query_text = re.sub(r'[^a-z0-9\s]', '', query_text)
    
    #Remove stop words
    stop_words = {
        "show", "me", "with", "and", "the", "a", "an",
        "for", "of", "to", "candidates", "please"
    }
    
    query_words = [w for w in query_text.split() if w not in stop_words]
    
    for email in emails:
        score = 0
        
        subject = email["subject"].lower()
        body = email["body"].lower()
        
        #Role matching
        if query_data["role"]:
            if query_data["role"] in subject:
                score += 4
            elif query_data["role"] in body:
                score += 3
        
        #Skill matching
        for skill in query_data["skills"]:
            if skill in subject:
                score += 6
            elif skill in body:
                score += 4
        
        # Experience matching
            if query_data["experience"]:
                exp = query_data["experience"]
    
                # match patterns like: 2 years, 2 year, 2+ years
                pattern = rf"\b{exp}\+?\s*(year|years)\b"
    
                if re.search(pattern, subject) or re.search(pattern, body):
                    score += 4  
        
        #Full-text matching (important for long queries)
        for word in query_words:
            if word in subject:
                score += 3
            elif word in body:
                score += 2
        
        #Strong fallback match (ensures results for long queries)
        if any(word in subject or word in body for word in query_words):
            score += 3
        
        #Add only relevant emails
        if score >= 2:
            preview = body[:150] + "..." if len(body) > 150 else body
            
            email["preview"] = preview
            email["tag"] = get_tag(email)
            
            results.append((score, email))
    
    #Sort by relevance
    results.sort(reverse=True, key=lambda x: x[0])
    
    return [r[1] for r in results]
