# Repository cleanup 8 October 2026

The repository was reorganized around the current CV, individual applications, WA Foundation project documents, shared supporting evidence, and image assets. The root README documents the new locations and rebuild commands.

## Removed files

| Original location | Reason |
| --- | --- |
| `Joshua Suubi/WASSWA WILSON - ACADEMIC DOCUMENTS.pdf` | Byte-identical duplicate of the academic master, now stored once as `supporting-documents/academics/Academic_Documents.pdf` |
| `CV FOR WASSWA WILSON - 2024.docx` | Superseded generic CV summary; its career history and substantive competencies are covered by the current CV and retained detailed references |
| `CV FOR WASSWA WILSON - 2026.docx` | Superseded March 2026 generic CV summary; the current CV includes the newer roles and projects |
| `CV FOR WASSWA WILSON - 2026.pdf` | Matching PDF export of the superseded March 2026 summary; its normalized body text matched the Word copy exactly |
| `wa-project/WASSWA_WILSON_FCHR_CV_ANNEX6.docx` | Draft superseded by the final Annex 6 CV, which corrects the ongoing FCHIP work and adds regional facility and training details |
| `prompt.md` | Completed AgroMavericks task instructions with obsolete source and output paths; unique job metadata was preserved in the application README |

## Retained files that needed clarification

The detailed 2024 biomedical CV and programming resume are reference sources, because they contain duties, technical competencies, and scans absent from the current CV. Their location is `cv/reference/`.

The Joshua Suubi CV contains distinct application content and remains in its own application folder. The former generic-looking application letter is an Omel Field Sales Supervisor letter, so it now lives under `applications/omel/`.

`wa-project/Untitled.docx` was a populated reusable template, not an empty document. It is now `projects/wa-foundation/Annex_6_Personnel_CV_Template.docx`. The final Word and PDF project CVs were renamed to the matching `Wasswa_Wilson_FCHR_CV_Annex6` basename; the PDF was verified against the final Word content.

The supporting Word document is required by the outreach builder, which extracts its embedded credential scans. The raw and cleaned signatures serve separate purposes. The two outreach dossiers intentionally include different identification content. Word and PDF exports remain together for editing and submission.

## Builder maintenance

The AgroMavericks builder now writes into its own application folder, matching the existing documents and answer checklist. Medequip and outreach resolve shared resources from their new locations. The current CV and outreach content modules remain next to their builders.

Retained document and image bytes were preserved. A recovery archive of the original working files was saved outside the repository before cleanup.

## Verification

The repository now contains 49 files, including four new documentation and Git configuration files. Six original files were removed, six text files were updated, and the other 39 retained originals passed byte-for-byte checks against the recovery archive. No byte-identical duplicate files remain.

All six Python sources passed syntax checks. All four builders' resource locations, 20 local Markdown links, and all 33 retained document and image files passed their relevant path or integrity checks. The outreach credential images and identification page references remain valid.

Full document regeneration was not run because the bundled verification runtime lacks `PyMuPDF`, an existing outreach dependency. The saved documents were moved without changing their content.

During publication, Git's automatic text detection flagged several PDFs for line-ending conversion. `.gitattributes` explicitly treats document and image formats as binary so Git preserves their bytes when staging and checking out files.
