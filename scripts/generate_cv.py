#!/usr/bin/env python3
"""Generate one-page CV PDF for Panos Kabasis with photo."""

import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
PHOTO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "profile", "DSC_0124ivol2.jpg")
PDF_PATH = os.path.join(PROJECT_ROOT, "assets", "docs", "cv", "cv.pdf")

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=letter,
    topMargin=0.35 * inch,
    bottomMargin=0.35 * inch,
    leftMargin=0.45 * inch,
    rightMargin=0.45 * inch,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("Name", parent=styles["Heading1"], fontSize=21, leading=23, fontName="Helvetica-Bold", textColor=colors.HexColor("#0b1f44"), spaceAfter=2))
styles.add(ParagraphStyle("Role", parent=styles["Normal"], fontSize=11, leading=13, textColor=colors.HexColor("#1d4ed8"), spaceAfter=5))
styles.add(ParagraphStyle("Meta", parent=styles["Normal"], fontSize=8.2, leading=10, textColor=colors.HexColor("#4b5563"), spaceAfter=0))
styles.add(ParagraphStyle("Section", parent=styles["Heading2"], fontSize=10.3, leading=12, fontName="Helvetica-Bold", textColor=colors.HexColor("#0f2f6b"), spaceBefore=6, spaceAfter=3))
styles.add(ParagraphStyle("Text", parent=styles["Normal"], fontSize=8.55, leading=10.3, textColor=colors.HexColor("#111827"), spaceAfter=1))
styles.add(ParagraphStyle("CvBullet", parent=styles["Text"], leftIndent=10))
styles.add(ParagraphStyle("JobTitle", parent=styles["Text"], fontName="Helvetica-Bold", spaceBefore=3, spaceAfter=1))

story = []

top_left = [
    Paragraph("PANOS KABASIS", styles["Name"]),
    Paragraph("DataOps Engineer | Azure, Databricks & Analytics Engineering", styles["Role"]),
    Paragraph("Frankfurt, Germany · panos.kabasis@gmail.com · (+30) 698 8120 621", styles["Meta"]),
    Paragraph("LinkedIn: linkedin.com/in/panos-kabasis-618b18264 · GitHub: github.com/UpBash", styles["Meta"]),
]

if os.path.exists(PHOTO_PATH):
    photo = Image(PHOTO_PATH, width=1.08 * inch, height=1.08 * inch)
else:
    photo = Paragraph("Photo", styles["Meta"])

header_table = Table(
    [[top_left, photo]],
    colWidths=[6.1 * inch, 1.0 * inch],
    hAlign="LEFT",
)
header_table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor("#c7d2fe")),
        ]
    )
)
story.append(header_table)
story.append(Spacer(1, 0.04 * inch))

story.append(Paragraph("PROFESSIONAL SUMMARY", styles["Section"]))
story.append(
    Paragraph(
        "DataOps Engineer experienced in Azure-based data platforms, Databricks workloads, metadata-driven pipeline design, and analytics engineering. "
        "Contributes across multiple repositories and teams by combining delivery execution, CI/CD alignment, troubleshooting, and maintainable data architecture practices.",
        styles["Text"],
    )
)

story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]))
story.append(Paragraph("DataOps Engineer · EnablerMinds · Sep 2026 - Present · Frankfurt", styles["JobTitle"]))
for bullet in [
    "Developed and maintained Azure Data Factory pipelines, activities, datasets, linked services, triggers, and parameterized environment configurations.",
    "Configured Databricks jobs and task dependencies; investigated failed runs and aligned processing logic with metadata and orchestration requirements.",
    "Supported Unity Catalog adoption and governed naming standards across catalogs, schemas, and data object references.",
    "Built and maintained dbt models, source definitions, and validation checks to support reusable analytics transformations.",
    "Contributed to Azure Pipelines CI/CD for deployment and validation across repositories; collaborated with teams using Jira.",
]:
    story.append(Paragraph(f"• {bullet}", styles["CvBullet"]))
story.append(Paragraph("Core stack: ADF, Azure Pipelines, Databricks, Unity Catalog, dbt, GitHub, Git, Jira, Python, SQL", styles["Meta"]))

story.append(Paragraph("Data Engineer · Accenture · 2024 - 2026", styles["JobTitle"]))
story.append(Paragraph("• Delivered enterprise ETL/ELT workflows and analytics pipelines; collaborated with cross-functional teams to productionize data solutions.", styles["CvBullet"]))

story.append(Paragraph("Data Engineering Analyst · Tgndata · 2023 - 2024", styles["JobTitle"]))
story.append(Paragraph("• Contributed to pipeline optimization, data quality improvements, and metadata management patterns.", styles["CvBullet"]))

story.append(Paragraph("Research Roles · NKUA Medical Lab / National Observatory of Athens · 2021 - 2023", styles["JobTitle"]))
story.append(Paragraph("• Applied ML and time-series methods to medical and energy datasets; built research-grade models and analysis workflows.", styles["CvBullet"]))

story.append(Paragraph("TECHNICAL SKILLS", styles["Section"]))
skills_rows = [
    ["Cloud & Integration", "Microsoft Azure, Azure Data Factory, Azure Pipelines"],
    ["Data Platform", "Databricks, Unity Catalog, Databricks Jobs, PySpark"],
    ["Analytics Engineering", "dbt, SQL transformations, model dependencies, validation"],
    ["Delivery & Collaboration", "GitHub, Git, pull requests, code reviews, Jira"],
    ["Engineering Practices", "Metadata-driven workflows, parameterization, troubleshooting"],
]
skills_table = Table(skills_rows, colWidths=[1.85 * inch, 5.25 * inch], hAlign="LEFT")
skills_table.setStyle(
    TableStyle(
        [
            ("FONT", (0, 0), (0, -1), "Helvetica-Bold", 8.2),
            ("FONT", (1, 0), (1, -1), "Helvetica", 8.2),
            ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#0b1f44")),
            ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#111827")),
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8faff")),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d6e0f5")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]
    )
)
story.append(skills_table)

story.append(Paragraph("EDUCATION", styles["Section"]))
story.append(Paragraph("M.Sc. Information Systems (Big Data Analytics) · NKUA", styles["Text"]))
story.append(Paragraph("B.Sc. Mathematics · NKUA", styles["Text"]))
story.append(Paragraph("Thesis: Deterministic and stochastic PDE modeling with machine learning methods.", styles["Meta"]))
story.append(Paragraph("Languages: Greek (native), English (fluent)", styles["Meta"]))

doc.build(story)
print(f"[SUCCESS] CV generated: {PDF_PATH}")
