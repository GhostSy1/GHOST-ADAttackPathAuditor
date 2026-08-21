# GHOST-ADAttackPathAuditor

Authorized Active Directory attack path and misconfiguration auditor. Developed by Abdulaziz (Ghost-SY1).

## Overview

`GHOST-ADAttackPathAuditor` is a specialized tool designed for authorized red team and Active Directory security assessments. It inspects local export artifacts (such as BloodHound JSON exports, group policy backups, or LDAP dumps), computes SHA-256 integrity hashes, identifies privilege escalation paths and delegation risks, and generates structured JSON, CSV, and SARIF reports without executing network requests or live exploitation.

## Installation & Setup

```bash
git clone https://github.com/GhostSy1/GHOST-ADAttackPathAuditor.git
cd GHOST-ADAttackPathAuditor
python3 main.py --help
```

## Usage

```bash
python3 main.py --input ./ad_exports/ --output report.json --sarif report.sarif
```
