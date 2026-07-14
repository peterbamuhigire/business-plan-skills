# Target Architecture

The implemented architecture keeps the engine identity but separates routing, doctrine, examples, templates, validation, and delivery evidence so an agent can find the right skill and prove the output state.

```text
business-plan-skills/
|-- README.md                         # router and domain contract
|-- AGENTS.md                         # Codex operating rules
|-- CLAUDE.md                         # Claude operating rules, if used
|-- docs/
|   |-- engine-upgrade-july-2026/     # this audit report set
|   |-- source-registers/             # NEW: dated official/current sources
|   |-- quality-gates/                # release-blocking QA gates
|   `-- workbook-audits/              # retained machine evidence
|-- skills/
|   |-- <category>/<skill>/SKILL.md   # active entrypoints with strong frontmatter
|   |-- <category>/<skill>/references/# supporting doctrine, standards, examples
|   `-- <category>/<skill>/templates/ # reusable templates where needed
|-- examples/                         # public, sanitised full workflows and honest release states
|-- templates/                        # shared document/workbook/code templates
|-- scripts/ or tools/                # validators, generators, conformance checks
|-- tests/                            # routing, positive, and negative fixtures
`-- projects/                          # optional local workspaces, excluded from engine scoring
```

The July implementation also adds `business-plan-orchestrator`, the cross-engine delivery contract, a release-evidence template, and an executable release-bundle validator. Existing folders are retained only when active, routed, or documented as historical/project material.
