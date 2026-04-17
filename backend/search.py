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
    
    # 🔥 raw query for full-text search
    query_text = query_data.get("raw_query", "").lower()
    query_words = query_text.split()
    
    for email in emails:
        score = 0
        subject = email["subject"].lower()
        body = email["body"].lower()
        
        # ✅ matching role
        if query_data["role"]:
            if query_data["role"] in subject:
                score += 3
            elif query_data["role"] in body:
                score += 2
            
        # ✅ matching skill
        for skill in query_data["skills"]:
            if skill in subject:
                score += 5
            elif skill in body:
                score += 3
                
        # ✅ matching experience
        if query_data["experience"] and query_data["experience"] in body:
            score += 1
            
        # ✅ skill bonus
        if query_data["skills"]:
            skill_match = any(skill in subject or skill in body for skill in query_data["skills"])
            if skill_match:
                score += 2
        
        # 🔥 FULL TEXT SEARCH (like Gmail)
        text_match_score = 0
        for word in query_words:
            if word in subject:
                text_match_score += 2
            elif word in body:
                text_match_score += 1
        
        score += text_match_score
        
        # ✅ Only add relevant emails
        if score > 0:
            preview = body[:150] + "..." if len(body) > 150 else body
            
            email["preview"] = preview   # 🔥 IMPORTANT
            email["tag"] = get_tag(email)
            
            results.append((score, email))
    
    # 🔥 sort by highest score
    results.sort(reverse=True, key=lambda x: x[0])
    
    
    return [r[1] for r in results]