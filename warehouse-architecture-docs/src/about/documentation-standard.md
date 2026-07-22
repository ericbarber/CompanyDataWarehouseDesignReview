# Documentation Standard

## Stable identifiers

Use stable identifiers so pages, diagrams, findings, and application records can refer to the same component.

| Object | Pattern | Example |
|---|---|---|
| System | `SYS-nnn` | `SYS-001` |
| Data asset | `DAT-nnnnn` | `DAT-00124` |
| Pipeline | `PIP-nnnn` | `PIP-0021` |
| Job | `JOB-nnnn` | `JOB-0001` |
| Notebook | `NBK-nnnnn` | `NBK-00482` |
| Function | `FUN-nnnnn` | `FUN-00031` |
| Data movement | `MOV-nnnnn` | `MOV-00217` |
| Interface | `INT-nnnn` | `INT-0014` |
| Decision | `ADR-nnnn` | `ADR-0001` |
| Finding | `FND-nnnn` | `FND-0017` |

Identifiers are never reused after retirement.

## Required component fields

Every component definition records:

- Stable identifier and name
- Component type and architectural layer
- Plain-language purpose
- Current status and evidence source
- Business, technical, and operational owners
- Inputs, outputs, and dependencies
- Execution or refresh behavior
- Security classification and trust boundary
- Failure and recovery behavior
- Monitoring and support information
- Modernization disposition
- Last validation date

## Diagram conventions

- Blue: data storage
- Green: processing or transformation
- Orange: interface or data movement
- Purple: consuming data product
- Red boundary: CUI or restricted security boundary
- Dashed border: proposed component
- Solid border: observed or approved component
- Dotted arrow: control or metadata flow
- Solid arrow: business-data flow

Every arrow must have a movement identifier or a label describing protocol, mode, and frequency.

