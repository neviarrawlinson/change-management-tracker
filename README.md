# Change Management Tracker

Change Management Tracker is a lightweight tool designed to help organizations document, assess, and approve changes to systems, processes, and infrastructure. It supports IT and business teams in maintaining oversight, ensuring compliance, and minimizing operational risk during change implementation.

This tracker is especially useful for teams operating under IT governance frameworks such as ITIL, COBIT, ISO 27001, and NIST, where structured change documentation and audit readiness are essential.

---

## Features

- Structured Change Request Template (Excel)
- Risk Assessment Matrix aligned to change categories
- Change Log for tracking status, risk levels, and approvals
- Optional CAB Review Log and Implementation Calendar
- Roles and responsibilities reference for governance alignment

---

## Use Cases

- IT Operations teams needing structured change control processes
- GRC and compliance teams documenting controls and approvals
- Business units implementing internal or infrastructure changes
- Audit preparation and internal governance reporting

---

## How to Use This Tracker

1. **Start with the Change Request Form**  
   Download the template in `/templates` and fill in:
   - Change Title
   - Description and Justification
   - Type of Change (Normal, Emergency, Standard)
   - Risk Assessment (Likelihood x Impact)
   - Mitigation Plan
   - Proposed Implementation Window
   - Stakeholders and Approvers

2. **Log Approved Requests in the Change Log**  
   Use the `change_log.xlsx` to track:
   - Status (Submitted, Approved, Rejected, Closed)
   - Change Owner
   - Approval Date
   - Risk Score
   - Implementation Notes

3. **Optional: Use the CAB Log**  
   Document discussion points, approvals, or decisions made during Change Advisory Board (CAB) meetings.

4. **Track Roles and Responsibilities**  
   Reference the `roles_responsibilities.md` in the `/docs` folder to define key actors in your process.

---

## Folder Structure

change-management-tracker/
│
├── templates/
│ ├── change_request_form.xlsx
│ ├── change_log.xlsx
│ └── risk_assessment_matrix.xlsx
│
├── docs/
│ ├── process_overview.md
│ ├── roles_responsibilities.md
│ └── sample_change_log.md
│
└── README.md


---

## Framework Alignment

This tracker aligns with:
- **ITIL v4** – Change Enablement Practice
- **COBIT** – BAI06 Manage Changes
- **ISO 27001** – A.12.1.2 Change Management
- **NIST 800-53** – CM-3 Configuration Change Control

---

## Benefits

- Promotes transparency and accountability
- Reduces risk through structured change assessment
- Ensures documentation needed for audits and governance reviews
- Supports faster, more confident decision-making for IT and operational changes

---

## Future Roadmap

- Add a simple Streamlit or web-based interface for change request submissions
- Integrate version-controlled change logs for audit trails
- Add role-based access control (RBAC) support for team collaboration

---

## License

This project is open-source and available under the MIT License.
