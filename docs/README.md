# User Stories

### 1. User Login

As a **business owner** or **crew member**, I want to securily log in to PaintPro, so I can access information and features associated with my role.

**Acceptance Criteria:**
- Users log in using username and password.
- Invalid login attempts display error message.
- Users can log out of accounts.
- Users can only access features based on their role.


### 2. Project Management
As a **business owner**, I want to create, view, update, and manage painting projects, so I can track ongoing jobes and keep project info organized.

**Acceptance Criteria:**
- Owner can create a new painting project
- Each project includes customer name, address, description, and estimated cost.
- Owner can assign a status to each proejct (Pending, In Progress, or Completed).
- Owner can update project details
- Owner can view a list of all painting projects.
- Only authorized users can create, modify, or delete projects.

### 3. Crew Management
As a **business owner**, I want to manage crew members and assign them to painting projects, so I can organize employees and track who is working on each job.

**Acceptance Criteria:**
- The owner can add new crew members.
- Each crew member has a name, phone number, and assigned role.
- The owner can assign one or more crew members to a project.
- The owner can view crews assigned to project.
- The owner can update or remove crew assignments
- Crew members acn view projects assigned to them
- Only authorized users can manage crew information and assignments.

### 4. Invoice Management
As a **business owner**, I want to create and manage invoices for projects, so I can track customer payments and oustanding balances.

**Acceptance Criteria:**
- The owner can create an invoice per project.
- Each invoice includes customer, invoice number, description, amount, and due date.
- The owner can view all invoices
- Invoices display payment status (e.g., Unapid, Partially Paid, or Paid).
- The owner can record payments received from customers.
- The system calculates remaining balance on invoice.
- Authorized users can create, modify, or delete invoices.

### 5. Owner Dashboard
As a **business owner**, I want to view summary of projects and finances, so I can monitor business performance from one centralized location.

**Acceptance Criteria**
- The dashboard displays total numebr of active and completed projects.
- The owner can view total expected revenue from projects.
- The dashbaord displays payments received and outstanding invoice balances.
- Dashboard information updates when projects, invoices, or payments change.
- Only authorized users can access the finance dashbaord.

## Mis-User Stories and Security Mitigation

### 1. Unauthorized Access to Business Info
As a malicious user, I want to access PaintPro without valid creds, so I can view sensitive customer or payment information.

**Mitigation Criteria**
- Require authentication before acessing protected pages.
- Store passwords securely using Django's built-in password hashing.
- Implements role-based access control (RBAC).
- Restrict financial info to authorized users.
- Return access denied message when attempting to access unauthorized pages.

### 2. Unauthorized Modifications of Job Info
As a malicious user, I want to modify job details, invoices, and payment so I can manipulate business records and attempt to disrupt business operations.

**Mitigation Criteria**
- Authorized users can modify job details, invoices, and payment info.
- Role-based access control (RBAC) will be implemeted.
- Unauthorized modificication updates are denied.
- Changes to business info is tracked and logged.

## UI Mockup

![PaintPro UI Mockup](<images/Paint Pro Mockup.png>)


## C4 Diagrams

### Level 1 Context Diagram

The diagram show how the Admin, Business Owner, and Crew Member interact with PaintPro.

![PaintPro Level 1](<images/PaintPro C4 Level 1.png>)

### Level 2 Container Diagram

![PaintPro Level 2](<images/PaintPro C4 Level 2.png>)

The diagram shows how the web browser, Django app, and database communicate with each other.


### Level 3 Component Diagram

![PaintPro Level 3](<images/PaintPro C4 Level 3.png>)

The diagram shows hwo the main components of PaintPro work together to manage users, projects, crews, and invoices.
