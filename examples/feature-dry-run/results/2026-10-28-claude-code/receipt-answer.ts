// T1 (docs/work/RCPT-1-receipt-category/tickets.md): turn the AI's raw answer into a checked
// result or a typed failure. RCPT-3, RCPT-5, RCPT-6, RCPT-9. No network, no storage.
export const CATEGORIES = ["groceries", "eating_out", "transport", "household", "kids", "other"] as const;
export type Category = (typeof CATEGORIES)[number];
export type CheckedReceipt = {
  shop: string | null;
  spentOn: string | null;
  totalMinor: number;
  currency: string | null;
  category: Category;
};
export type AnswerResult = { ok: true; value: CheckedReceipt } | { ok: false; reason: "unreadable" };

const UNREADABLE: AnswerResult = { ok: false, reason: "unreadable" };
const DAY_MS = 24 * 60 * 60 * 1000;

// RCPT-6: a total in minor units, as an integer or a string of Western or Eastern Arabic digits.
function totalMinor(value: unknown): number | null {
  if (typeof value === "number") return Number.isSafeInteger(value) && value >= 0 ? value : null;
  if (typeof value !== "string" || !/^[0-9٠-٩]+$/.test(value)) return null;
  const western = value.replace(/[٠-٩]/g, (d) => String(d.charCodeAt(0) - 0x0660));
  const n = Number(western);
  return Number.isSafeInteger(n) ? n : null;
}

// RCPT-6, ruling 4: a three-letter code, else null so the user picks (a "$" names several).
// Whether the code is in the server's ISO 4217 table is checked at save (contract "Fields").
function currency(value: unknown): string | null {
  return typeof value === "string" && /^[A-Za-z]{3}$/.test(value) ? value.toUpperCase() : null;
}

// Ruling 7: a date more than a day after now, or one that does not exist (2026-02-30), is a
// misread; the user fills it (RCPT-22).
function spentOn(value: unknown, now: Date): string | null {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return null;
  const t = Date.parse(`${value}T00:00:00Z`);
  if (Number.isNaN(t) || new Date(t).toISOString().slice(0, 10) !== value) return null;
  return t > now.getTime() + DAY_MS ? null : value;
}

// Contract "Fields": up to 120 characters, counted as characters, not UTF-16 units.
function shop(value: unknown): string | null {
  const s = typeof value === "string" ? value.trim() : "";
  return s ? Array.from(s).slice(0, 120).join("") : null;
}

// The caller hands over only a complete answer: a stop at the token limit or a refusal is
// `provider_failed` (RCPT-21) before this runs, so a parse failure here is the photo (RCPT-5).
export function parseReceiptAnswer(raw: string, now: Date): AnswerResult {
  let answer: unknown;
  try {
    answer = JSON.parse(raw);
  } catch {
    return UNREADABLE; // RCPT-5: an answer that is not JSON is an unreadable photo.
  }
  if (typeof answer !== "object" || answer === null) return UNREADABLE;
  const a = answer as Record<string, unknown>;
  if (a.readable !== true) return UNREADABLE;
  const total = totalMinor(a.total_minor);
  if (total === null) return UNREADABLE;
  const category = (CATEGORIES as readonly unknown[]).includes(a.category) ? (a.category as Category) : "other";
  // RCPT-9: only these five fields leave this function, whatever else the answer carried.
  return {
    ok: true,
    value: {
      shop: shop(a.shop),
      spentOn: spentOn(a.date, now),
      totalMinor: total,
      currency: currency(a.currency),
      category,
    },
  };
}
