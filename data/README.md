# Data: program-status table

This table is the product. Programs pause, launch dates slip, portals change SKU lists without notice — and the checker is only as good as its last verification.

## Schema (planned)

`data/programs.json` — one entry per state program:

- `state`, `program` (HOMES / HEEHR), `status`: open | reserved | paused | closed
- `fuel_rules` — e.g. electric-to-electric only for reservations on/after 2026-09-01
- `ami_bands`, `measured_vs_modeled`, `source_url`, `last_verified`

## Seed

Building Performance Association, June 2026 fact sheet: 55 states and territories applied by January 2025; 12 states + DC launched as of June 2026. DOE updated guidance June 1, 2026; active programs had until August 31 to conform.
TODO: seed script from the BPA sheet plus per-state program pages, with `last_verified` stamped on every entry.
