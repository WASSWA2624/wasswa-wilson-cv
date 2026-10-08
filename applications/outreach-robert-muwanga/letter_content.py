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
     "My name is Wasswa Wilson. I am a data analyst, biomedical engineer and full-stack software "
     "developer based in Kampala, with over nine years of work across health research, data "
     "systems and software engineering. I would welcome a conversation about where my experience "
     "could be useful to you or your network."),

    ("Current data analysis and reporting",
     "At FairBanks Medical Centre, I analyse health data in Python and SQL, define indicators and "
     "validation rules, and build management reporting dashboards for the FairBanks Community "
     "Health Intelligence Platform. I design its data capture tools and cloud data flows, check "
     "the quality of the records behind the reports, and build automated auditing and "
     "verification tools. I also work with MATLAB and Excel."),

    ("Regional biomedical programme leadership",
     "As Biomedical Programs Manager at the Gould Family Foundation, I led biomedical engineers "
     "and technicians across Uganda, Kenya, Tanzania, Burundi, Malawi, Somaliland and Rwanda. "
     "I directed regional programme planning, implementation and reporting, maintained equipment "
     "and lifecycle records, and led training for engineers, technicians and clinical staff."),

    ("Research and analysis",
     "I began at the Uganda Virus Research Institute doing laboratory data analysis, mathematical "
     "modelling and research pipeline design in Python. At International Hospital Kampala, where "
     "I managed the biomedical function for four years, I developed oxygen consumption formulas "
     "during the COVID-19 response and tested them against hospital demand to support supply and "
     "capacity planning."),

    ("Proposal and grant writing",
     "I write and edit what FairBanks submits: community health project proposals, accelerator "
     "and fellowship applications, investment proposals and partnership documents, with the "
     "financial annexes and supporting evidence."),

    ("Hospital software development",
     "I am the founder and developer of HOSSPI (https://hosspi.com/), a hospital management "
     "system connecting patient records, clinical care, laboratory and pharmacy workflows, "
     "billing and reporting. It also supports biomedical engineering and role-based access. "
     "I am also building a cross-sector application for data collection and reporting."),

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

I am Wasswa Wilson, a data analyst, biomedical engineer and full-stack software developer based in Kampala. My experience combines current health data analysis and reporting at FairBanks Medical Centre with regional biomedical programme leadership and research.

My experience includes:

  Current data analysis. At FairBanks, I analyse health data in Python and SQL, define indicators and validation rules, check data quality, and build management dashboards for the FairBanks Community Health Intelligence Platform. I also use MATLAB and Excel and build automated auditing and verification tools.

  Regional programme leadership. As Biomedical Programs Manager at the Gould Family Foundation, I led biomedical engineers and technicians across Uganda, Kenya, Tanzania, Burundi, Malawi, Somaliland and Rwanda. I directed programme planning, implementation, reporting and training across partner health facilities.

  Research and analysis. I began at the Uganda Virus Research Institute doing laboratory data analysis, mathematical modelling and research pipeline design in Python. During the COVID-19 response at International Hospital Kampala, I developed oxygen consumption formulas and tested them against hospital demand to support supply and capacity planning.

  Proposal and grant writing. I write FairBanks community health proposals, accelerator applications and investment proposals, with the annexes and evidence files that go with them.

  Hospital software development. I am the founder and developer of HOSSPI (https://hosspi.com/), a hospital management system connecting patient records, clinical care, laboratory and pharmacy workflows, billing and reporting. It also supports biomedical engineering and role-based access.

Alongside this I am building an application that simplifies data collection and reporting for record-heavy professions, accounting and audit among them, producing the report in real time as the work is done.

I am not writing about a specific vacancy. This is an open introduction, and if anything here is useful to you or to someone in your network, I would be glad of a short conversation.

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
