from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.generator import generate_legal_document


router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.get("/")
def home():
    return {"message": "LegalEase Backend is running"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/generate")
def generate_document(data: DocumentRequest):

    content = generate_legal_document(
        document_type=data.document_type,
        parties=data.parties,
        terms=data.terms,
        effective_date=data.dates
    )

    return {
        "document_type": data.document_type,
        "content": content
    }