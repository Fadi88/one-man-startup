# Setup step 1: check the computer

Part of `skills/setup/SKILL.md`.

Check, without asking, that Git and Python 3.11 or newer run on this computer (`git --version`,
then `python --version`, `python3 --version` or `py --version`); the checks need both. Say the
result in one line inside your first message. If one is missing, explain in plain words what it
is for, give the official download page, and offer to install it; install only on the founder's
go.

Then check the repository: `python tools/repo_visibility.py`. If it says PUBLIC, tell the founder
in their words that anyone on the internet can read everything here (the idea, the decisions,
the code), recommend making it private, and give the steps (`skills/human-steps/`): on the
repository's page on GitHub, Settings, then "Change visibility" in the "Danger Zone" section
(GitHub's guide, "Setting repository visibility", opened 2026-10-17:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).
Run the check again after. The choice is theirs; carry it into the summary, and step 3 records a
public repository they keep. NO REMOTE means it is not on GitHub yet: recommend Private when they
put it there. OTHER HOST means it is not on GitHub: ask the founder whether that service shows
the project to strangers. UNKNOWN means GitHub could not be reached: ask the founder to look at
the repository's page.
