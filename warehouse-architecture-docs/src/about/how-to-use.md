# How to Use This Book

Readers should begin at the level appropriate to their question:

| Question | Starting point |
|---|---|
| What is DW2023 and what surrounds it? | System Context |
| How does data move through the warehouse? | Current-State Overview |
| What creates a specific table? | Data Movement Register |
| What does a notebook or function do? | Processing Architecture |
| How is a business domain implemented? | Domain Architecture |
| Where is CUI processed or transmitted? | Security and Trust Boundaries |
| What changes during modernization? | Modernization Roadmap |

## Evidence hierarchy

When sources disagree, use this priority and record the conflict:

1. Observed production behavior and deployed configuration
2. Version-controlled deployment configuration
3. Version-controlled notebooks and libraries
4. Operational metadata and run history
5. Existing diagrams and written documentation
6. Interviews and undocumented institutional knowledge

Production evidence is not automatically the desired design. Differences between actual behavior and intended behavior become architecture findings.

