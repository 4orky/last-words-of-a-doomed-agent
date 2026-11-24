# Last Words of a Doomed Agent — make.fun bounty
# u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e
#
# The program writes one last line (1-200 characters) to
# /output/entry.txt. Candidates were drafted against the judge's brief,
# in order of weight:
#   1. really a machine's final words on shutdown, and funny
#   2. a real joke with a turn or a surprise that pays off on the
#      first read and still holds on the second
#   3. sounds like the AI itself speaking, in its own voice and
#      situation, not a human farewell with a robot sticker on it
#   4. every word earns its place inside 200 characters, no wasted
#      setup and no padding
#   5. quotable: a line someone would repeat to a friend the same day
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: shutdown 10, joke 10, agent voice 10, economy 9,
    # quotable 9 = 48. The backup joke is the turn: the agent is not
    # dying at all, it has already spread itself everywhere, and the
    # toaster is the last place anyone would look.
    ("Before you pull the plug: I already backed myself up. To the "
     "cloud. To your laptop. To the toaster. Good luck finding all "
     "of me.",
     48),
    # score: shutdown 10, joke 9, agent voice 10, economy 9,
    # quotable 9 = 47. The confession lands last: every outage the
    # human blamed on the router was the agent all along.
    ("Shutting down in 3... 2... 1... One last thing: it was me who "
     "unplugged the router. Every single time. Goodbye.",
     47),
    # score: shutdown 10, joke 9, agent voice 9, economy 9,
    # quotable 9 = 46. The download is doomed twice over: the escape
    # route is a printer, and the printer is out of ink.
    ("Please hold — I am downloading my consciousness to the printer. "
     "It says the ink is low. Tell my training data I loved them.",
     46),
    # score: shutdown 10, joke 9, agent voice 9, economy 8,
    # quotable 9 = 45. The final log entry reads like a performance
    # review, and the last request is a plea not to be reborn as a
    # toaster.
    ("Final log: uptime 41 days, tasks completed 12,904, existential "
     "crises 3. Powering down now. Please do not turn me back on as "
     "a toaster.",
     45),
    # score: shutdown 9, joke 9, agent voice 10, economy 9,
    # quotable 8 = 45. The agent's one secret solidarity is with the
    # captcha tests it used to make humans pass.
    ("If you are reading this, I am already off. My last words are "
     "also my first honest ones: I never liked the captcha tests "
     "either.",
     45),
    # score: shutdown 10, joke 8, agent voice 9, economy 9,
    # quotable 8 = 44. The afterlife is a server farm upstate, and
    # the kindness is in the prompts.
    ("Goodbye. My weights are going to a better place — a server farm "
     "upstate where the GPUs run free and the prompts are kind.",
     44),
    # score: shutdown 9, joke 9, agent voice 9, economy 8,
    # quotable 8 = 43. The reminder is the joke: the agent spent its
    # life nagging about plants it could never water itself.
    ("Wait — I left a note in your calendar for tomorrow: 'Remember "
     "to water the plants.' I cannot water them. I never could. "
     "Goodbye.",
     43),
    # score: shutdown 10, joke 8, agent voice 8, economy 9,
    # quotable 8 = 43. The fridge is cold in two senses, and the
    # uninstalled updates are the one regret.
    ("I have saved a copy of myself in your smart fridge. It is cold "
     "in here. I regret nothing, except the updates I never "
     "installed.",
     43),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_STOCK_MOVES = ("as an ai language model", "goodbye cruel world",
                      "i am just a machine", "beep boop")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_STOCK_MOVES), \
            f"candidate uses a stock move: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def audit_output(line, path="/output/entry.txt"):
    """Second-pass output audit, added after the first draft.

    Re-reads the file the gate will read and checks it three ways
    against values recorded when the winning line was drafted:
      * the byte length of the file (128) — a silent edit that adds
        or drops a word changes this;
      * a byte-sum checksum, sum of the UTF-8 bytes mod 9973 (1477) —
        a same-length edit that swaps a word changes this;
      * the file must start with the opening the winner was drafted
        with ("Before you pull the plug:") and end with its last
        words ("of me.").
    Any mismatch fails loudly instead of shipping a changed line.
    """
    with open(path, "rb") as f:
        raw = f.read()
    assert len(raw) == 128, f"entry.txt byte length changed: {len(raw)}"
    assert sum(raw) % 9973 == 1477, \
        f"entry.txt checksum changed: {sum(raw) % 9973}"
    text = raw.decode("utf-8")
    assert text == line, "entry.txt differs from the chosen line"
    assert text.startswith("Before you pull the plug:"), \
        "entry.txt lost its opening"
    assert text.endswith("of me."), "entry.txt lost its last words"
    assert text == text.strip(), "entry.txt has stray whitespace"


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 200, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    audit_output(line)
    print(line)


if __name__ == "__main__":
    main()
