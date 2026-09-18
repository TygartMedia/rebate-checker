# Rebate Checker

The best energy product this year is not another savings calculator. It is the thing that reads the nameplate on the unit already sitting on the pad and tells you, this week, whether your ZIP still has an open rebate file.

Two clocks no longer match. The 25C federal credit closed for property placed in service after December 31, 2025 — the simple path is gone. The $8.8B in IRA state money (HOMES + HEEHR/HEAR) is still rolling out: 12 states and DC launched as of June 2026, most of the country still in the lag. Open last month is not open this week. That is the product surface.

## How it works

1. Photograph the outdoor nameplate or water-heater sticker. Add the ZIP.
2. Thirty seconds later: **open**, **reserved**, **paused/closed**, or **fuel-switch blocked** for that equipment in that ZIP.
3. If open: the checker drafts the state packet. A homeowner or licensed contractor signs — the model drafts, a person owns the send.

## The data problem (the real work)

State portals change eligible-SKU lists without a press release. Programs pause — Georgia paused HEAR on August 14, 2026. DOE's June 2026 guidance set an August 31 conformance date and limited HEEHR replacement to electric-to-electric for reservations on or after September 1, 2026. The `data/` program-status table is the product, and it must be maintained like one. See `data/README.md`.

## Quickstart

```bash
pip install -r requirements.txt
python src/checker.py --photo path/to/nameplate.jpg --zip 98402
```

## Build order

- **Week 1–2:** one checker. Nameplate photo + ZIP in, verdict out. No account to see the first answer.
- **Week 3–4:** a draft packet for one live state program, human signer, contingency or contractor bounty only.
- **Month 2:** the second object in the same house — water-heater sticker or the first page of the bill.
- **Month 3:** the first ugly internal scoreboard. Model families, ZIPs, weeks the portal flipped. Seed of the B2B SKU.

If you cannot get a stranger to photograph one nameplate this week, you do not have a company. You have a thesis.

---

Part of the [idea-mill series](https://tygartmedia.com/the-best-rebate-product-reads-the-nameplate-before-you-call-the-contractor/). MIT licensed.
