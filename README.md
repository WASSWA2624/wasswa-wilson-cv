# Wasswa Wilson CV and application documents

The current general-purpose CV is in [cv/](cv/). Employer-specific applications, project documents, supporting evidence, and shared images each have a dedicated location.

## Repository layout

| Location | Contents |
| --- | --- |
| [cv/](cv/) | Current 2026 CV in Word and PDF, its builder, and shared CV content |
| [cv/reference/](cv/reference/) | Detailed biomedical CV and programming resume retained for experience and evidence absent from the current CV |
| [applications/agromavericks/](applications/agromavericks/) | Full Stack Developer CV, application letter, form answers, and builder |
| [applications/medequip-rwanda/](applications/medequip-rwanda/) | Biomedical Engineer CV, cover letter, submission notes, and builder |
| [applications/outreach-robert-muwanga/](applications/outreach-robert-muwanga/) | Introduction email, cover letter, dossiers, and builder |
| [applications/joshua-suubi/](applications/joshua-suubi/) | Distinct March 2026 CV shared for this introduction |
| [applications/omel/](applications/omel/) | February 2025 Field Sales Supervisor cover letter |
| [projects/wa-foundation/](projects/wa-foundation/) | Final Annex 6 CV, reusable personnel CV template, completion guide, project brief, and team roles |
| [supporting-documents/academics/](supporting-documents/academics/) | Academic documents and course units |
| [supporting-documents/professional/](supporting-documents/professional/) | COHSASA accreditation evidence |
| [supporting-documents/identification/](supporting-documents/identification/) | Identification document packet |
| [supporting-documents/Supporting_Documents.docx](supporting-documents/Supporting_Documents.docx) | Original credential scans used to build the outreach dossiers |
| [assets/](assets/) | Original signature, cleaned signature, and passport photo |

## Rebuild documents

Run these commands from the repository root using a Python environment with `python-docx`, `reportlab`, `Pillow`, and `PyMuPDF` installed:

```bash
python cv/build_wilson_cv.py
python applications/agromavericks/build_agromavericks_application.py
python applications/medequip-rwanda/build_medequip_application.py
python applications/outreach-robert-muwanga/build_outreach.py
```

Each builder writes beside its own source files. Rebuild the current CV before rebuilding an outreach dossier when the CV content changes. The Medequip builder regenerates the shared cleaned signature from `assets/signature.jpeg`.

Edit [cv/cv_content.py](cv/cv_content.py) for the general CV and [applications/outreach-robert-muwanga/letter_content.py](applications/outreach-robert-muwanga/letter_content.py) for outreach text. Employer-specific content lives in each application's builder.

## File retention

Keep one copy of each shared source. Word and PDF versions serve different purposes and are retained together. The two outreach dossiers intentionally differ in whether they include identification. Older documents in `cv/reference/` preserve unique experience and supporting scans; use the current CV for general applications.

The [cleanup record](docs/repository-cleanup.md) explains which duplicate and superseded files were removed. Generated caches, Office lock files, and temporary dossier PDFs are ignored by Git.
