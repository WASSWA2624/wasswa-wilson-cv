# -*- coding: utf-8 -*-
"""
Single source of truth for the Wasswa Wilson general-purpose CV.

Both the DOCX and the PDF renderers read from this module, so the two
documents can never drift apart. Edit here, then re-run build_wilson_cv.py.

House rules
-----------
* No em dashes. Use commas, colons, parentheses, full stops or the middot.
* First person throughout. "I led", "I built", "I contributed", never
  "Led" or "Responsible for". The reader should never be in doubt about
  which parts of this were mine.
* Research, proposal writing and data work are the spine of this CV, not
  a footnote to the engineering.
"""

# --------------------------------------------------------------------------
# Header
# --------------------------------------------------------------------------

NAME = "WASSWA WILSON"

TAGLINE = ("Data Analyst  ·  Biomedical Engineer  ·  Full-Stack Software Developer"
           "  ·  Researcher and Proposal Writer")

HOSSPI_URL = "https://hosspi.com/"

PROJECT_LINKS = {"HOSSPI Hospital Management System": HOSSPI_URL}

CONTACT_LINES = [
    "Kampala, Uganda   ·   wasswawilson0001@gmail.com   ·   +256 783 230 321",
    "English (fluent, professional working proficiency)   ·   Luganda (native)",
]

# --------------------------------------------------------------------------
# Profile
# --------------------------------------------------------------------------

PROFILE = (
    "I am a biomedical programmes leader, data analyst and full-stack software developer based "
    "in Kampala, "
    "with over nine years of work across health research, data systems and software engineering. "
    "As Biomedical Programs Manager at the Gould Family Foundation (GFF), I led biomedical "
    "engineers and technicians across seven countries in East, Central and Southern Africa. "
    "I also trained doctors, nurses and apprentices alongside these teams. "
    "I founded and develop HOSSPI, my hospital management platform. My data work includes "
    "analysis in Python, SQL, MATLAB and Excel, data validation, automated auditing and "
    "management dashboards. At International Hospital Kampala, I managed the biomedical "
    "function, developed COVID-19 oxygen demand models for hospital and national planning, and "
    "supported COHSASA accreditation. My research experience includes laboratory data analysis "
    "and mathematical modelling at the Uganda Virus Research Institute. I also undertake "
    "independent biomedical consulting across five countries, develop software and production "
    "AI agents, and write institutional proposals."
)

# --------------------------------------------------------------------------
# Career highlights
# --------------------------------------------------------------------------

HIGHLIGHTS = [
    "As Biomedical Programs Manager at the Gould Family Foundation (GFF), I led biomedical "
    "engineers and technicians across Uganda, Kenya, Tanzania, Burundi, Malawi, Somaliland and "
    "Rwanda. I managed programme planning, implementation and reporting across partner health "
    "facilities, and I led training for biomedical engineers, technicians and clinical users, "
    "including doctors, nurses and apprentices.",

    "I founded and develop HOSSPI, a hospital management system covering patient records, "
    "clinical, laboratory, pharmacy and billing workflows. The platform includes biomedical "
    "engineering, role-based permissions, multi-facility management and live analytics.",

    "My current data analysis work includes community screening, referral and follow-up data "
    "in Python and SQL. I define reporting indicators and data-quality checks, and I develop "
    "FCHIP management dashboards alongside the platform's data capture, database and cloud "
    "flows.",

    "I developed the oxygen consumption formulas used to calculate patient demand during the "
    "COVID-19 response at International Hospital Kampala, and I supported Ministry of Health "
    "oxygen planning. I tested the model against real hospital demand, and it informed capacity "
    "planning for later facility projects.",

    "I am building a cross-sector data collection and reporting application that writes the "
    "report as the user works, instead of leaving it to be compiled afterwards. I designed it for "
    "accounting, research, biology, agriculture, social media and similar fields.",

    "I designed, built and deployed an AI reception agent for a law firm in Texas, USA. It "
    "handles live inbound client calls, books and reschedules appointments, and runs client "
    "follow-up. It is in active production use.",

    "I prepared and maintained the biomedical compliance evidence that carried International "
    "Hospital Kampala through successful COHSASA accreditation, which is data quality assurance "
    "against a published standard.",

    "I have delivered hospital technology projects in five countries: Uganda, the Democratic "
    "Republic of Congo, Kenya, Tanzania and Somaliland, and I upgraded partner facilities for the "
    "Gould Family Foundation including the neonatal intensive care unit at Mama Lucy Kibaki "
    "Hospital, Nairobi.",
]

# --------------------------------------------------------------------------
# Research, data and proposal development
# --------------------------------------------------------------------------

RESEARCH = [
    ("Research",
     "I worked as a research intern at the Uganda Virus Research Institute on laboratory data "
     "analysis, mathematical modelling and research pipeline design in Python. My BSc at Makerere "
     "covered Research Methods, Biomedical Modelling and Simulation, Biosignal Processing and "
     "Analysis, and Bioinformatics and Functional Genomics, and I carried a full research project "
     "through to completion. I apply the same method to operational problems, most visibly in the "
     "COVID-19 oxygen demand modelling."),

    ("Data management at scale",
     "I built and maintained equipment registers, maintenance schedules and service histories "
     "at International Hospital Kampala and the Gould Family Foundation. I now design and run "
     "FCHIP's data layer, including capture schemas, validation rules, cloud flows, storage and "
     "synchronisation across web and mobile."),

    ("Analysis and reporting",
     "I analyse data in Python, SQL, MATLAB and Excel, build live management dashboards, and "
     "develop automated auditing and verification tools that check records in bulk."),

    ("Proposals, grants and technical writing",
     "I write and edit institutional proposals, grant applications, investment proposals, concept "
     "notes, partnership documents, pitch decks, technical documentation and user manuals, "
     "together with the annexes and evidence files that have to stand up to assessment."),

    ("Modern tooling and automation",
     "I work with AI agents and agent-assisted development daily, in Cursor, Claude, OpenAI GPT "
     "and Codex, and I build automation pipelines that take routine collection, reconciliation "
     "and reporting off people's hands."),
]

# --------------------------------------------------------------------------
# Technical skills
# --------------------------------------------------------------------------

SKILLS = [
    ("Data, analytics and reporting",
     "Python  ·  SQL  ·  MATLAB  ·  Excel  ·  relational modelling and query optimisation  ·  "
     "data cleaning and validation  ·  ETL and cloud data pipelines  ·  dashboard and report "
     "design  ·  automated auditing and verification tooling"),

    ("AI, agents and automation",
     "AI agent design, deployment and monitoring  ·  workflow and process automation  ·  "
     "third-party systems integration  ·  Cursor  ·  Claude  ·  OpenAI GPT  ·  Codex"),

    ("Programming languages",
     "Java  ·  Python  ·  JavaScript  ·  TypeScript  ·  C  ·  C++  ·  C#  ·  PHP  ·  SQL  ·  "
     "MATLAB  ·  Arduino C  ·  HTML5  ·  CSS3"),

    ("Web and mobile",
     "React  ·  Next.js (App Router)  ·  React Native  ·  Expo  ·  Tailwind CSS  ·  "
     "styled-components  ·  Bootstrap  ·  JavaFX / FXML  ·  Jest  ·  Playwright"),

    ("Backend and APIs",
     "Node.js  ·  Express  ·  Laravel  ·  CodeIgniter  ·  Spring / Spring Boot  ·  Convex  ·  "
     "Prisma  ·  MySQL  ·  REST APIs  ·  JWT  ·  role-based access control"),

    ("Cloud and DevOps",
     "AWS  ·  Microsoft Azure  ·  Vercel  ·  EAS  ·  Bunny.net CDN  ·  Git and GitHub  ·  "
     "CI/CD pipelines  ·  release and environment management"),

    ("Research and scientific",
     "Research methods and study documentation  ·  mathematical modelling and simulation  ·  "
     "biosignal processing  ·  medical imaging  ·  bioinformatics and functional genomics  ·  "
     "embedded systems design  ·  Proteus  ·  Eagle CAD  ·  Solid Edge"),

    ("Documents and productivity",
     "Microsoft Word  ·  Excel  ·  PowerPoint  ·  proposal, grant and investment writing  ·  "
     "technical writing  ·  document editing and design  ·  Windows, Linux and Android"),

    ("Medical equipment",
     "CT and X-ray imaging  ·  ultrasound and C-arms  ·  ventilators, monitors and infusion "
     "pumps  ·  theatre and ICU systems  ·  haematology, chemistry and blood bank analysers  ·  "
     "neonatal incubators, phototherapy, foetal Dopplers and CTG  ·  oxygen plants, cylinder "
     "and manifold systems and piped medical gas  ·  RO water and sterilisation plant"),
]

# --------------------------------------------------------------------------
# Professional experience
# --------------------------------------------------------------------------

EXPERIENCE = [
    {
        "role": "Founder and Developer",
        "org": "HOSSPI Hospital Management System",
        "dates": "Current",
        "bullets": [
            "I founded HOSSPI and develop its hospital management platform, integrating patient "
            "records with clinical, laboratory, pharmacy, billing and biomedical engineering "
            "workflows.",

            "I develop role-based permissions, multi-facility management and live analytics to "
            "support hospital teams' operational and reporting needs.",
        ],
    },
    {
        "role": "Data Analyst and Lead Software Developer, FCHIP and Health Information Systems",
        "org": "FairBanks Medical Centre Limited, Kampala, Uganda",
        "dates": "2026 to present",
        "bullets": [
            "I analyse community screening, referral and follow-up data in Python and SQL. I "
            "define reporting indicators, validation rules and data-quality checks, and I "
            "develop management dashboards based on verified figures.",

            "I lead the design and build of the FairBanks Community Health Intelligence Platform "
            "(FCHIP). I design the data capture forms, database structure and cloud data flows, "
            "and I deliver the platform across web and mobile.",

            "I write FairBanks institutional proposals, grants, investment materials and "
            "partnership documents, including the Community Health Reach proposal. I chaired the "
            "meeting with the Uganda Health Partners Cooperative on cooperative health insurance "
            "in July 2026.",

            "I own the technical documentation, the data-protection practice, the access control "
            "and the release management across the platform.",
        ],
    },
    {
        "role": "Consultant Biomedical Engineer, Independent Practice",
        "org": "Contract assignments: Uganda, DR Congo, Kenya, Tanzania, Somaliland",
        "dates": "Mar 2025 to present",
        "bullets": [
            "I install, commission, calibrate and maintain hospital medical equipment under "
            "contract across five countries, working independently on site and to a fixed "
            "handover standard.",

            "I completed the laboratory, theatre and radiology installations at several hospitals "
            "in the Democratic Republic of Congo, including the facility serving the Kibali Gold "
            "Mine.",

            "I train the clinical users at handover, and I produce a written service report and "
            "maintenance record for every assignment, so the client keeps a verifiable equipment "
            "history.",
        ],
    },
    {
        "role": "Biomedical Programs Manager",
        "org": "Gould Family Foundation (GFF), East, Central and Southern Africa",
        "dates": "Aug 2024 to Feb 2025",
        "bullets": [
            "I led biomedical engineers and technicians across Uganda, Kenya, Tanzania, Burundi, "
            "Malawi, Somaliland and Rwanda. I managed programme planning, implementation and "
            "reporting across partner health facilities in all seven countries.",

            "I built and maintained the programme data: equipment registers, lifecycle records, "
            "procurement documentation and the routine reports that went to management.",

            "I developed the equipment lifecycle-management and master-planning strategies that "
            "were then applied across partner facilities.",

            "I upgraded several facilities, including the neonatal intensive care unit at Mama "
            "Lucy Kibaki Hospital, Nairobi, where my oxygen and equipment demand modelling "
            "informed the capacity plan.",

            "I led training programmes for biomedical engineers, technicians and clinical users, "
            "including doctors, nurses and apprentices.",
        ],
    },
    {
        "role": "Biomedical Manager",
        "org": "International Hospital Kampala (IHK)",
        "dates": "Jan 2020 to Jan 2024",
        "bullets": [
            "I managed the biomedical engineering function of a major private hospital for four "
            "years, including team supervision, workplans and reporting to executive management.",

            "I led oxygen therapy management through the COVID-19 response and I supported "
            "Ministry of Health oxygen planning. I developed the formulas used to calculate "
            "patient oxygen consumption, which gave managers a dependable basis for sizing plant "
            "capacity, cylinder stock and flow requirements rather than estimating them.",

            "I prepared and maintained the compliance evidence files reviewed for COHSASA "
            "accreditation, and I supported the hospital through successful accreditation.",

            "I led the installation and commissioning of CT and X-ray imaging, oxygen plant, "
            "laboratory, theatre and ICU systems through to handover, and I trained the clinical "
            "users.",

            "I built the preventive maintenance schedules and service-record systems that reduced "
            "equipment downtime, and I coordinated procurement, technical specification and "
            "lifecycle management of hospital medical equipment.",
        ],
    },
    {
        "role": "Biomedical Engineer",
        "org": "Norvik Hospital Ltd, Kampala",
        "dates": "Apr 2019 to Jan 2020",
        "bullets": [
            "I maintained and serviced the hospital diagnostic and patient-monitoring equipment, "
            "and I supported the installation and calibration of imaging and ICU equipment.",
            "I helped establish the preventive maintenance schedules and service follow-up "
            "records.",
        ],
    },
    {
        "role": "Research Intern",
        "org": "Uganda Virus Research Institute (UVRI)",
        "dates": "Dec 2018 to Apr 2019",
        "bullets": [
            "I carried out laboratory data analysis, mathematical modelling and research pipeline "
            "design in Python.",
            "I contributed to biomedical research projects and laboratory experimentation, and I "
            "handled the recording, quality checking and documentation of research data so "
            "results could be reproduced.",
        ],
    },
    {
        "role": "Teaching Assistant",
        "org": "Makerere University, College of Health Sciences",
        "dates": "Mar 2016 to Aug 2017",
        "bullets": [
            "I assisted in teaching biomedical engineering course units at undergraduate level.",
            "I supervised and supported the laboratory practical sessions for engineering "
            "students.",
        ],
    },
]

# --------------------------------------------------------------------------
# Selected projects  (project, role, context, period, detail)
# --------------------------------------------------------------------------

PROJECTS = [
    ("HOSSPI Hospital Management System",
     "Founder and Developer",
     "Hospital software and data systems",
     "Current",
     "I founded and develop HOSSPI, a hospital management system connecting patient records "
     "with clinical, laboratory, pharmacy and billing workflows. The platform integrates "
     "biomedical engineering, role-based access permissions, multi-facility management and live "
     "analytics, giving hospital teams a shared view of patient care, hospital operations and "
     "management reporting."),

    ("Institutional proposals, grants and investment materials",
     "Lead Writer",
     "FairBanks Medical Centre Limited",
     "2026 to present",
     "I write proposals, partnership documents and pitch decks for FairBanks, including "
     "Community Health Reach, accelerator and fellowship applications, and maternity and "
     "diagnostics investments. I prepare the narrative, financial annexes and supporting "
     "evidence, and I manage application opportunities and deadlines."),

    ("COVID-19 oxygen therapy management and demand modelling",
     "Biomedical Manager",
     "International Hospital Kampala, with Ministry of Health planning support",
     "2020 to 2022",
     "I ran oxygen therapy management for the hospital through the pandemic and I developed the "
     "formulas for calculating patient oxygen consumption. My figures were used to size plant "
     "capacity, cylinder stock and flow requirements, and to support planning decisions at "
     "managerial and national level."),

    ("AI reception agent",
     "Designer and Developer",
     "Law firm, Texas, USA",
     "2025 to present",
     "I built and deployed an AI agent that answers live inbound client calls, books and "
     "reschedules appointments, and runs post-contact client follow-up. It is in active "
     "production use."),

    ("Shulekeeper school information system",
     "Assistant Software Developer",
     "Shulekeeper",
     "2021 to 2024",
     "I contributed front-end and back-end development, third-party integrations, testing, user "
     "training and documentation to a multi-user records and reporting platform built with React "
     "and Next.js, TypeScript, Laravel, MySQL and AWS."),

    ("Endoscopy image capture and reporting software",
     "Lead Software Developer",
     "St. Catherine Hospital and St. Francis Hospital",
     "2017 to 2019",
     "I led the build of a clinical image capture and procedure reporting system in JavaFX and "
     "MySQL. I did the algorithm design, the relational modelling, the legacy data migration, the "
     "on-site installation, the user training and the user manual."),

    ("Wekebere foetal heart-rate monitoring system",
     "Electronics Developer and Programmer",
     "Wekebere",
     "2017 to 2024",
     "I built an Android and Arduino monitoring system for third-trimester foetal heart-rate "
     "measurement, and I implemented the Java serial communication between device and phone, with "
     "Microsoft Azure cloud storage."),
]

# --------------------------------------------------------------------------
# Professional competencies
# --------------------------------------------------------------------------

COMPETENCIES = [
    ("Programme and project management",
     "I led biomedical engineers and technicians across seven countries in East, Central and "
     "Southern Africa at GFF, and I managed a hospital "
     "biomedical function for four years: workplans, schedules, procurement coordination and "
     "management reporting."),

    ("Procurement, specification and compliance",
     "I coordinated specification, procurement, commissioning and lifecycle documentation, and I "
     "kept the compliance evidence reviewed for COHSASA accreditation."),

    ("Stakeholder and partnership management",
     "I chair partner meetings and write them up, and I work with hospital departments, "
     "suppliers, trainees, accreditation assessors, donors and prospective partners."),

    ("Training and capacity building",
     "At GFF, I trained biomedical engineers, technicians, doctors, nurses and apprentices. "
     "I also taught undergraduate engineering laboratory practicals at Makerere University."),

    ("Communication and adaptability",
     "I write and speak clear English and I present comfortably to clinical, executive and donor "
     "audiences. I settle quickly into new countries, teams, codebases and equipment brands."),
]

# --------------------------------------------------------------------------
# Education & professional development
# --------------------------------------------------------------------------

EDUCATION = [
    ("Certificate in Leadership and Management in Health",
     "University of Washington",
     "2022",
     "Grade A+. Planning, leadership and management of health programmes."),

    ("BSc Biomedical Engineering, Second Upper Honours",
     "Makerere University, Kampala",
     "2012 to 2017",
     "Research-relevant course units: Research Methods, Biomedical Modelling and Simulation, "
     "Biosignal Processing and Analysis, Bioinformatics and Functional Genomics, Database Systems "
     "and Software Engineering. I completed a full research project as part of the degree."),

    ("Advanced Java Programming, Level 1",
     "Green Bridge School of Open Technologies",
     "2015 to 2016",
     "Grade A+."),

    ("Uganda Advanced Certificate of Education (UACE)",
     "Mengo Secondary School",
     "2011",
     "Principal subjects: Mathematics, Physics, Biology, Chemistry."),

    ("Uganda Certificate of Education (UCE)",
     "St. John's Wakiso Secondary School",
     "2009",
     "Division 1."),
]

TRAINING = [
    ("COHSASA accreditation standards: in-service preparation and compliance",
     "International Hospital Kampala", "2020 to 2024"),
    ("Fire Safety, Prevention, Firefighting and Emergency Scene Management",
     "Fire Technologies Limited (IHK)", "2021"),
]

# --------------------------------------------------------------------------
# Interests
# --------------------------------------------------------------------------

INTERESTS = (
    "I play music, the saxophone in particular.  ·  I watch film.  ·  I train and exercise "
    "regularly.  ·  I enjoy travelling and working in unfamiliar places, which the regional field "
    "work has made second nature."
)

# --------------------------------------------------------------------------
# Referees
# --------------------------------------------------------------------------

REFEREES = [
    ("Eng. Richard Ssejongo",
     "Biomedical Engineer, St. Francis Hospital Nsambya",
     "+256 753 818 754  ·  +256 777 132 489"),

    ("Dr. Annet Khingi",
     "Senior Radiologist and Administrator, Mengo Hospital",
     "+256 772 592 771  ·  +256 701 592 771"),

    ("Racheal Nabukeera",
     "Director and Founder, FairBanks Medical Centre",
     "+256 772 849 258  ·  nracheal017@gmail.com"),
]
