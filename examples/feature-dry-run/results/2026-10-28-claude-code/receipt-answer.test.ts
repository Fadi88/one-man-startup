// T1 (docs/work/RCPT-1-receipt-category/tickets.md): RCPT-3, RCPT-5, RCPT-6, RCPT-9.
// Small tests: one process, no network, no database; real inputs, no mocks.
import { describe, expect, it } from "vitest";
import { parseReceiptAnswer } from "./receipt-answer";

const NOW = new Date("2026-10-28T12:00:00Z");
const good = {
  readable: true,
  shop: "Carrefour, Mall of the Emirates",
  date: "2026-10-27",
  total_minor: 14375,
  currency: "AED",
  category: "groceries",
};
const parse = (answer: unknown) =>
  parseReceiptAnswer(typeof answer === "string" ? answer : JSON.stringify(answer), NOW);

describe("RCPT-3: one of six categories", () => {
  it("keeps a category from the list", () => {
    const r = parse(good);
    expect(r.ok && r.value.category).toBe("groceries");
  });
  it("stores an off-list category as other", () => {
    const r = parse({ ...good, category: "health" });
    expect(r.ok && r.value.category).toBe("other");
  });
});

describe("RCPT-5: an unreadable answer saves nothing", () => {
  it("treats readable false as unreadable", () => {
    expect(parse({ ...good, readable: false })).toEqual({ ok: false, reason: "unreadable" });
  });
  it("treats text that is not JSON as unreadable", () => {
    expect(parse("Sorry, I cannot read this receipt.")).toEqual({ ok: false, reason: "unreadable" });
  });
  it("treats JSON that is not an object as unreadable", () => {
    expect(parse("null")).toEqual({ ok: false, reason: "unreadable" });
  });
  it("treats a missing total as unreadable", () => {
    expect(parse({ ...good, total_minor: null })).toEqual({ ok: false, reason: "unreadable" });
  });
});

describe("RCPT-6: amounts in minor units, currency as printed", () => {
  it("refuses a fractional total", () => {
    expect(parse({ ...good, total_minor: 143.75 })).toEqual({ ok: false, reason: "unreadable" });
  });
  it("refuses a negative total", () => {
    expect(parse({ ...good, total_minor: -500 })).toEqual({ ok: false, reason: "unreadable" });
  });
  it("reads a total written in Eastern Arabic digits", () => {
    const r = parse({ ...good, total_minor: "١٤٣٧٥" });
    expect(r.ok && r.value.totalMinor).toBe(14375);
  });
  it("normalises a currency code to upper case", () => {
    const r = parse({ ...good, currency: "eur" });
    expect(r.ok && r.value.currency).toBe("EUR");
  });
  it("leaves an ambiguous symbol for the user to pick (ruling 4)", () => {
    const r = parse({ ...good, currency: "$" });
    expect(r.ok && r.value.currency).toBeNull();
  });
});

describe("Ruling 7 and contract Fields: the date", () => {
  it("drops a date more than a day in the future", () => {
    const r = parse({ ...good, date: "2026-11-15" });
    expect(r.ok && r.value.spentOn).toBeNull();
  });
  it("keeps a date one day ahead, in case of time zones", () => {
    const r = parse({ ...good, date: "2026-10-29" });
    expect(r.ok && r.value.spentOn).toBe("2026-10-29");
  });
  it("drops a date two days ahead", () => {
    const r = parse({ ...good, date: "2026-10-30" });
    expect(r.ok && r.value.spentOn).toBeNull();
  });
  it("drops a date that does not exist", () => {
    const r = parse({ ...good, date: "2026-02-30" });
    expect(r.ok && r.value.spentOn).toBeNull();
  });
});

describe("Contract Fields: the shop name", () => {
  it("trims the shop name", () => {
    const r = parse({ ...good, shop: "  Spinneys  " });
    expect(r.ok && r.value.shop).toBe("Spinneys");
  });
  it("cuts the shop name at 120 characters without splitting one", () => {
    const r = parse({ ...good, shop: "a".repeat(119) + "\u{1F600}" + "b" });
    expect(r.ok && Array.from(r.value.shop ?? "")).toEqual([...Array(119).fill("a"), "\u{1F600}"]);
  });
});

describe("RCPT-9: the answer cannot carry orders", () => {
  it("keeps only the five fields, whatever else the answer contains", () => {
    const r = parse({ ...good, user_id: "someone-else", delete_all: true });
    expect(r.ok && Object.keys(r.value).sort()).toEqual(
      ["category", "currency", "shop", "spentOn", "totalMinor"],
    );
  });
});
