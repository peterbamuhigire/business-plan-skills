# Plan Figures Reference

[Owning skill](../SKILL.md)

Use when a business plan, funding request or pitch deck needs one of the three diagrams the plan skills already ask for: the implementation Gantt (`13-implementation-timeline`), a key-process flow (`08-operations-plan`) or a pitch money-flow or solution diagram (`meta-pitch/pitch-deck`, `meta-pitch/meta-presentation-design`). It covers diagrams only. Charts drawn from data (financial projections, cohort curves, sensitivity charts) follow the design engine's data-visualisation skills instead.

Figure approach follows the diagram IR and render-evidence pattern adapted from Archify (MIT, https://github.com/tt-a1i/archify, commit 0e4949f910a8e390bd3b4933883a4dcabad571be) as implemented in chwezi-sdlc-documentation (M10-07). Paraphrased.

## The three figure types

| Figure | Owning section | Authoring form | Must show |
|---|---|---|---|
| Implementation Gantt | `13-implementation-timeline` | Fenced Mermaid `gantt` block (Gantt is not an IR kind) | Workstreams as sections; approval gates (PPDA Contracts Committee award, Attorney-General clearance, donor tranche release, board approval) as `milestone` tasks that later tasks start `after`; critical-path tasks marked `crit`; owners and lead times in the plan's work-plan table |
| Key-process flow | `08-operations-plan` | Diagram IR kind `dataflow`, or Mermaid `flowchart` | The critical processes, the stores and external parties they depend on, and the control points the operations section names |
| Pitch money-flow or solution diagram | `meta-pitch/pitch-deck` | Mermaid `flowchart LR`, or IR `context` for a solution view | Who pays whom, for what, and where margin arises; or the product in use with its users and external systems |

Rules:

- A gate is blocking: nothing downstream starts before the milestone, consistent with `13-implementation-timeline/references/procurement-and-gating-schedule.md`. Statutory lead times and thresholds come from the current PPDA instrument, verified at the time of writing, never from this reference or an old plan.
- Figures illustrate the plan's own assumptions. A money flow carries the finance doctrine's professional-review state; illustrative figures never become client facts (the `00-plan-assembly` rule).
- The figure and the text must agree task for task and gate for gate; a gate in only one of them is an assembly defect.
- Mermaid `gantt` renders at a fixed wide canvas, so labels shrink below legible size at the portrait body measure. Put the Gantt on a landscape page or split it by phase, and keep the full schedule as a work-plan table; check that labels are 8 pt or more at the placed size.
- Labels in sentence case. Every Mermaid block carries `%% alt:` and `%% caption:` lines.

## Presentation

- Document figures: numbered caption below, alt text of at least one full sentence, PNG at 300 ppi or more plus SVG, labels in Public Sans under the design engine's `diagram-visual-standards.md` (the formal-document mapping for business plans).
- Pitch figures: export the PNG at the deck's slide pixel size and keep the SVG; one diagram per slide, carrying the slide's single message.
- The figure manifest (`<OutputName>.figures.json`) stays with the plan working files as evidence; it is not sent to the funder.

## Figure rendering hand-off

**Figure rendering hand-off.** Figures are rendered by the SRS engine, which owns the renderer, the diagram IR and the figure manifest; this engine holds no rendering code and must not copy any. Resolve the owning engine from `chwezi-engine-agents/catalog/engines.yaml` (entry `id: chwezi-sdlc-documentation`, `path: chwezi-sdlc-documentation`, resolved against the local portfolio root) and run every command from that folder. *Inputs:* a working folder containing an `_context/` directory (a one-line brief is enough) and a document directory of Markdown section files. Each figure is either a diagram-IR file at `<doc-dir>/diagrams/<name>.ir.json`, embedded with `<!-- diagram-ir: FIG-nnn -->` (IR fields `meta.srs_section` and `evidence.srs_section` take the numeric section of this document), or a fenced Mermaid block carrying `%% alt:` and `%% caption:` lines. *Commands:* for IR figures, `python -X utf8 -m engine diagrams validate <folder> --doc <doc-dir>` then `python -X utf8 -m engine diagrams generate <folder> --doc <doc-dir>`; then `bash scripts/build-doc.sh <doc-dir> <OutputName>`, which renders every figure through `scripts/render_diagrams.py`, builds the `.docx` with Pandoc and the SRS reference template, fails if Mermaid source survives (`scripts/check_docx_diagrams.py`) and writes the figure manifest; finally `python -X utf8 -m engine diagrams verify-manifest <doc-dir>`. Give paths relative to the SRS engine folder or as Windows paths: MSYS-style `/c/...` paths stop Pandoc finding the figures. *Outputs:* PNG at 300 ppi or more at the 6.25 in body measure plus SVG under `<doc-dir>/_figures/`; numbered captions ("Figure N — caption") with alt text in the Word image description; `_figures/render-manifest.json`; and `<OutputName>.figures.json` beside the `.docx`. *Font check:* every figure's `font_substitution_check` in the figure manifest must read `PASS` (labels in Public Sans under the design engine's `diagram-visual-standards.md`); `FAIL` or `NOT_ASSESSED` means the figure is not delivered. *Other document workflows:* when the document is assembled another way (for example with the docx skill), run `python -X utf8 scripts/render_diagrams.py --doc-dir <doc-dir> --name <OutputName> --out <stitched.md> <files>` for the figures only, insert the PNGs with their captions and alt text, then run `python -X utf8 scripts/check_docx_diagrams.py <file.docx>` and `python -X utf8 -m engine diagrams manifest --doc-dir <doc-dir> --name <OutputName> --docx <file.docx>`. *Degraded mode:* if the SRS engine, its Node renderer, Chrome or Edge, or Pandoc is unavailable, no figure is promised: describe the content in prose and a table, state that figures were not produced, record the render and font checks as `NOT_ASSESSED`, and never paste diagram source into the deliverable.

## Checks before release

- [ ] Each figure the plan promises is present, numbered and captioned, with alt text; or the plan says in prose that figures were not produced.
- [ ] Gates appear as blocking milestones with owners and lead-time sources recorded in the work-plan table.
- [ ] Every figure's `font_substitution_check` is `PASS`; `verify-manifest` passes; no diagram source in the delivered file.
