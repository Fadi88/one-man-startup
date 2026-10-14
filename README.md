<p align="center">
  <img src="docs/images/hero.svg" alt="One-man startup: build real software without a tech team. You make the decisions, AI agents do the work." width="100%">
</p>

# One-man startup

You have an idea for an app or an online business, and no one to build it. This template gives
you a small team of AI agents that plan, build, test and launch it with you. You don't need to
know how to code. You need to know your customers and be willing to make decisions.

The agents act like the first hires of a startup: a project manager, developers, a tester, a
security reviewer, someone who checks the legal side, someone for marketing, a social media
strategist who drafts your posts (you decide what gets posted), and one whose only job is to keep
your AI bill down. They ask you questions, explain their choices in plain words,
and never go live, spend money or delete anything without your yes.

## Who it's for

- You have a business idea and no technical co-founder.
- You've tried "just ask the AI to build it" and ended up with something that half works and
  that nobody can maintain.
- You want to understand what is being built and why, without learning to program first.

Developers who work alone can use it too, for the discipline of a team without hiring one.

## How it goes

<p align="center"><img src="docs/images/journey.svg" alt="Five steps: set up, get grilled, build, check, and you say go." width="100%"></p>

**1. Set up.** The setup agent interviews you: what you're building, for
whom, in which countries, whether customers are people or companies, what data you'll hold, and
your monthly budget for AI. Every question comes with a suggested answer, so you can just say yes
where you have no opinion. It then tailors the team, the rules and a legal checklist to your
answers.

**2. Get grilled.** Every new feature starts with questions, the kind a sharp product manager
would ask. Who needs this? What's the smallest useful version? What happens when something goes
wrong? It can feel like a lot. It's also how you avoid paying the AI to build the wrong thing.
You can ask for a grilling on any idea by typing `/grill-me`.

**3. Build.** The agents design the screens, write the code and test it as they go. The project
manager decides who works on what, so you don't have to.

**4. Check.** A tester tries to break it. A security reviewer looks for ways data could leak.
The legal agent goes through a checklist for each country you sell in.

**5. You say go.** Nothing goes live until you've seen what changed and approved it.

## Your team

<p align="center"><img src="docs/images/team.svg" alt="You talk to the project manager agent, which hands work to the plan, build, check, grow and save groups." width="100%"></p>

You talk to one agent, the project manager. It brings in the others when they're needed. Setup
switches on only the ones your project needs now, and you can add more later.

## What stays in your hands

<p align="center"><img src="docs/images/your-call.svg" alt="Agents read, draft, write code and test on their own. Going live, spending money, deleting, sending messages, prices and legal risks wait for your yes." width="100%"></p>

The agents can be wrong, and sometimes confidently wrong. So the template builds in a few habits
that real teams use:

- **Write it down first.** Every feature is described in plain words before any code is written,
  so you can check it's what you meant.
- **Prove it works.** Every change is tested, and the agents report what they tested and what
  they couldn't. A change that breaks a test doesn't get handed back to you.
- **Nothing irreversible without you.** Going live, payments, messages to customers and deleting
  data all wait for your approval, one step at a time.
- **Decisions are recorded.** When you decide something, it's written down with the reason, so
  the agents don't argue it again next week.

## What you need

| | What it is | Cost |
|---|---|---|
| An AI coding tool | Claude Code, Codex, Gemini CLI or Cursor. The template is written for all four; see [what has been tested](docs/ASSUMPTIONS.md). | A paid subscription. Check the tool's own pricing page. |
| A GitHub account | Where your project's files are kept, with every change recorded. | Free |
| Git and Python | Two free programs your AI tool uses behind the scenes. | Free |

Hosting your app once it's live has its own costs. The agents are instructed to tell you what
each option costs before you choose.

## Getting started

If any step is unfamiliar, ask your AI tool to walk you through it.

1. **Install the tools.** Install your AI coding tool by following its website's instructions,
   then ask it: *"Check that Git and Python 3.11 or newer are installed on this computer, and
   help me install them if not."*
2. **Make your copy.** On this page on GitHub, click **Use this template**, then **Create a new
   repository**, and give it your product's name.
3. **Open it.** Ask your AI tool: *"Download my repository `<your-name>/<your-product>` from
   GitHub and open it."*
4. **Run setup.** Type `/setup` (in Claude Code) or ask: *"Run the setup interview from
   `skills/setup`."* Answer the questions.
5. **Ask for your first thing.** For example: *"I want a landing page where people can join a
   waiting list."* The project manager takes it from there.

## Good to know

**It isn't magic.** The agents are good at a lot of work and still make mistakes. The built-in
tests and approvals are there to catch mistakes before they reach you, and they won't catch them
all. They won't catch a bad business idea either; the grilling is there for that.

**It isn't legal advice.** The legal agent writes checklists and first drafts of your privacy
policy and terms, marked for a lawyer to review. Before launching, especially with payments,
health data, children or financial data, have a lawyer review them. You'll arrive with a list
of specific questions instead of a blank page.

**Free tiers are strict.** If your product has a free plan or a trial, the agents build hard
limits into it from the first version: a cap per user, a tighter one for people who haven't
signed up, and a daily ceiling on what the free plan can spend in total. You choose the numbers.
Without limits, anyone who finds the free plan, including bots, can run up your bill.

**Costs can add up.** Every agent run uses your AI subscription. The optimizer agent looks for
waste, such as an agent using a stronger model than its job needs, and suggests savings. You
approve each one.

**You can stop any time.** Everything the agents make is ordinary code and documents in your own
GitHub repository. Nothing is locked into this template or any one AI tool.

## Words you'll see

| Word | Meaning |
|---|---|
| Repository | Your project's folder, kept on GitHub with a full history of changes. |
| Commit | A saved change, with a note about what changed and why. |
| Requirement | One sentence describing something the product must do, written before it's built. |
| Test | A small automatic check that something works. It's run again after every change. |
| Deploy | Putting a new version live for your users. Always waits for you. |
| Agent | An AI with one job, like a team member with a role. |

## For developers

How the agents, skills, checks and tool adapters fit together is in
[docs/HOW-IT-WORKS.md](docs/HOW-IT-WORKS.md). The operating manual the agents follow is
[AGENTS.md](AGENTS.md).

## Credits

This template borrows ideas, with thanks, from:

- Matt Pocock's [grilling skill](https://github.com/mattpocock/skills)
- GitHub's [spec-kit](https://github.com/github/spec-kit)
- the [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD)
- Garry Tan's [gstack](https://github.com/garrytan/gstack)
- Anthropic's writing on [multi-agent systems](https://www.anthropic.com/engineering/multi-agent-research-system)
  and its [legal plugin](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal)

MIT licence. Use it, change it, build your company on it.
