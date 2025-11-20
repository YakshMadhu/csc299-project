<!--
Sync Impact Report

- Version change: template -> 1.0.0 (initial fill)
- Modified principles: (introduced the following principles)
	- Code Clarity & Readability
	- Simplicity & Minimal Surface Area
	- Code Quality & Maintainability
	- Testing Standards (NON-NEGOTIABLE)
	- User Experience Consistency
- Added sections: Development Workflow, Additional Constraints
- Removed sections: none
- Templates updated: ✅ `.specify/templates/plan-template.md`
										✅ `.specify/templates/spec-template.md`
										✅ `.specify/templates/tasks-template.md`
- Follow-up TODOs: none
-->

# Tasks Constitution

## Core Principles

### Code Clarity & Readability
Code MUST be written to be immediately understandable by an experienced reader. Public APIs,
function names, type names, and variable names MUST be descriptive and unambiguous. Implementations
MUST prefer clear, explicit control flow over clever or terse constructs.

Rules:
- Use short, focused functions; prefer composition over long functions.
- Prefer explicit types and names; avoid abbreviations that are unclear outside current authors.
- Include brief in-line comments only where intent is not obvious from code.

Rationale: Readable code reduces review time, onboarding friction, and long-term maintenance cost.

### Simplicity & Minimal Surface Area
Designs and implementations MUST minimize surface area: smaller public APIs, fewer knobs, and
a single clear way to perform common tasks.

Rules:
- New features MUST start with the smallest reasonable abstraction that solves the user's need.
- Avoid adding feature flags, configuration keys, or public APIs unless justified in the PR description.
- Complex solutions require an explicit justification section in the PR and approval from owners.

Rationale: Simpler code is easier to test, reason about, and refactor; it reduces cognitive load.

### Code Quality & Maintainability
All code MUST follow agreed quality standards: formatting, linting, static analysis, dependency hygiene,
and review processes.

Rules:
- Commits MUST pass linters and formatters in CI before merging.
- Dependency upgrades MUST include a compatibility & risk note in the PR and tests covering critical
	integration points.
- Every non-trivial module MUST include a short README describing purpose, public surface, and
	expected invariants.

Rationale: Quality tooling and conventions prevent regressions and make automated checks reliable.

### Use Emojis in output 

Add emojis in program output when possible. Be happy!

### Testing Standards (NON-NEGOTIABLE)
Testing is mandatory. For any user-visible feature (P1), authoring tests is REQUIRED before or as
part of implementation. Tests MUST be organized into unit, integration, and contract tests where
appropriate.

Rules:
- P1 features MUST include unit tests and at least one integration or contract test validating
	behavior across the integration boundary.
- Tests should be deterministic and runnable in CI; flaky tests MUST be fixed or removed.
- Test names and assertions MUST document the scenario and expected outcome.
- Test-driven development (TDD) is STRONGLY RECOMMENDED for critical flows.

Rationale: Reliable tests are the primary guardrail for long-term maintainability and safe refactors.

### User Experience Consistency
User-facing behaviors (APIs, CLI, web UI) MUST be consistent, predictable, and documented.

Rules:
- Error messages MUST be actionable and follow a consistent structure (short summary + cause + remediation).
- Public APIs and CLI behaviors MUST preserve backward compatibility unless a MAJOR version bump is
	explicitly planned and approved.
- Documentation and quickstarts MUST be updated alongside UI/API changes.

Rationale: Consistent UX reduces user errors and support overhead; it enables stable integration.

## Additional Constraints

- Security: Code handling secrets or authentication MUST follow the security guidance in `docs/security.md`.
- Observability: Services MUST emit structured logs and metrics for critical flows; include correlation IDs
	where relevant.
- Performance: Performance targets (latency, throughput) MUST be defined in the plan and validated in
	benchmarks when applicable.

## Development Workflow

- Branches: Use descriptive branch names `feature/`, `fix/`, `chore/`.
- PRs: Every PR MUST include a brief summary, linked plan/spec, testing notes, and a "Constitution Check"
	section that documents how the change satisfies or explains deviations from the Constitution.
- Reviews: At least one approving review from a maintainer is required for non-trivial changes; high-risk
	or cross-cutting changes require two reviewers and an explicit rollout plan.
- Gates: CI green + Constitution Check passing are required before merge.

## Governance

Amendment procedure:
- Propose changes via a PR against `.specify/memory/constitution.md` with rationale and migration steps.
- Amendments MUST include a version bump per the policy below and a `Last Amended` date.
- Maintainership approval: Amendments require approval from at least two maintainers or a unanimous
	approval if fewer than two maintainers exist.

Versioning policy:
- Use semantic versioning for the constitution: `MAJOR.MINOR.PATCH`.
	- MAJOR: Backwards-incompatible principle removals or redefinitions.
	- MINOR: Addition of new principles or materially expanded guidance.
	- PATCH: Editorial clarifications, typo fixes, or non-substantive rewording.

Compliance and review expectations:
- Every plan (see `.specify/templates/plan-template.md`) MUST include a "Constitution Check" section that
	maps the plan to applicable principles.
- Non-conforming changes are allowed only with documented justification and an explicit risk
	mitigation plan; such changes MUST be short-lived and tracked via tasks.

**Version**: 1.0.0 | **Ratified**: 2025-11-19 | **Last Amended**: 2025-11-19
