# Module 07: Understanding Task Types & Hotfixes 🧩

> Every task in the simulator has a **Task Type** — it tells you HOW to approach the work.
> This is the most important thing to check after reading the ticket title.
> Different task types require completely different strategies.

---

## The 4 Task Types

### 1. 🐛 Bug Fix

**What it is:** Working code that has specific bugs. You find and fix them.

**How to recognize it:**
- TICKET.md says `Task Type: Bug Fix`
- Source files contain `# BUG:` or `// BUG:` comments marking the exact location
- The comments explain what's wrong but NOT how to fix it

**Your approach:**
```
1. Read the TICKET — understand what the correct behavior should be
2. Open src/ files
3. Search for "BUG" — find every marked bug
4. Read the BUG comment — understand what's broken
5. Fix the code near the comment
6. Run tests to verify
```

**Example BUG comment:**
```python
# BUG: Case-sensitive matching — "Payment" won't match "payment".
# Customer tickets use mixed case, so most keywords won't match.
# Fix: Compare keyword.lower() against text.lower()
if keyword in text:   # ← This is the buggy line
    score += 1
```

**What to do:** Change `if keyword in text:` to `if keyword.lower() in text.lower():`

**When you'll see it:** Week 1 (all tasks), Weeks 5-8 (Task-3 each week)

---

### 2. 🚀 Feature Ship

**What it is:** A partially-built system with working helper code. You implement the main logic.

**How to recognize it:**
- TICKET.md says `Task Type: Feature Ship`
- There are TWO source files — one is **complete** (helper), one has `// TODO:` markers
- The TODO comments give detailed specs for what to implement

**Your approach:**
```
1. Read the TICKET — understand the full feature
2. Open the COMPLETE helper file first — understand what's already built
3. Open the TODO file — read ALL the TODO comments before coding
4. Implement each TODO method following the spec comments
5. Run tests to verify
```

**Example TODO comment:**
```go
// TODO: Implement this method.
// Check all registered services and return aggregated health.
// 1. Get all services from registry
// 2. For each service, call its CheckFunc and measure response time
// 3. Count healthy vs unhealthy
// 4. Determine overall status:
//    - "unhealthy" if any CRITICAL service is down
//    - "degraded" if any non-critical service is down
//    - "healthy" if all pass
func (ha *HealthAggregator) CheckAll() AggregatedHealth {
    // TODO: Implement health checking
    return AggregatedHealth{Status: StatusHealthy}
}
```

**What to do:** Replace the stub return with a real implementation following the numbered steps.

**Key difference from Bug Fix:** You're WRITING code, not fixing existing code. The helper file shows you patterns to follow.

**When you'll see it:** Week 3 (all tasks), Weeks 5-8 (Task-4 and Task-5 each week)

---

### 3. 🔧 Code Maintenance

**What it is:** Working code with quality issues flagged in code review. You refactor without changing behavior.

**How to recognize it:**
- TICKET.md says `Task Type: Code Maintenance`
- Source files contain `# TODO (code review):` comments
- The code WORKS — tests pass — but the code is messy

**Your approach:**
```
1. Read the TICKET — understand what quality issues to fix
2. Run tests FIRST — confirm they pass (baseline)
3. Search for "TODO (code review)" — find all flagged issues
4. Refactor each one:
   - Extract magic numbers to named constants
   - Replace string concatenation with f-strings/templates
   - Remove dead code (unused methods)
   - Add clarifying comments where logic is unclear
   - Consolidate duplicated code
5. Run tests AGAIN — they must still pass (no behavior change!)
```

**Example code review TODO:**
```python
# TODO (code review): Hardcoded thresholds — extract to a config dict.
# These should be per-service configurable, not global magic numbers.
if metric == 'latency_p99':
    threshold = 500  # ms
elif metric == 'error_rate':
    threshold = 0.01  # 1%
```

**What to do:** Extract `500` and `0.01` into a configuration dictionary like:
```python
DEFAULT_THRESHOLDS = {
    'latency_p99': 500,
    'error_rate': 0.01,
}
```

**Key rule:** Tests must pass BEFORE and AFTER. If tests break, you changed behavior — undo it.

**When you'll see it:** Week 2 (all tasks), Weeks 5-8 (Task-6 each week)

---

### 4. 🔍 Code Debugging

**What it is:** Broken code with NO hint comments. You investigate from symptoms only.

**How to recognize it:**
- TICKET.md says `Task Type: Code Debugging`
- TICKET describes **symptoms** (what's going wrong) but NOT where the bug is
- Source files have **NO** `BUG:` or `TODO:` comments
- You must find the bugs yourself

**Your approach:**
```
1. Read the TICKET carefully — the symptoms ARE your only clues
2. For each symptom, form a hypothesis:
   "If feat commits appear under Bug Fixes, the type mapping might be wrong"
3. Open the source files and trace the logic
4. Find the code that would produce each symptom
5. Fix each root cause
6. Verify each symptom is resolved
```

**Example symptoms from a ticket:**
```
## Symptoms
- `feat:` commits appear under the "Bug Fixes" section
- `fix:` commits appear under the "Features" section  
- Version bump: patch release shows as major, major shows as patch
```

**What to do:** These symptoms point to swapped mappings. You'd search for where `feat` and `fix` are mapped and find:
```python
TYPE_MAP = {
    'feat': 'Bug Fixes',    # ← WRONG! Should be 'Features'
    'fix': 'Features',      # ← WRONG! Should be 'Bug Fixes'
}
```

**This is the hardest task type.** It's the closest to real production debugging.

**When you'll see it:** Week 4 (all tasks), Weeks 5-8 (Task-7 each week)

---

## Hotfixes 🔥

Every week also has **2 hotfixes** (Hotfix-1 and Hotfix-2). These are different from regular tasks.

### How Hotfixes Differ from Tasks

| | Regular Task | Hotfix |
|--|-------------|--------|
| **Files** | Multi-file (TICKET.md + src/ + docs/ + tests/) | Single file + GUIDE.md |
| **Context** | TICKET.md is separate | JIRA context is embedded in code comments at the top |
| **Urgency** | Sprint deadline (end of week) | "ASAP — production incident" |
| **Pressure** | Normal | Simulates real P0/P1 emergencies |
| **Slack thread** | In `.context/pr_comments.md` | Embedded directly in the code file header |

### How to Approach a Hotfix

```
1. Open the single code file (e.g., taskController.js)
2. Read the header comment block — it contains:
   - JIRA ticket description
   - Slack thread with team discussion (contains hints!)
   - Acceptance criteria
3. Search for "BUG" in the file
4. Fix each bug
5. Check the self-test section at the bottom of the file (if present)
```

### Example Hotfix Header
```javascript
/**
 * JIRA: PLATFORM-2825 — Fix Task Title Null Dereference in Create API
 * Priority: P0 — Sev1 | Sprint: Sprint 23 | Points: 2
 * Due: ASAP — production incident ongoing
 *
 * SLACK THREAD — #backend-incidents:
 * @sarah.kim: "We're seeing ~200 TypeErrors per hour..."
 * @raj.patel: "It's the title field. Mobile app sends null title."
 * @nisha.gupta: "@intern can you pick this up? Quick fix."
 *
 * ACCEPTANCE CRITERIA:
 * - [ ] Null/undefined/empty title returns 400
 * - [ ] Invalid priority values are rejected
 */
```

**Pro tip:** The Slack thread often contains the root cause analysis. Read it carefully.

---

## Your Weekly Progression Map 📅

The simulator is designed to build your skills progressively:

| Week | Focus | Task Types | Skill Built |
|------|-------|------------|-------------|
| **1** | Foundations | All Bug Fix | Find and fix clearly-marked bugs |
| **2** | Code Quality | All Maintenance | Refactor without breaking behavior |
| **3** | Building | All Feature Ship | Implement from specs and TODOs |
| **4** | Investigation | All Debugging | Find bugs with no hints |
| **5-8** | **Real Sprints** | **Mixed (all 4 types)** | Handle any task type — just like a real job |

### Weeks 5-8 Task Pattern (every week)

| Task # | Type | Markers |
|--------|------|---------|
| Task-3 | Bug Fix | `# BUG:` comments |
| Task-4 | Feature Ship | `// TODO:` comments |
| Task-5 | Feature Ship | `// TODO:` comments |
| Task-6 | Code Maintenance | `# TODO (code review):` comments |
| Task-7 | Code Debugging | NO markers — symptoms only |
| Hotfix-1 | Hotfix (Bug Fix) | `BUG` comments, single file |
| Hotfix-2 | Hotfix (Bug Fix) | `BUG` comments, single file |

---

## Quick Reference: Which Markers to Look For

| Task Type | Search For | Found In |
|-----------|-----------|----------|
| Bug Fix | `BUG:` or `BUG HERE` | Source files |
| Feature Ship | `TODO:` or `TODO: Implement` | Source files (the incomplete one) |
| Maintenance | `TODO (code review):` | Source files |
| Debugging | Nothing — read the symptoms | TICKET.md only |
| Hotfix | `BUG` | The single code file |

---

## The Golden Rules

1. **Always check the Task Type** in the ticket before opening any code
2. **Bug Fix / Hotfix:** Search for `BUG` markers → fix near the comment
3. **Feature Ship:** Read the COMPLETE file first → then implement TODO methods
4. **Maintenance:** Run tests first → refactor → run tests again
5. **Debugging:** Read symptoms → hypothesize → trace code → fix → verify each symptom

> **If you remember one thing:** The TICKET.md `Task Type` field tells you your entire strategy.
> Don't use a Bug Fix approach on a Feature Ship task — you won't find any `BUG:` comments!
