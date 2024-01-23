#!/bin/bash
pip install spacy
pip install python-multipart
python -m spacy download en_core_web_sm
pip install fastapi uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 &
sleep infinity
