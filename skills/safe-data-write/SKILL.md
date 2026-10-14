---
name: safe-data-write
description: How any write to real user or business data proves itself and stays reversible - before-image journal, read-back proof that the target changed and nothing else did, undo by change id. Use for every write, migration, backfill or bulk edit on real data.
---

# Safe data write

**Nothing may corrupt the data.** A 200 response proves the server answered, not that the data
is right.

## Every write

1. **Before:** read the target rows and the row count of the table.
2. **Journal:** append `{change_id, at, op, table, row_id, before, after}` to the change journal
   before applying. The journal stores before-images, not table snapshots.
3. **Apply** the write.
4. **Prove:** read back. The target rows hold exactly the intended values, and every other row
   is unchanged (compare a hash or the rows themselves). Return
   `{ok, rows_before, rows_after, other_rows_checked, differences}`.
5. **Accept** the write only if `ok` is true and `other_rows_checked` equals the table's row
   count minus the rows changed. Anything else: undo it and report.

An undo applies the inverse of a journal entry and is itself journalled, so undoing an undo is a
redo.

## Migrations and bulk changes

Run on a copy first, with the proof. Then on production only with the founder's go for that
exact operation, with a tested backup taken in the same session.

## Tests

Every suite that touches stored data asserts the data it did not mean to change is
byte-identical before and after.
