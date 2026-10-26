# Domain Docs

This repo uses a single-context layout: `GLOSSARY.md` at the repo root and architecture decision records in `docs/adr/`.

## Before exploring

Read `GLOSSARY.md` and any ADRs in `docs/adr/` relevant to the area being explored.

If these files do not exist, proceed silently. The `/domain-modeling` skill creates them lazily when terms or decisions are resolved.

## Use the glossary's vocabulary

Use the glossary's terms in issue titles, proposals, hypotheses, and test names. If a needed concept is absent, reconsider whether the term belongs to the project; note real gaps for `/domain-modeling`.

## Flag ADR conflicts

When a proposal contradicts an existing ADR, name the ADR and explain why the decision should be revisited.
