from fastapi import FastAPI, HTTPException, Form
import spacy

app = FastAPI()

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

@app.post("/ner")
async def extract_entities(text: str = Form(...)):
    """
    Endpoint to extract named entities from the provided text.
    """
    try:
        # Process the input text with the spaCy NER model
        doc = nlp(text)

        # Extract named entities
        entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_}
                    for ent in doc.ents]

        return {"entities": entities}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
