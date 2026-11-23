#!/usr/bin/env python3
"""Generate a detailed two-page CV PDF for Panos Kabasis."""

import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
PHOTO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "profile", "headshot-2026.jpg")
PDF_PATH = os.path.join(PROJECT_ROOT, "assets", "docs", "cv", "cv.pdf")


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#6b7280"))
    canvas.drawRightString(A4[0] - 0.5 * inch, 0.32 * inch, f"Page {canvas.getPageNumber()}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A4,
    topMargin=0.44 * inch,
    bottomMargin=0.5 * inch,
    leftMargin=0.48 * inch,
    rightMargin=0.48 * inch,
)

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        "Name",
        parent=styles["Heading1"],
        fontSize=21,
        leading=23,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#0b1f44"),
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        "Role",
        parent=styles["Normal"],
        fontSize=10.4,
        leading=12.6,
        textColor=colors.HexColor("#1d4ed8"),
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        "Meta",
        parent=styles["Normal"],
        fontSize=8.2,
        leading=10,
        textColor=colors.HexColor("#4b5563"),
    )
)
styles.add(
    ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontSize=10.6,
        leading=12.8,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#0f2f6b"),
        spaceBefore=7,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        "Text",
        parent=styles["Normal"],
        fontSize=8.7,
        leading=10.7,
        textColor=colors.HexColor("#111827"),
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        "CvBullet",
        parent=styles["Text"],
        leftIndent=11,
        firstLineIndent=0,
        spaceAfter=1.2,
    )
)
styles.add(
    ParagraphStyle(
        "JobTitle",
        parent=styles["Text"],
        fontName="Helvetica-Bold",
        fontSize=9.2,
        textColor=colors.HexColor("#0b1f44"),
        spaceBefore=4,
        spaceAfter=1.5,
    )
)

story = []

header_left = [
    Paragraph("PANOS KABASIS", styles["Name"]),
    Paragraph("Data Engineer | Azure Databricks | Data Platform Engineering", styles["Role"]),
    Paragraph("Frankfurt, Germany | panos.kabasis@gmail.com | (+30) 698 8120 621", styles["Meta"]),
    Paragraph("LinkedIn: linkedin.com/in/panos-kabasis-618b18264 | GitHub: github.com/UpBash", styles["Meta"]),
]

if os.path.exists(PHOTO_PATH):
    photo = Image(PHOTO_PATH, width=1.2 * inch, height=4.2 * inch)
else:
    photo = Paragraph("Photo unavailable", styles["Meta"])

header_table = Table([[header_left, photo]], colWidths=[5.9 * inch, 1.25 * inch], hAlign="LEFT")
header_table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LINEBELOW", (0, 0), (-1, 0), 0.9, colors.HexColor("#c7d2fe")),
        ]
    )
)
story.append(header_table)
story.append(Spacer(1, 0.05 * inch))

story.append(Paragraph("PROFESSIONAL SUMMARY", styles["Section"]))
story.append(
    Paragraph(
        "Data Engineer with experience designing and delivering enterprise-scale data pipelines, lakehouse solutions, and analytics platforms across cloud environments. "
        "Strong expertise in Python, SQL, PySpark, Azure Data Factory, Databricks, and Microsoft Fabric, with practical experience in medallion architectures, ETL/ELT development, "
        "data orchestration, CI/CD, and metadata-driven workflows.",
        styles["Text"],
    )
)
story.append(
    Paragraph(
        "Combines a strong mathematical foundation (B.Sc. Mathematics) with an M.Sc. in Big Data Analytics, specializing in machine learning, neural networks, and computational modelling. "
        "Experienced in translating complex data requirements into maintainable engineering solutions, with a particular interest in scalable data architecture, platform engineering, and distributed computing.",
        styles["Text"],
    )
)

story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"]))

story.append(Paragraph("DataOps Engineer | EnablerMinds | Sep 2026 - Present | Frankfurt, Germany", styles["JobTitle"]))
for bullet in [
    "Develop and maintain Azure Data Factory pipelines supporting ingestion, movement, and downstream processing across multiple environments.",
    "Configure and extend ADF activities, datasets, linked services, parameters, and triggers based on evolving business and data requirements.",
    "Build and maintain Databricks job/task definitions, schedules, dependencies, and execution parameters aligned with delivery timelines.",
    "Support Unity Catalog-aligned data organization, including governed catalog/schema/table references in code and workflow configurations.",
    "Contribute to dbt model development, source updates, and transformation dependency management for maintainable analytics layers.",
    "Support Azure Pipelines CI/CD processes for code, configuration, and data platform changes across multiple repositories.",
    "Troubleshoot pipeline and job failures through logs, execution output review, and coordinated cross-team issue resolution.",
]:
    story.append(Paragraph(f"• {bullet}", styles["CvBullet"]))
story.append(
    Paragraph(
        "<b>Stack:</b> Azure Data Factory, Databricks Jobs, Unity Catalog, dbt, Azure Pipelines, GitHub, Git, Jira, Python, SQL",
        styles["Meta"],
    )
)

story.append(Paragraph("Data Engineer | Accenture | 2024 - 2026 | Athens, Greece", styles["JobTitle"]))
for bullet in [
    "Contributed to enterprise ETL/ELT pipeline delivery for analytical and reporting initiatives.",
    "Supported medallion-oriented processing flows (Silver/Gold layers) using Databricks and PySpark patterns.",
    "Worked on Microsoft Fabric and Power BI integration paths for analytics consumption and stakeholder reporting.",
    "Collaborated with engineering and business teams to transform requirements into maintainable platform components.",
]:
    story.append(Paragraph(f"• {bullet}", styles["CvBullet"]))
story.append(Paragraph("<b>Stack:</b> Databricks, PySpark, SQL, Microsoft Fabric, Power BI, Git, CI/CD", styles["Meta"]))

story.append(Paragraph("Data Engineering Analyst | Tgndata | 2023 - 2024 | Athens, Greece", styles["JobTitle"]))
for bullet in [
    "Worked on ingestion, extraction, and cleansing workflows for structured data pipelines.",
    "Supported ETL development with SQL and Python while maintaining data quality and consistency checks.",
    "Contributed to metadata updates and workflow alignment with upstream and downstream dependencies.",
]:
    story.append(Paragraph(f"• {bullet}", styles["CvBullet"]))
story.append(Paragraph("<b>Stack:</b> SQL, Python, ETL workflows, data quality practices", styles["Meta"]))

story.append(Paragraph("Research Associate | NKUA Medical Research Lab | 2022 - 2023 | Athens, Greece", styles["JobTitle"]))
for bullet in [
    "Applied machine learning and deep learning methods to medical datasets for classification and predictive research tasks.",
    "Contributed to model experimentation workflows and technical reporting for research outcomes.",
]:
    story.append(Paragraph(f"• {bullet}", styles["CvBullet"]))

story.append(Paragraph("Research Analyst | National Observatory of Athens | 2021 - 2022 | Athens, Greece", styles["JobTitle"]))
for bullet in [
    "Analyzed solar and environmental data using statistical and time-series techniques.",
    "Developed forecasting workflows with Python-based analytical tools and model evaluation practices.",
]:
    story.append(Paragraph(f"• {bullet}", styles["CvBullet"]))

story.append(Paragraph("TECHNICAL SKILLS", styles["Section"]))
skills_rows = [
    ["Programming", "Python, SQL, PySpark"],
    ["Cloud", "Microsoft Azure, Azure Data Factory"],
    ["Data Platforms", "Databricks, Unity Catalog, Microsoft Fabric"],
    ["Distributed Computing", "Apache Spark, PySpark"],
    ["Analytics Engineering", "dbt, data modelling, SQL transformations"],
    ["Data Architecture", "Medallion architecture, Lakehouse, ETL/ELT"],
    ["DevOps", "Azure Pipelines, GitHub Actions, Git, CI/CD"],
    ["Databases", "SQL databases, MongoDB"],
    ["BI", "Power BI"],
    ["Machine Learning", "scikit-learn, TensorFlow, PyTorch, neural networks"],
]
skills_table = Table(skills_rows, colWidths=[1.9 * inch, 5.05 * inch], hAlign="LEFT")
skills_table.setStyle(
    TableStyle(
        [
            ("FONT", (0, 0), (0, -1), "Helvetica-Bold", 8.3),
            ("FONT", (1, 0), (1, -1), "Helvetica", 8.3),
            ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#0b1f44")),
            ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#111827")),
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8faff")),
            ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#d6e0f5")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ]
    )
)
story.append(skills_table)

story.append(Paragraph("EDUCATION", styles["Section"]))
story.append(Paragraph("<b>M.Sc. Information Systems (Big Data Analytics)</b> - National and Kapodistrian University of Athens (NKUA)", styles["Text"]))
story.append(Paragraph("Thesis: Deterministic and stochastic partial differential equations with machine learning methods.", styles["CvBullet"]))
story.append(Paragraph("<b>B.Sc. Mathematics</b> - National and Kapodistrian University of Athens (NKUA)", styles["Text"]))

story.append(Paragraph("SELECTED PROJECT THEMES", styles["Section"]))
for bullet in [
    "Machine learning pipelines for forecasting and predictive analytics.",
    "Computer vision and NLP model experimentation with evaluation-focused workflows.",
    "Data mining, dimensionality reduction (PCA/LDA), and feature engineering patterns.",
]:
    story.append(Paragraph(f"• {bullet}", styles["CvBullet"]))

story.append(Paragraph("LANGUAGES", styles["Section"]))
story.append(Paragraph("Greek (native), English (fluent)", styles["Text"]))

doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
print(f"[SUCCESS] CV generated: {PDF_PATH}")
