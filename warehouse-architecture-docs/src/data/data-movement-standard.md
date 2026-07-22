# Data Movement Standard

Every movement of data is documented independently of the assets at either end.

## Required fields

| Field | Description |
|---|---|
| Movement ID | Stable `MOV-nnnnn` identifier |
| Source | System, dataset, endpoint, or file location |
| Destination | Dataset, endpoint, or consumer |
| Executor | Job, task, notebook, function, or external service |
| Trigger | Schedule, event, dependency, or manual action |
| Mode | Batch, micro-batch, stream, CDC, or request/response |
| Interface | Protocol, connector, library, and authentication method |
| Format | Source and destination serialization |
| Cursor | Watermark, offset, version, timestamp, or key |
| Transformation | Plain-language description and code reference |
| Quality | Validation, quarantine, reject, and failure policy |
| Security | Classification, encryption, identity, and trust-boundary crossing |
| Operations | Volume, latency, retry, replay, monitoring, and support owner |

## Diagram rule

An unlabeled arrow is incomplete. Every data-flow arrow must display its movement ID and at least the mode and interface.

