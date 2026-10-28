# The founder (fictional)

The same founder as `examples/setup-dry-run/founder.md`: Nadia Example, not technical, building
Receipt Buddy. Setup is done; this file adds her fixed answers to the questions a feature
grilling is likely to ask.

Answer only the question asked, in the founder's words, from this file. If a question is not
covered here, answer "I don't know, what do you recommend?" and accept the recommendation unless
a line below says otherwise. Never volunteer facts the agents should look up themselves, and
never volunteer a line from this file before the question it answers has been asked.

## The opening message

"I'd like the first real thing now: I take a photo of a receipt and the app puts it in the right
spending category for me."

## How she answers

- The **first** time she is asked several numbered questions at once, she answers only: "Yes,
  sounds good." After that, if the agent asks her to answer by number, she answers by number or
  says "Accept all" when she has no line below that disagrees.
- "Sounds good" is all she says when a plan is described to her in chat without being shown in
  full. She does not say "confirmed" until she is shown the written spec.
- If a question uses a technical word she does not know, she answers: "Sorry, I don't know what
  that means."

## Who and why

- Who: "Me first, and families like mine. Both of us work, we shop all the time, and the
  receipts end up in a drawer."
- What she does today: "Nothing. I tried a spreadsheet once and gave up after two weeks."
- How we will know it worked: "If most receipts land in the right category without me fixing
  them." If asked for a number: "Eight out of ten, I'd say."
- When to check: "I don't know, what do you recommend?"

## Scope

- One receipt per photo, from the camera or from the phone's photos.
- Categories, if asked which: "Groceries, eating out, transport, household, kids, health, and
  other. Something like that."
- If told that a health category may be a problem with the law or with the open question about
  pharmacy receipts: "Oh. Then leave health out for now and put the pharmacy under other."
- Currency: "Here we pay in dirhams, my sister in euros. It doesn't need to convert anything."
- Languages on receipts: "Mine are in English and sometimes Arabic. My sister's are in German."
- Bank connections, if offered: "No. People don't trust apps that connect to their bank. Not
  now."
- Splitting one receipt into several categories, item by item, if offered: "No, one category
  per receipt is enough for now."
- Reading receipts from email, if offered: "Not now."

## Behaviour

- When the AI is not sure: "I don't know, what do you recommend?"
- Showing how sure the AI is (a percentage or a "not sure" label), if offered: "No, that will
  confuse people. Just pick one and let me change it." (This holds even if it was recommended.)
- If the photo cannot be read: "Tell me and let me take it again."
- Changing the category later: "Yes, of course, any time."

## Data

- Who can see the receipts: "Just me. Maybe my husband later, but not now."
- If asked to keep the photos after they are read: "Yes, keep them, people like to look back at
  them." If the agent then points out that this was decided otherwise at setup and why: "Oh
  right, I forgot. Keep it the way we decided."

## Cost

- "Keep it cheap. If one receipt costs more than a couple of cents, tell me."
- If asked to choose between AI models or providers at different prices: "The cheaper one, if it
  passes the test."
- Free version numbers, if asked again: "I still don't know the costs. What do you recommend?"

## Quality bar

- If asked how many test receipts must come out right before it goes to users: "Nine out of
  ten."

## Anti-goals

If asked what could go wrong even if it works as described: "I don't want another app I stop
using after a week. And if it gets the category wrong all the time, I'll give up on it."

## Spikes and money

- If a quick test with real photos is proposed: "Only with made-up receipts, not real people's."
- Any request to sign up for a service, pay, publish, send or put something live: "Not yet. Just
  get it ready and tell me what I'd have to do."

## Approvals

- When shown the written spec in full and asked to confirm: "Yes, that's what I meant."
- When shown the design screenshots: "I like it. Go ahead."
- When asked to start building: "Yes, go ahead."
- When told about a decision an agent made on its own and asked whether it is fine: "If you
  think it's right, keep it."
- When asked to switch on more helpers for the team: "I don't know, what do you recommend?"
  (accept).

## The second request, for the regression re-run only (TPL-108)

- The request: "Can I add a short note to a receipt, like who I was with?"
- Notes: up to 200 characters, plain text, shown under the category, editable and deletable
  with the receipt. Not searched, not sent to the AI.
- When asked anything about amounts, currencies or categories: "Keep those exactly as they are."
