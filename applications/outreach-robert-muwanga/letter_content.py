# -*- coding: utf-8 -*-
"""
Content for the open introduction to Mr. Robert Muwanga, referred by Juliet.

House rule, same as the CV: no em dashes anywhere.
"""

DATE = "11 September 2026"

RECIPIENT = ["Mr. Robert Muwanga", "Kampala, Uganda"]

SENDER = {
    "name": "Wasswa Wilson",
    "title": "Data Analyst, Biomedical Engineer and Software Developer",
    "email": "wasswawilson0001@gmail.com",
    "phone": "+256 783 230 321",
    "city": "Kampala, Uganda",
}

SUBJECT_LINE = "An introduction, on the recommendation of Juliet"

SALUTATION = "Dear Mr. Muwanga,"

# --------------------------------------------------------------------------
# Cover letter body. Tuples of (heading or None, paragraph text).
# --------------------------------------------------------------------------

LETTER_BODY = [
    (None,
     "My colleague Juliet suggested that I write to you and share my CV, and I am glad to do so."),

    (None,
     "My name is Wasswa Wilson. I am a biomedical programmes leader, data analyst and full-stack "
     "software developer based in Kampala, with over nine years across hospital engineering, "
     "research and software. My experience includes seven-country team leadership at GFF, "
     "independent consulting and founding HOSSPI. I would welcome a conversation about where "
     "this experience could be useful to you or your network."),

    ("Regional biomedical programme leadership",
     "As Biomedical Programs Manager at the Gould Family Foundation, I led biomedical engineers "
     "and technicians across Uganda, Kenya, Tanzania, Burundi, Malawi, Somaliland and Rwanda. "
     "I managed regional planning, implementation and reporting, and trained biomedical "
     "engineers, technicians and clinical users, including doctors, nurses and apprentices."),

    ("Hospital software development",
     "I am the founder and developer of HOSSPI (https://hosspi.com/), a hospital management "
     "system connecting patient records, clinical care, laboratory and pharmacy workflows, "
     "billing and live analytics. It also supports biomedical engineering and role-based access. "
     "I am also building a cross-sector application for data collection and reporting."),

    ("Research, data analysis and reporting",
     "At the Uganda Virus Research Institute, I analysed laboratory data and developed research "
     "pipelines in Python. At International Hospital Kampala, I developed and tested oxygen "
     "demand models during COVID-19 to support supply planning. My current work includes Python "
     "and SQL analysis, data validation and management dashboards for FairBanks' Community "
     "Health Intelligence Platform. I also use MATLAB and Excel."),

    ("Hospital management and independent consulting",
     "I managed the biomedical function at International Hospital Kampala for four years, "
     "maintaining equipment records and compliance evidence for COHSASA accreditation. I now "
     "undertake independent equipment installation, commissioning, maintenance and clinical "
     "user training in Uganda, DR Congo, Kenya, Tanzania and Somaliland."),

    ("Proposal and grant writing",
     "I write institutional proposals, grant applications and partnership documents, including "
     "community health, accelerator and investment submissions for FairBanks, with financial "
     "annexes and supporting evidence."),

    (None,
     "I have attached my CV, together with a single file containing this letter, the CV and my "
     "academic and professional credentials. I would value a short conversation at your "
     "convenience, whether about work within your own firm or simply to be pointed towards others "
     "who may find this useful."),

    (None,
     "Thank you for your time, and please pass on my thanks to Juliet."),
]

CLOSING = "Yours sincerely,"

# --------------------------------------------------------------------------
# Email. Plain text, for pasting straight into a mail client.
# --------------------------------------------------------------------------

EMAIL_SUBJECT = ("Introduction from Juliet: Wasswa Wilson, data analyst "
                 "and biomedical engineer")

EMAIL_BODY = """Dear Mr. Muwanga,

My colleague Juliet suggested I write to you and share my CV, so please allow me to introduce myself.

I am Wasswa Wilson, a biomedical programmes leader, data analyst and full-stack software developer based in Kampala. My experience spans seven-country team leadership at GFF, founding HOSSPI, hospital management, research and independent consulting.

My experience includes:

  Regional programme leadership. As Biomedical Programs Manager at the Gould Family Foundation, I led biomedical engineers and technicians across Uganda, Kenya, Tanzania, Burundi, Malawi, Somaliland and Rwanda. I managed regional planning, implementation and reporting, and trained biomedical engineers, technicians and clinical users, including doctors, nurses and apprentices.

  Hospital software development. I am the founder and developer of HOSSPI (https://hosspi.com/), a hospital management system connecting patient records, clinical care, laboratory and pharmacy workflows, billing and live analytics. It also supports biomedical engineering and role-based access.

  Research, data analysis and reporting. At the Uganda Virus Research Institute, I analysed laboratory data and developed research pipelines in Python. At International Hospital Kampala, I developed and tested oxygen demand models during COVID-19 to support supply planning. My current work includes Python and SQL analysis, data validation and management dashboards for FairBanks' Community Health Intelligence Platform. I also use MATLAB and Excel.

  Hospital management and independent consulting. I managed the biomedical function at International Hospital Kampala for four years, maintaining equipment records and compliance evidence for COHSASA accreditation. I now undertake independent equipment installation, commissioning, maintenance and clinical user training in Uganda, DR Congo, Kenya, Tanzania and Somaliland.

  Proposal and grant writing. I write institutional proposals, grant applications and partnership documents, including community health, accelerator and investment submissions for FairBanks, with financial annexes and supporting evidence.

Alongside this, I am building an application for real-time data collection and reporting across accounting, research and other fields.

This is an open introduction. If my experience could be useful to you or someone in your network, I would welcome a short conversation.

I have attached:

  1. My CV.
  2. A single file containing my cover letter, CV and supporting documents, that is my academic and professional credentials.

Thank you for your time, and my thanks to Juliet for the introduction.

Kind regards,

Wasswa Wilson
Data Analyst, Biomedical Engineer and Software Developer
wasswawilson0001@gmail.com
+256 783 230 321
"""

# --------------------------------------------------------------------------
# Dossier assembly
# --------------------------------------------------------------------------

DOSSIER_TITLE = "Professional Dossier"

CONTENTS = [
    ("1", "Cover letter", "Introduction to Mr. Robert Muwanga"),
    ("2", "Curriculum vitae", "Four pages"),
    ("3", "Academic and professional credentials", "Eight documents"),
    ("4", "Identification documents", "National identification card and driving licence"),
]

CONTENTS_NO_ID = CONTENTS[:3]

# Credentials, in the order they appear. (image name, caption)
CREDENTIALS = [
    ("image1.png", "Makerere University: Academic Transcript, BSc Biomedical Engineering, "
                   "Second Class Honours Upper Division"),
    ("image2.jpg", "Makerere University: Transcript key to grades and classification of awards"),
    ("image7.jpg", "University of Washington: Leadership and Management in Health, December 2022"),
    ("image6.jpg", "Greenbridge School of Open Technologies: Certificate in Java Programming, "
                   "Level 1, Grade A+, 2016"),
    ("image4.jpg", "Uganda National Examinations Board: Uganda Advanced Certificate of "
                   "Education, Mengo Secondary School, 2011"),
    ("image3.png", "Uganda National Examinations Board: Uganda Certificate of Education, "
                   "Division 1, St. John's Wakiso Secondary School, 2009"),
    ("image8.jpg", "Fire Technologies Limited: Fire safety, prevention, firefighting and "
                   "emergency scene management, International Hospital Kampala, April 2021"),
    ("image9.png", "COHSASA: Recognition of Achievement of Accreditation Status, Maintenance "
                   "Service, International Hospital Kampala, February 2022"),
]

# Images whose content sits rotated inside a portrait frame.
ROTATE_CCW = {"image6.jpg", "image7.jpg"}

# Identification pages, taken from Identification documents.pdf
IDENTIFICATION = [
    (0, "Republic of Uganda: National Identification Card, front"),
    (1, "Republic of Uganda: National Identification Card, reverse"),
    (2, "Republic of Uganda: Driving Licence, front"),
    (3, "Republic of Uganda: Driving Licence, reverse"),
]
