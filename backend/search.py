def get_tag(email):
    text = email["body"].lower()
    
    if "experience" in text or "delevoper" in text:
        return "Candidate"
    elif "internship" in text:
        return "Internship"
    else:
        return "General"
    

def search_emails(query_data,emails):
    results = []
    
    for email in emails:
        score = 0
        subject = email["subject"].lower()
        body = email["body"].lower()
        
        #matching role
        if query_data["role"]:
            if query_data["role"] in subject:
                score = score + 3
            elif query_data["role"] in body:
                score = score + 2
            
        #matching skill
        for skill in query_data["skills"]:
            if skill in subject:
                score = score + 5
            elif skill in body:
                score = score + 3
                
        #matching experience
        if query_data["experience"] and query_data["experience"] in body:
            score = score + 1
            
        # if query_data["skills"]:
        #     skill_match = any(skill in subject or skill in body for skill in query_data["skills"])
        #     if not skill_match:
        #         continue
        if query_data["skills"]:
            skill_match = any(skill in subject or skill in body for skill in query_data["skills"])
            if skill_match:
                score += 2
            
        
        email["tag"] = get_tag(email)
        results.append((score,email))
            
    #highest score sorted
    results.sort(reverse=True, key=lambda x: x[0])
            
    return [r[1] for r in results]























