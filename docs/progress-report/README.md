# ESC 491 – First Progress Report

The report is written in parts. Each part has its own folder, named
`<number>-<Section>-<Owner>`, and only that owner edits the files in it.
This keeps every person's branch independent, so the pull requests merge
without conflicts. When all parts are merged, the parts are combined into
one report in the order below.

## Division of work

| # | Section (guideline weight) | Owner | Branch |
|---|---|---|---|
| 1 | Overview / Executive Summary (5%) | Mert Gökalp | `report/mert-gokalp` |
| 2 | Introduction: problem statement, aim and objectives (15%) | Mert Gökalp | `report/mert-gokalp` |
| 3 | Literature Review (30%) | Yağız Akkaya | `report/yagiz-akkaya` |
| 4 | Requirement Specifications (20%) | Adil Mert İş | `report/adil-mert-is` |
| 5 | Research Method (10%) | Aydan Doğan | `report/aydan-dogan` |
| 6 | System Design (10%) | Mert Gökalp | `report/mert-gokalp` |
| 7 | Conclusion (10%) | Mert Gökalp | `report/mert-gokalp` |

The cover page (project title and group members) is added when the parts
are combined.

## Workflow

1. Switch to your branch: `git fetch origin && git checkout report/<your-name>`
2. Write only inside your own folder(s). Replace the guidance notes in the
   template with your text.
3. Put figures in the same folder and reference them with a relative path.
4. Commit, push to your branch and open a pull request into `main`.
5. After all parts are merged, the full report is assembled from the folders
   in numerical order.

## Writing rules

- English only.
- Refer to team members by name.
- Cite every source (author, year, title, link). Use one citation style
  across the report (IEEE is suggested).
- Useful material already in the repository: `README.md`, `docs/team-plan.md`,
  `docs/proposal/`, `docs/hardware/`, `docs/pilot-region/`, `docs/diagrams/`
  and `layers/`.
