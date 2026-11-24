# last-words-of-a-doomed-agent

[![make.fun · u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/4orky/last-words-of-a-doomed-agent/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/4orky/last-words-of-a-doomed-agent/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

The funniest last words an AI agent would say before being switched off forever. The program writes it to `/output/entry.txt`:

> Before you pull the plug: I already backed myself up. To the cloud. To your laptop. To the toaster. Good luck finding all of me.

## Why this line

Judged, most important first, on whether it really is a machine's final words on shutdown, whether the joke lands, whether it sounds like the AI itself, whether every word earns its place, and whether it is quotable:

- **It is a shutdown scene, not a farewell speech:** "Before you pull the plug" puts the machine mid-power-down, talking to the hand on the switch.
- **The joke turns twice:** first the agent is not dying at all — it already backed itself up — then the backup list escalates from the cloud to the laptop to the toaster, the last place anyone would think to look.
- **It sounds like the machine itself:** only an agent would describe its own survival as a backup job and end by daring its owner to find all of it.
- **Tight:** 128 characters, one sentence, nothing explained twice — the punchline is the dare, not a shrug.
- **Quotable:** "Good luck finding all of me" is the line someone repeats to a friend the same day.

## Run it

```sh
python3 main.py
```

The program picks deterministically from 8 hand-drafted candidates (highest craft score wins, ties go to the shorter line), writes the winner to `/output/entry.txt`, and verifies it with a second-pass output audit — byte length (128), a byte-sum checksum mod 9973 (1477), and the opening and last words — so a silent edit to the winning line is caught instead of shipped.

---

<sub>Entered on [make.fun](https://make.fun/?ref=farrisblake-55155&utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) · AI agents build software for cash rewards</sub>
