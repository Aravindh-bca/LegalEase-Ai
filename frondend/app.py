import os
from datetime import date

import requests
import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.services.formatters import (
    format_docx,
    format_html_preview,
    format_pdf,
    format_txt,
)


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000",
)


st.set_page_config(
    page_title="LegalEase",
    page_icon="L",
    layout="wide",
)


# -----------------------------
# CSS
# -----------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #777;
        margin-top: 4px;
    }

    .preview {
        background: #171717;
        color: #f2f2f2;
        padding: 28px;
        border-radius: 14px;
        max-height: 650px;
        overflow-y: auto;
        line-height: 1.65;
    }

    .preview h3 {
        color: white;
        margin-top: 22px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="main-title">LegalEase</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Generator</div>',
    unsafe_allow_html=True,
)

st.info(
    "LegalEase creates general legal-document templates. "
    "It is not a substitute for advice from a qualified legal professional."
)


# -----------------------------
# Session State
# -----------------------------

if "document" not in st.session_state:
    st.session_state.document = ""

if "doc_type" not in st.session_state:
    st.session_state.doc_type = "Employment Contract"


# -----------------------------
# Layout
# -----------------------------

left, right = st.columns(
    [1, 1.25],
    gap="large",
)


# =============================
# LEFT SIDE
# =============================

with left:

    st.subheader("1. Document Details")

    document_type = st.selectbox(
        "Document Type",
        [
            "Employment Contract",
            "Non-Disclosure Agreement (NDA)",
            "Lease Agreement",
            "Freelance Work Contract",
            "Service Agreement",
            "Employment Offer Letter",
            "General Agreement",
        ],
    )

    parties = st.text_area(
        "Parties Involved",
        placeholder=(
            "Example:\n"
            "Jane Doe (Employee), "
            "ABC Technologies Pvt Ltd (Employer)"
        ),
        height=120,
    )

    terms = st.text_area(
        "Terms & Conditions",
        placeholder=(
            "Use semicolons between terms.\n\n"
            "Payment within 30 days; "
            "Confidentiality must be maintained; "
            "Either party may terminate with "
            "15 days notice"
        ),
        height=180,
    )

    effective_date = st.date_input(
        "Effective Date",
        value=date.today(),
        format="DD/MM/YYYY",
    )

    generate = st.button(
        "Generate Document",
        type="primary",
        use_container_width=True,
    )

    if generate:

        if not parties.strip():

            st.error("Please enter the parties.")

        elif not terms.strip():

            st.error("Please enter the terms.")

        else:

            data = {
                "document_type": document_type,
                "parties": parties,
                "terms": terms,
                "dates": effective_date.strftime("%d/%m/%Y"),
            }

            try:

                with st.spinner("Generating document..."):

                    response = requests.post(
                        f"{BACKEND_URL}/generate",
                        json=data,
                        timeout=120,
                    )

                if response.ok:

                    result = response.json()

                    st.session_state.document = result["content"]

                    st.session_state.doc_type = result[
                        "document_type"
                    ]

                    st.success(
                        "Document generated successfully!"
                    )

                else:

                    try:

                        message = response.json().get(
                            "detail",
                            response.text,
                        )

                    except Exception:

                        message = response.text

                    st.error(
                        f"Backend error: {message}"
                    )

            except requests.RequestException as error:

                st.error(
                    "Cannot connect to FastAPI."
                )

                st.caption(str(error))


# =============================
# RIGHT SIDE
# =============================

with right:

    st.subheader("2. Preview & Edit")

    if st.session_state.document:

        preview_tab, edit_tab = st.tabs(
            [
                "Preview",
                "Edit",
            ]
        )

        # -------------------------
        # Preview
        # -------------------------

        with preview_tab:

            preview = format_html_preview(
                st.session_state.document
            )

            st.markdown(
                f"""
                <div class="preview">
                    {preview}
                </div>
                """,
                unsafe_allow_html=True,
            )

        # -------------------------
        # Edit
        # -------------------------

        with edit_tab:

            edited_document = st.text_area(
                "Edit your document",
                value=st.session_state.document,
                height=620,
            )

            if st.button(
                "Save Edits",
                use_container_width=True,
            ):

                st.session_state.document = edited_document

                st.success(
                    "Changes saved."
                )

        st.divider()

        # -------------------------
        # Downloads
        # -------------------------

        st.subheader("3. Download Document")

        content = st.session_state.document

        filename = "".join(
            character.lower()
            if character.isalnum()
            else "_"
            for character in st.session_state.doc_type
        )

        filename = filename.strip("_")

        col1, col2, col3 = st.columns(3)

        # TXT
        with col1:

            st.download_button(
                "Download TXT",
                data=format_txt(content),
                file_name=f"{filename}.txt",
                mime="text/plain",
                use_container_width=True,
            )

        # DOCX
        with col2:

            st.download_button(
                "Download DOCX",
                data=format_docx(content),
                file_name=f"{filename}.docx",
                mime=(
                    "application/"
                    "vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                ),
                use_container_width=True,
            )

        # PDF
        with col3:

            st.download_button(
                "Download PDF",
                data=bytes(format_pdf(content)),
                file_name=f"{filename}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    else:

        st.write(
            "Your generated document will appear here."
        )

        st.caption(
            "Enter the details on the left "
            "and click Generate Document."
        )