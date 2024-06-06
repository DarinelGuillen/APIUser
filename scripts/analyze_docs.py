import spacy

nlp = spacy.load('en_core_web_sm')

def analyze_text(text):
    doc = nlp(text)
    for entity in doc.ents:
        print(f'{entity.text}: {entity.label_}')

# Ejemplo de uso
text = """
GET /users - Retrieves a list of users.
POST /users - Creates a new user.
"""
analyze_text(text)
