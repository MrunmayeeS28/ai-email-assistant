import re

SKILLS = ["python","java","react","node","mongodb","html","css","javascript"]

def extract_query(query):
    query = query.lower()
    
    skills = []
    role = None
    experience = None
    
    # #for deteccting skills (first Testing)
    # if "react" in query:
    #     skills.append("react")
    # if "python" in query:
    #     skills.append("python")
    # if "java" in query:
    #     skills.append("java")
    
    for skill in SKILLS:
        if skill in query:
            skills.append(skill)
        
    #detecting role 
    if "developer" in query:
        role = "developer"
        
    #deteccting experience
    exp_match = re.search(r'\d+',query)
    if exp_match:
        experience = exp_match.group()
        
    return{
        "skills" : skills,
        "role" : role,
        "experience" : experience,
        "raw_query": query.lower()
        
    }