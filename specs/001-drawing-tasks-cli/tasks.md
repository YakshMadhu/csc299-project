---

description: "Task list for Drawing Tasks CLI implementation"
---

# Tasks: Drawing Tasks CLI

**Input**: Design documents from `/specs/001-drawing-tasks-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: Tests are REQUIRED per the project Constitution for P1 stories. For P1 stories,
include unit tests and at least one integration or contract test as applicable. The
tasks generated for a feature MUST include explicit test tasks for the story priorities
that require them. If tests are omitted for a given story, the plan/spec MUST document a
justification and a mitigation plan.

**Documentation tasks**: For every P1 story the generated tasks MUST include one or more
documentation tasks (for example: update `docs/`, update `quickstart.md`, or add module
README). Documentation tasks are required and MUST be completed before merging to `master`,
unless a documented exception with an approved issue is referenced in the PR.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Initialize Python project with v.mod and pyproject.toml configuration
- [X] T002 [P] Create project directory structure: src/cli, src/storage, src/models, tests/unit, tests/integration
- [X] T003 [P] Create all __init__.py files for Python packages
- [X] T004 [P] Create .gitignore for Python (.venv, __pycache__, *.pyc, .pytest_cache, etc.)
- [X] T005 [P] Set up pytest configuration in pyproject.toml

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Create Task dataclass in src/models/task.py with description and optional created_at fields
- [X] T007 Create file_storage.py module in src/storage/ with get_storage_path() function
- [X] T008 Implement load_tasks() function in src/storage/file_storage.py to read JSON file
- [X] T009 Implement save_tasks() function in src/storage/file_storage.py to write JSON file atomically
- [X] T010 [P] Create task_manager.py in src/storage/ with sort_tasks() function for alphabetical sorting

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and List Drawing Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add and list drawing tasks via CLI with alphabetical sorting

**Independent Test**: Run CLI to add tasks, then list them and verify alphabetical order output

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T011 [P] [US1] Unit test for load_tasks() in tests/unit/test_storage.py (empty file, valid JSON, missing file cases)
- [X] T012 [P] [US1] Unit test for save_tasks() in tests/unit/test_storage.py (write new file, overwrite existing)
- [X] T013 [P] [US1] Unit test for sort_tasks() in tests/unit/test_task_manager.py (case-sensitive alphabetical order: "Apple", "banana", "zebra")
- [X] T014 [US1] Integration test for add command in tests/integration/test_cli.py (add task and verify file saved)
- [X] T015 [US1] Integration test for list command in tests/integration/test_cli.py (add multiple tasks, list, verify sorted output)

### Implementation for User Story 1

- [X] T016 [P] [US1] Create main.py CLI entry point in src/cli/ with argparse setup
- [X] T017 [P] [US1] Implement add command handler in src/cli/commands/add.py
- [X] T018 [P] [US1] Implement list command handler in src/cli/commands/list.py
- [X] T019 [US1] Wire up add and list commands in src/cli/main.py with subparsers
- [X] T020 [US1] Add error handling for empty task descriptions in add.py
- [X] T021 [US1] Format list output with numbered tasks in list.py

### Documentation for User Story 1

- [X] T022 [P] [US1] Create src/cli/README.md documenting CLI command structure
- [X] T023 [P] [US1] Create src/storage/README.md documenting storage module API
- [X] T024 [US1] Create root README.md with installation instructions using 'v' and basic usage examples
- [X] T025 [US1] Verify quickstart.md has accurate add/list command examples

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Data Integrity and Error Handling (Priority: P2)

**Goal**: Handle file errors gracefully with clear error messages and no data loss

**Independent Test**: Simulate file permission errors and corrupted JSON, verify error messages and data safety

### Tests for User Story 2

- [X] T026 [P] [US2] Unit test for load_tasks() with corrupted JSON in tests/unit/test_storage.py
- [X] T027 [P] [US2] Unit test for save_tasks() with read-only file simulation in tests/unit/test_storage.py
- [X] T028 [US2] Integration test for add command with file permission errors in tests/integration/test_cli.py
- [X] T029 [US2] Integration test for list command with corrupted storage file in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T030 [US2] Add try/except in load_tasks() for JSONDecodeError with clear error message
- [X] T031 [US2] Add try/except in save_tasks() for PermissionError and OSError with actionable messages
- [X] T032 [US2] Implement atomic write pattern in save_tasks() (write to temp file, then rename)
- [X] T033 [US2] Add error message formatting following pattern: "Error: [summary]. Cause: [cause]. Remediation: [action]"
- [X] T034 [US2] Ensure CLI returns exit code 1 on errors, 0 on success

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently with robust error handling

---

## Phase 5: User Story 3 - Logical Separation of CLI and Storage (Priority: P3)

**Goal**: Verify clean separation between CLI and storage modules for maintainability

**Independent Test**: Code review confirms no direct file I/O in CLI code

### Implementation for User Story 3

- [X] T035 [US3] Review src/cli/ modules and ensure no direct file I/O operations (no open(), json.load(), etc.)
- [X] T036 [US3] Review src/storage/ modules and ensure they expose clean public API via __init__.py
- [X] T037 [US3] Verify CLI only imports from src.storage, not from file_storage directly
- [X] T038 [US3] Add type hints to all public functions in storage module for clear interface contracts

**Checkpoint**: All user stories should now be independently functional with clean architecture

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Add emojis to CLI output per constitution ("✓ Task added", "📝 Drawing Tasks:")
- [X] T040 [P] Add docstrings to all public functions in src/storage/ and src/cli/
- [X] T041 Run all tests with pytest --cov to verify >80% code coverage
- [X] T042 [P] Update quickstart.md with troubleshooting section
- [X] T043 Manual validation: Run quickstart.md examples and verify all outputs match documentation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed) or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Extends US1 error handling but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Code review task, no implementation dependencies

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services/managers
- Storage functions before CLI commands
- Core implementation before integration
- Documentation alongside or immediately after implementation
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Within a story: multiple [P] tasks can run in parallel (different files)
- Documentation tasks marked [P] can run in parallel with implementation

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task T011: "Unit test for load_tasks() in tests/unit/test_storage.py"
Task T012: "Unit test for save_tasks() in tests/unit/test_storage.py"
Task T013: "Unit test for sort_tasks() in tests/unit/test_task_manager.py"

# Launch all implementation files for User Story 1 together:
Task T016: "Create main.py CLI entry point in src/cli/"
Task T017: "Implement add command handler in src/cli/commands/add.py"
Task T018: "Implement list command handler in src/cli/commands/list.py"

# Launch all documentation for User Story 1 together:
Task T022: "Create src/cli/README.md"
Task T023: "Create src/storage/README.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (More robust!)
4. Add User Story 3 → Test independently → Deploy/Demo (Clean architecture!)
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (P1)
   - Developer B: User Story 2 (P2) 
   - Developer C: User Story 3 (P3) or start on Polish
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Python 3.14+ required - verify with `python --version`
- Use 'v' tool for all dependency and script management
- Follow constitution: add emojis to output, clear error messages, complete documentation before merge
