def generate_legal_document(
    document_type: str,
    parties: str,
    terms: str,
    effective_date: str
) -> str:

    document = f"""
{document_type}

Effective Date: {effective_date}

PARTIES
{parties}

TERMS AND CONDITIONS
{terms}

AGREEMENT

Both parties agree to the terms and conditions
mentioned in this document.

This document is a general legal template and
should be reviewed by a qualified legal professional
before use.
"""

    return document.strip()