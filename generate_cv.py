#!/usr/bin/env python3
"""Generate professional CV PDF for Panos Kabasis"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime

# Create PDF
pdf_path = "cv.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                       topMargin=0.4*inch, bottomMargin=0.4*inch,
                       leftMargin=0.5*inch, rightMargin=0.5*inch)

# Style definitions
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=2,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

section_style = ParagraphStyle(
    'SectionHead',
    parent=styles['Heading2'],
    fontSize=11,
    textColor=colors.HexColor('#000000'),
    spaceAfter=4,
    spaceBefore=6,
    fontName='Helvetica-Bold',
    borderColor=colors.HexColor('#333333'),
    borderPadding=2
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontSize=9,
    alignment=TA_CENTER,
    spaceAfter=2,
    textColor=colors.HexColor('#333333')
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=9,
    spaceAfter=2,
    leading=10
)

bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=styles['Normal'],
    fontSize=9,
    spaceAfter=2,
    leftIndent=15,
    leading=10,
    textColor=colors.HexColor('#000000')
)

job_title_style = ParagraphStyle(
    'JobTitle',
    parent=styles['Heading3'],
    fontSize=10,
    textColor=colors.HexColor('#000000'),
    spaceAfter=1,
    fontName='Helvetica-Bold'
)

job_meta_style = ParagraphStyle(
    'JobMeta',
    parent=styles['Normal'],
    fontSize=8.5,
    textColor=colors.HexColor('#555555'),
    spaceAfter=3,
    leading=9,
    fontName='Helvetica-Oblique'
)

# Build document
content = []

# Header
content.append(Paragraph("PANOS KABASIS", title_style))
content.append(Spacer(1, 0.08*inch))

# Contact info
contact_info = "Frankfurt, Hesse, Germany | 📧 panos.kabasis@gmail.com | 📱 (+30) 698 8120 621 | " \
               "<a href='https://linkedin.com/in/panos-kabasis-618b18264/'>LinkedIn</a> | " \
               "<a href='https://github.com/UpBash'>GitHub</a>"
content.append(Paragraph(contact_info, contact_style))
content.append(Spacer(1, 0.08*inch))

# Professional Summary
content.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
summary_text = ("Data engineer and AI researcher with hands-on expertise in cloud data platforms, analytics engineering, "
                "and enterprise data orchestration. Proven track record building and maintaining scalable data pipelines across "
                "Azure, Databricks, and analytics ecosystems. Strong foundation in machine learning, full-stack data engineering, "
                "and collaborative software development.")
content.append(Paragraph(summary_text, normal_style))
content.append(Spacer(1, 0.06*inch))

# Professional Experience
content.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))

# DataOps Engineer
content.append(Paragraph("<b>DataOps Engineer</b> | EnablerMinds, Frankfurt | Sep 2026 – Present", job_title_style))
content.append(Spacer(1, 0.02*inch))
roles_data = [
    ("Azure Data Integration:", "Architected and maintained ADF pipelines for data ingestion, transformation, and downstream processing; "
     "configured activities, datasets, linked services, and environment-specific parameters."),
    ("Databricks Workflows:", "Designed job configurations, task definitions, and scheduling; troubleshot execution failures; integrated workloads "
     "into broader orchestration frameworks."),
    ("Data Governance & Catalog:", "Leveraged Unity Catalog for governed data asset organization; aligned catalogs, schemas, and table references "
     "with governance standards."),
    ("Analytics Engineering (dbt):", "Developed modular transformation models; maintained dependencies across source and reporting layers; "
     "implemented data quality validations."),
    ("CI/CD & Automation:", "Built Azure Pipelines for automated validation and deployment; coordinated multi-repository changes; "
     "maintained consistency between deployments."),
    ("Cross-team Collaboration:", "Supported multiple teams via Jira; translated requirements into pipeline logic, job definitions, and configuration "
     "changes; documented solutions for knowledge transfer."),
]

for label, text in roles_data:
    bullet_text = f"<b>{label}</b> {text}"
    content.append(Paragraph(bullet_text, bullet_style))

content.append(Paragraph("<i>Technologies: Azure Data Factory, Azure Pipelines, Databricks, Unity Catalog, dbt, GitHub/Git, Jira, Python, SQL</i>",
                        ParagraphStyle('TechStyle', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#555555'), spaceAfter=3, leftIndent=15)))
content.append(Spacer(1, 0.04*inch))

# Accenture
content.append(Paragraph("<b>Data Engineer</b> | Accenture, Athens | 2024 – 2026", job_title_style))
content.append(Paragraph("• Designed and implemented end-to-end data pipelines for enterprise clients "
                        "• Developed ETL workflows supporting business intelligence and analytics initiatives "
                        "• Collaborated with cross-functional teams to translate requirements into scalable solutions "
                        "• <i>Technologies: Python, SQL, Apache Spark, AWS/Azure, CI/CD pipelines</i>",
                        bullet_style))
content.append(Spacer(1, 0.04*inch))

# Other roles (condensed)
content.append(Paragraph("<b>Data Engineering Analyst</b> | Tgndata, Athens | 2023 – 2024<br/>"
                        "Contributed to data pipeline development and optimization; supported data quality initiatives and metadata management.",
                        bullet_style))
content.append(Paragraph("<b>Research Associate</b> | NKUA Medical Research Lab, Athens | 2022 – 2023<br/>"
                        "Conducted ML research on medical datasets; published findings; developed deep learning models for classification.",
                        bullet_style))
content.append(Paragraph("<b>Research Analyst</b> | National Observatory of Athens | 2021 – 2022<br/>"
                        "Analyzed solar energy data; developed time series forecasting models using Python, pandas, scikit-learn, TensorFlow.",
                        bullet_style))
content.append(Spacer(1, 0.04*inch))

# Technical Skills
content.append(Paragraph("TECHNICAL SKILLS", section_style))
skills_data = [
    ("Cloud & Integration:", "Microsoft Azure, Azure Data Factory (ADF), Azure Pipelines, Azure Storage"),
    ("Data Platforms:", "Databricks, Unity Catalog, Databricks Jobs & Workflows, PySpark"),
    ("Analytics & Transformation:", "dbt, SQL, Python, dimensional modeling, data validation"),
    ("Version Control & CI/CD:", "GitHub, Git, Azure Pipelines, pull requests, code reviews"),
    ("Configuration & Orchestration:", "Metadata-driven workflows, job scheduling, parameterization, environment management"),
    ("Data Engineering:", "ETL/ELT design, data warehouse architecture, pipeline monitoring, troubleshooting"),
    ("ML & Analysis:", "Machine Learning, Deep Learning, NLP, Computer Vision, Predictive Analytics, Time Series"),
    ("Programming:", "Python, SQL, Spark, Scala (basics)"),
    ("Collaboration Tools:", "Jira, Confluence, GitHub, multi-repository development"),
]

for skill_cat, skill_list in skills_data:
    skill_text = f"<b>{skill_cat}</b> {skill_list}"
    content.append(Paragraph(skill_text, bullet_style))

content.append(Spacer(1, 0.04*inch))

# Education
content.append(Paragraph("EDUCATION", section_style))
content.append(Paragraph("<b>M.Sc. in Information Systems</b> – National Kapodistrian University of Athens (NKUA)<br/>"
                        "Specialization: Big Data Analytics | Thesis: Deterministic & Stochastic PDEs with Machine Learning",
                        normal_style))
content.append(Paragraph("<b>B.Sc. in Mathematics</b> – National Kapodistrian University of Athens (NKUA)", normal_style))
content.append(Spacer(1, 0.04*inch))

# Languages & Certifications
content.append(Paragraph("LANGUAGES & CERTIFICATIONS", section_style))
content.append(Paragraph("• <b>Languages:</b> Greek (native), English (fluent)<br/>"
                        "• <b>Expertise:</b> Advanced Azure Data Platform knowledge, Databricks workflows & job configurations, Modern Data Stack (dbt, Unity Catalog, CI/CD)",
                        bullet_style))

# Build PDF
doc.build(content)
print(f"[SUCCESS] CV generated: {pdf_path}")
