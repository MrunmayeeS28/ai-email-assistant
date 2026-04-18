import re

def extract_query(query):
    query = query.lower()

    # 🔥 normalize text
    query = query.replace("-", " ")   # full-stack → full stack

    role = None
    skills = []
    experience = None

    words = query.split()

    # 🔹 ROLE detection (based on words)
    role_keywords = ["developer", "engineer", "intern", "analyst"]

    for word in words:
        if word in role_keywords:
            role = word

    # 🔹 SKILL detection (word-based, not exact match)
    skill_keywords = ["java", "python", "react", "node", "fullstack", "full stack", "frontend", "backend"]

    for skill in skill_keywords:
        if skill in query:
            skills.append(skill.replace(" ", ""))  # full stack → fullstack

    # 🔹 EXPERIENCE detection (regex NLP)
    exp_match = re.search(r'(\d+)\s*(year|years)', query)
    if exp_match:
        experience = exp_match.group(1)

    return {
        "role": role,
        "skills": skills,
        "experience": experience,
        "raw_query": query
    }# import re

# def extract_query(query):
#     query = query.lower()

#     role = None
#     skills = []
#     experience = None

#     # 🔹 Extract role (generic pattern)
#     role_keywords = ["developer", "engineer", "intern", "analyst"]

#     for word in role_keywords:
#         if word in query:
#             role = word

#     # 🔹 Extract experience (regex-based NLP)
#     exp_match = re.search(r'(\d+)\s*(year|years)', query)
#     if exp_match:
#         experience = exp_match.group(1)

#     # 🔹 Extract skills (based on known tech words)
#     skill_keywords = ["java", "python", "react", "node", "fullstack", "frontend", "backend"]

#     for skill in skill_keywords:
#         if skill in query:
#             skills.append(skill)

#     return {
#         "role": role,
#         "skills": skills,
#         "experience": experience,
#         "raw_query": query
#     }# import re

# SKILLS = ["python","java","react","node","mongodb","html","css","javascript"]

# def extract_query(query):
#     query = query.lower()
    
#     skills = []
#     role = None
#     experience = None
    
#     # #for deteccting skills (first Testing)
#     # if "react" in query:
#     #     skills.append("react")
#     # if "python" in query:
#     #     skills.append("python")
#     # if "java" in query:
#     #     skills.append("java")
    
#     for skill in SKILLS:
#         if skill in query:
#             skills.append(skill)
        
#     #detecting role 
#     if "developer" in query:
#         role = "developer"
        
#     #deteccting experience
#     exp_match = re.search(r'\d+',query)
#     if exp_match:
#         experience = exp_match.group()
        
#     return{
#         "skills" : skills,
#         "role" : role,
#         "experience" : experience,
#         "raw_query": query.lower()
        
#     }