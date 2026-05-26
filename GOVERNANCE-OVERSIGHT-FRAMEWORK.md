# Change Management Governance Oversight Framework

**A practitioner's guide to governing the change management process —
not just tracking changes, but ensuring the governance system holds.**

---

## Purpose

Most change management programs track changes well. Fewer govern the
process itself. This framework closes that gap.

This document defines the governance layer that sits above individual
change requests — the ownership structures, oversight cadences,
escalation paths, and audit evidence requirements that make change
management a governed system rather than a documented one.

Use this alongside the change request templates and CAB log in this
repository.

---

## Section 1: Governance Ownership Structure

Every change management program needs named accountable parties at
three levels.

### Process Owner
The single person accountable for the overall health and effectiveness
of the change management process. Responsible for:
- Ensuring the process is followed consistently
- Reviewing and approving updates to process documentation
- Escalating systemic failures to leadership
- Reporting change governance metrics to executive stakeholders

**Named Process Owner:** ________________________

**Review cadence:** Quarterly process health review

---

### CAB Chair
The person responsible for facilitating Change Advisory Board meetings,
ensuring quorum, and maintaining CAB records. Responsible for:
- Scheduling and running CAB sessions on the defined cadence
- Ensuring all standard changes are reviewed before approval
- Maintaining the CAB log with decisions and rationale
- Flagging emergency changes that bypassed CAB for retrospective review

**Named CAB Chair:** ________________________

**Backup CAB Chair:** ________________________

---

### Change Owners
Each individual change request must have a named change owner who is
accountable for:
- Accurate and complete change request documentation
- Coordinating testing and implementation activities
- Completing post-implementation review (PIR) within the defined window
- Notifying stakeholders of implementation status and outcomes

Change ownership cannot be assigned to a team or department. It must
be a named individual.

---

## Section 2: CAB Governance Standards

### Meeting Cadence

| CAB Type | Frequency | Quorum Requirement | Scope |
|---|---|---|---|
| Standard CAB | Weekly | Minimum 3 approvers | Normal and standard changes |
| Emergency CAB | As needed | Minimum 2 approvers | Emergency changes only |
| Post-Implementation Review | Monthly | Process owner required | PIR review for prior period |

### Approval Thresholds

| Change Risk Level | Approvers Required | CAB Review Required |
|---|---|---|
| Low | 1 technical approver | No — standard approval |
| Medium | 2 approvers including 1 business | Yes |
| High | 3 approvers including process owner | Yes — mandatory |
| Emergency | 2 approvers — retrospective CAB within 48 hours | Retrospective |

### CAB Record Requirements

Every CAB session must produce a record that includes:
- Date, time, and attendees
- Changes reviewed with risk ratings
- Approval or rejection decision with documented rationale
- Any conditions attached to approval
- Emergency changes approved outside CAB since last session
- Outstanding PIRs and their status

CAB records must be retained for a minimum of 3 years and stored in
the designated evidence repository.

---

## Section 3: Change Risk Assessment Standards

All change requests must include a risk assessment before CAB review.
Use the following rating criteria for consistency.

### Likelihood Rating

| Score | Definition |
|---|---|
| 1 — Rare | Unlikely to occur under normal conditions |
| 2 — Unlikely | Could occur but historical precedent is low |
| 3 — Possible | Has occurred before in similar conditions |
| 4 — Likely | Expected to occur without strong controls |
| 5 — Almost Certain | Will occur without intervention |

### Impact Rating

| Score | Definition |
|---|---|
| 1 — Negligible | No user impact, no data risk, fully reversible |
| 2 — Minor | Limited user impact, short duration, easily reversed |
| 3 — Moderate | Noticeable user impact, extended duration, reversible with effort |
| 4 — Major | Significant user impact, potential data exposure, difficult to reverse |
| 5 — Critical | Widespread outage, data loss risk, irreversible without full recovery |

**Risk Score = Likelihood x Impact**

| Score Range | Risk Level | CAB Escalation |
|---|---|---|
| 1-4 | Low | Standard approval path |
| 5-9 | Medium | CAB review required |
| 10-19 | High | CAB review + process owner approval |
| 20-25 | Critical | CAB review + executive notification required |

---

## Section 4: Post-Implementation Review (PIR) Requirements

A PIR is required for all medium, high, and critical changes within
the defined window after implementation.

### PIR Completion Window

| Change Risk Level | PIR Required | Completion Window |
|---|---|---|
| Low | Optional | N/A |
| Medium | Yes | Within 5 business days |
| High | Yes | Within 3 business days |
| Critical | Yes | Within 24 hours |

### PIR Documentation Requirements

Each PIR must document:

**Implementation outcome**
Did the change implement as planned? If not, what deviated and why?

**Rollback status**
Was a rollback required? If yes, what triggered it and was the rollback
plan executed effectively?

**User impact**
What was the actual user or business impact compared to what was
assessed in the change request?

**Lessons learned**
What would be done differently? What process or documentation
improvements are recommended?

**Evidence of completion**
Screenshot, ticket closure record, or sign-off confirming the change
is complete and stable.

PIRs that are not completed within the defined window must be escalated
to the process owner and flagged in the next CAB session.

---

## Section 5: Emergency Change Governance

Emergency changes are the highest-risk category in any change
management program because they bypass normal review and approval
controls. They require the strongest governance oversight as a result.

### Emergency Change Criteria

A change qualifies as emergency only when all three of the following
are true:
- An active or imminent incident is occurring or will occur without the change
- The change cannot wait for the next scheduled CAB session
- Delaying the change would result in material harm to operations, security, or data

Changes that are simply urgent or that missed the CAB submission
deadline do not qualify as emergency changes.

### Emergency Change Process

1. Change owner documents the change request as completely as possible
   given time constraints
2. Minimum two approvers authorize verbally or via documented message
   before implementation
3. Change is implemented with real-time documentation of actions taken
4. Post-implementation documentation is completed within 4 hours
5. Retrospective CAB review is conducted within 48 hours
6. Emergency change is logged in the emergency change register

### Emergency Change Oversight

Emergency changes must be reviewed in aggregate monthly by the process
owner. Patterns of emergency changes — repeated emergency changes in
the same system, by the same team, or for the same type of issue —
signal a governance design failure that must be addressed at the
process level, not the individual change level.

---

## Section 6: Audit
