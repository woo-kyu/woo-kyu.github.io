---
layout: single
title: VDI :pgi
toc_label: VDI Project Map
categories: VDI Project
tags: [Map]
author_profile: false
search: false
use_tex: false
---

> Architecture

# UniFi-/QNAP-Style VDI Controller — Technical Overview

> **Goal**  
> One powerful **main computer (Proxmox VE)** runs multiple **office VMs**.  
> Users connect from **small PoE thin clients** (Raspberry Pi class / ThinOS-like) over the internet/LAN,  
> logging in with **ID & password** to open **their VM**.  
> The **admin UI** feels like UniFi/QNAP: simple, visual, and safe to operate.

---

## 1) Personas & Core Flows

| Persona | Needs | Key Screens | Success Criteria |
|---|---|---|---|
| **Admin** | Connect Proxmox, register templates, create/assign VMs, monitor, snapshot/restore | Setup Wizard, Cluster Overview, VMs, Templates, Users/Teams, Snapshots | VM from template in ≤3 min; one-click start/stop/restore |
| **Team Operator** | Day-to-day ops for a team, schedules/quotas | Team Dashboard, Schedules, Quotas | Keep team online; easy restores; enforce simple limits |
| **End User** | Log in from any thin client, open “My VM” | Login, My VMs | 2 clicks from login to desktop; auto-reconnect |
| **Installer** | First-run onboarding/diagnostics | Setup Wizard | 15–30 min guided setup, all checks green |

---

## 2) System Architecture (High Level)

| Layer | Component | Notes |
|---|---|---|
| Hypervisor/Infra | **Proxmox VE (KVM)** | Main computer; VM templates with Cloud-Init |
| Orchestrator API | **FastAPI (Python)** | Wraps Proxmox REST; issues sessions for Guacamole; JWT auth |
| Web UI | **React + TypeScript + Tailwind** | UniFi/QNAP-style admin console + user portal |
| Remote Gateway | **Apache Guacamole** (guacd + web) | Browser-based RDP/VNC; also supports native RDP/SPICE clients |
| Identity | **JWT (MVP)** → OIDC/LDAP (later) | MFA later; device binding optional |
| Data | **PostgreSQL** (+ Redis optional) | Users/VMs/Templates/Audit/Schedules |

---

## 3) User Journey (Sequence)

### 3.1 Login → Connect (Guacamole)
sequenceDiagram
  autonumber
  participant U as User (Thin Client/Web)
  participant FE as Web UI
  participant BE as Orchestrator API
  participant DB as PostgreSQL
  participant PVE as Proxmox
  participant G as Guacamole

  U->>FE: Open Login
  FE->>BE: POST /auth/login {id,pw}
  BE->>DB: verify; issue JWT
  BE-->>FE: {access_token}

  U->>FE: Click "Connect" on VM card
  FE->>BE: POST /session/open {vmid}
  BE->>PVE: ensure VM running (start if needed)
  BE->>G: create guac connection/ticket
  G-->>BE: {guac_url}
  BE-->>FE: {guac_url}
  FE->>U: Open VM desktop in browser



### Provisioning

sequenceDiagram
  autonumber
  participant A as Admin
  participant FE as Web UI
  participant BE as Orchestrator
  participant PVE as Proxmox
  participant DB as PostgreSQL

  A->>FE: "Create VM"
  FE->>BE: POST /vm/create {template,newid,name,cores,ram,storage,ci_vars}
  BE->>PVE: clone template (async UPID)
  PVE-->>BE: {upid}
  BE->>PVE: poll /tasks/{upid}/status until "OK"
  BE->>PVE: config (cores,memory,cloud-init)
  BE->>PVE: start VM
  BE->>DB: register VM metadata/owner
  BE-->>FE: {vmid,state:"running"}


## 4) Data Model (MVP)


| Table | Key Fields | Purpose |
|---|---|---|
| **users** | id, username (unique), password_hash, role {admin, operator, user} | Authentication & role-based access |
| **teams** | id, name | Optional grouping of users |
| **vms** | id, vmid, node, owner_user_id, team_id, name, state, created_at | VM registry, synced with Proxmox |
| **templates** | id, name, vmid, os_type {win_client, win_server, linux}, requires (json), enabled | Template catalog (metadata for compliance hooks later) |
| **settings** | key, value (json) | System-wide settings: branding, mode, cluster endpoints |
| **audit** | id, actor_user_id, action, target, payload (json), ts | Immutable log of operations |
| **schedules** (future) | id, vmid/team_id, cron_expr, action | For auto start/stop/snapshot |
| **quotas** (future) | team_id, vcpu_limit, ram_mb_limit, storage_gb_limit | To enforce per-team resource limits |

**Indexes:**  
- `users.username` (unique)  
- `vms.owner_user_id` and `vms.vmid`  
- `audit.ts` for chronological queries  

<br>

## 5) REST API (MVP)

### 5.1 Authentication
| Method | Path | Body | Returns |
|---|---|---|---|
| POST | `/auth/login` | `{username, password}` | `{access_token, role}` |

### 5.2 Inventory
| Method | Path | Query | Returns |
|---|---|---|---|
| GET | `/nodes` | — | List of Proxmox nodes |
| GET | `/vms` | `mine=true/false` | VM list: `{node, vmid, name, state, owner}` |

### 5.3 Lifecycle
| Method | Path | Body | Returns |
|---|---|---|---|
| POST | `/vm/create` | `{node, template_vmid, newid, name, storage, cores, memory, ci_vars?}` | `{upid}` → client polls `/tasks/{upid}/status` |
| POST | `/vm/{node}/{vmid}/start` | — | `{state:"running"}` |
| POST | `/vm/{node}/{vmid}/stop` | — | `{state:"stopped"}` |
| DELETE | `/vm/{node}/{vmid}` | `?purge=1` | `{deleted:true}` |
| GET | `/tasks/{upid}/status` | — | `{status, exitstatus, progress}` |

### 5.4 Sessions
| Method | Path | Body | Returns |
|---|---|---|---|
| POST | `/session/open` | `{vmid}` | `{guac_url}` (or RDP/SPICE connection info) |
| POST | `/session/close` | `{vmid}` | `{closed:true}` |

**Security:**  
- JWT bearer token in `Authorization` header  
- TLS terminated at nginx reverse proxy  
- CSRF protection for web dashboard  

<br>

## 6) Admin Console (UniFi/QNAP-style UI)

### 6.1 Screens

| Screen | Widgets | Notes |
|---|---|---|
| **Setup Wizard** | PVE URL/token test, Template discovery, Branding setup | 4–6 guided steps, must end with all green checks |
| **Cluster Overview** | Node cards, CPU/RAM/IO gauges, alerts | At-a-glance health status |
| **VMs** | Table (node, vmid, owner, state, live CPU/RAM), action buttons | Start/Stop/Delete, Snapshot, Resize |
| **Templates** | Card/list view; import by VMID; cloud-init readiness check | Template tagging & search |
| **Users/Teams** | CRUD for users/teams, assign VMs, set roles | RBAC basics |
| **Snapshots** | Tree view of snapshots, create/restore actions | MVP+1 (not required for first MVP) |
| **Schedules/Quotas** | Cron editor, sliders for quotas | MVP+1 |
| **Audit Logs** | Filterable list, export to CSV/JSON | Always-on logging |

### 6.2 UX Principles
- **Big cards** and **color-coded badges** (green/amber/red) for clarity.  
- **Single-click actions** with confirmation toasts.  
- **Progress modals** for long tasks (clone/snapshot) using UPID polling.  
- **Persistent “Connect” button** visible on each VM card.  

---

## 7) Thin Client (PoE Module)

### 7.1 Minimum vs Recommended Specs

| Spec | Minimum | Recommended |
|---|---|---|
| CPU | Dual-core ARM/x86 | Quad-core low-power |
| RAM | 2–4 GB | 8 GB (for dual display, video conferencing) |
| Storage | 16–32 GB eMMC/SSD | 64–128 GB |
| Network | Gigabit Ethernet, **PoE** | + Wi-Fi 6 optional |
| Display | 1× HDMI/DP | **2× outputs** |
| Peripherals | USB keyboard/mouse | Optional USB redirection |
| OS | ThinOS/ThinStation/light Linux | Kiosk mode auto-connect |

### 7.2 Boot & Connect Logic
1. Device boots minimal OS → kiosk shell.  
2. Shows controller login → user enters credentials.  
3. Calls `/auth/login` → receives JWT.  
4. Queries `/vms?mine=true` → displays list of assigned VMs.  
5. On “Connect” → POST `/session/open {vmid}` → returns `guac_url`.  
6. Opens desktop session fullscreen via Guacamole or native RDP/SPICE.  
7. Maintains heartbeat → auto-reconnect on network drop.  

---

## 8) Config & Deployment

### 8.1 `.env.example`

PVE_BASE_URL=https://pve.local:8006/api2/json
PVE_API_TOKEN=PVEAPIToken=root@pam!demo=SECRET123
PVE_DEFAULT_NODE=pve1
PVE_TEMPLATE_VMID=9000
PVE_DEFAULT_STORAGE=local-lvm
JWT_SECRET=change_me
POSTGRES_URL=postgresql://app:pass@db:5432/app
GUACD_HOST=guacd
GUACD_PORT=4822
COMPLIANCE_MODE=false # Hooks present, disabled in MVP
BRANDING_NAME="Orbit VDI"



### 8.2 Docker Compose Services
- **api** (FastAPI backend)  
- **web** (React frontend served via nginx)  
- **db** (Postgres database)  
- **guacd + guacamole** (remote access gateway)  
- **reverse-proxy** (nginx: TLS termination, routes `/api` and `/guac`)  

**Networks:** backend (api/db/guac), edge (proxy/web).  
**Volumes:** db data, guac configs, TLS certs.  

---

## 9) Non-Functional Targets

| Area | MVP Target | Later |
|---|---|---|
| Provisioning Time | Clone→Boot ≤ 3 min | ≤ 90 sec with optimized templates |
| Connect Latency | Desktop in ≤ 3 sec (LAN) | WAN adaptive with codecs/bitrate |
| Availability | Single node | HA cluster with live migration |
| Security | TLS, JWT, RBAC minimal | MFA, OIDC/LDAP, device certificates, Vault |
| Observability | Basic Proxmox graphs | Prometheus + Grafana, alerting |
| Backup/Restore | Manual snapshots | Scheduled backups, retention policies |

---

## 10) Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Storage I/O contention | VM slowdown | NVMe/ZFS cache, staggered clones, quotas |
| Single-node failure | Outage | Spare node; cluster in v2 |
| Licensing confusion | Compliance issues | Compliance hooks coded but disabled; clear docs later |
| WAN instability | Poor UX | Guacamole settings, reconnect logic, local caching |

---

## 11) MVP Roadmap

| Phase | Scope | Deliverables | Acceptance Criteria |
|---|---|---|---|
| **MVP-0 (Week 1)** | Foundations | Repo, CI/CD, `docker-compose.yml` | All services start with `docker compose up -d` |
| **MVP-1 (Weeks 2–3)** | Auth & Inventory | `/auth/login`, `/vms`, React login & VM table | JWT works; VM list shows Proxmox data |
| **MVP-2 (Weeks 4–5)** | Provisioning | `/vm/create`, UPID polling, Create wizard | Create VM from template and boot in ≤3 min |
| **MVP-3 (Weeks 6–7)** | Sessions | `/session/open`, Guac integration | “Connect” opens VM desktop in browser |
| **MVP-4 (Weeks 8–9)** | Ops Usability | Snapshot/Restore, Resize controls | One-click snapshot restore works |
| **MVP-5 (Weeks 10–12)** | Team Features | Users/Teams CRUD, RBAC, assignments | User sees only “My VMs”; operator scoped to team |

---

## 12) Code Organization

- repo/
  - api/ (FastAPI entrypoint)
    - main.py → App init, middleware, routes mount
    - routes/
      - auth.py → Login, JWT issue
      - inventory.py → /nodes, /vms
      - lifecycle.py → VM create/start/stop/delete
      - session.py → Open/close sessions (Guac tickets)
  - core/ (business/domain logic)
    - models.py → Pydantic/ORM DTOs
    - services.py → VM orchestration, assignments, snapshots
    - policies.py → Compliance/licensing hooks (stub; COMPLIANCE_MODE flag)
  - adapters/
    - proxmox.py → Proxmox REST client
    - guacamole.py → Guac connection/ticket management
    - db.py → Postgres session, repositories
    - auth.py → Password hashing, JWT verify
  - web/ (React frontend)
    - src/
      - pages/ → Login, Dashboard, VMList, VMCreateWizard
      - components/ → Cards, Tables, TaskToast, LicenseBanner (hidden in MVP)
      - api/ → Fetcher hooks (TanStack Query)
      - store/ → Auth/session state
  - deploy/
    - docker-compose.yml
    - nginx.conf
    - initdb.sql
  - docs/
    - ADRs/ → Architecture Decision Records
    - OPERATIONS.md → Setup, template building, token creation
    - API.md → Endpoint docs
  - .env.example → Example configuration



---

## 13) Thin Client Flow (Reference)

1. Boot minimal OS → kiosk shell.  
2. Login prompt → call `/auth/login`.  
3. Fetch `/vms?mine=true` → show list of VMs.  
4. User clicks → call `/session/open`.  
5. Open `guac_url` fullscreen.  
6. Maintain heartbeat; auto-reconnect if dropped.  

---

### TL;DR
- **Core Promise:** Any admin can provision, any user can connect in 2 clicks.  
- **MVP Scope:** Login → VM list → Create/Start/Stop/Delete → Connect in browser.  
- **Design Style:** UniFi/QNAP-like console; compliance hooks exist but disabled in MVP; modular codebase ready for production.  
