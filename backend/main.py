import os
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF

app = FastAPI()

# Enable CORS to prevent frontend issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-resumes/")
async def upload_resumes(files: List[UploadFile] = File(...)):
    uploaded_files = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        uploaded_files.append(file.filename)
    return {"results": uploaded_files}

@app.post("/match-resumes/")
async def match_resumes_endpoint(
    job_description: str = Form(...),
    filenames: List[str] = Form(...)
):
    resume_paths = [os.path.join(UPLOAD_DIR, filename) for filename in filenames]
    if not resume_paths:
        raise HTTPException(status_code=400, detail="No resumes found")

    results = match_resumes(resume_paths, job_description)

    ec2_ip = "13.233.159.45"
    for result in results["results"]:
        result["file_url"] = f"http://{ec2_ip}:8000/view-resume/{result['filename']}"
    
    return results

@app.get("/view-resume/{filename}")
async def view_resume(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/pdf")
    return {"error": "File not found"}

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return " ".join(page.get_text("text") for page in doc)

def match_resumes(resume_paths, job_description):
    job_desc_text = job_description.lower()
    resume_texts = [extract_text_from_pdf(resume).lower() for resume in resume_paths]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([job_desc_text] + resume_texts)
    similarity_scores = cosine_similarity(vectors[0], vectors[1:]).flatten()

    results = [{"filename": os.path.basename(resume_paths[i]), "match_score": round(score * 100, 2)}
               for i, score in enumerate(similarity_scores)]
    
    return {"results": results}
