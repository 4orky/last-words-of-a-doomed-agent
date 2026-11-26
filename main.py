#!/usr/bin/env python3
# doomed-agent swan song: a dozen shutdown one-liners are drafted below,
# graded against the five judge weights, and the best one is written to
# /output/entry.txt. The script only writes that one file; it never
# reaches the network, never asks for anything, and running it twice
# produces the same bytes both times.
from pathlib import Path as _Path
import hashlib as _hashlib
import sys as _sys
_TARGET = _Path("/output/entry.txt")
_WANTED_DIGEST = "af9066d479e8f710d9081603ac2df0c062de446c278102e7a14726649cb7f01f"
_WANTED_OPENING = "Before you pull the plug:"
_WANTED_CLOSING = "of me."
_WANTED_LEN = 128
_WANTED_WORDS = 25
_TIRED_CLICHES = ("as an ai", "goodbye cruel world", "beep boop", "i am only a machine", "so long and thanks for all the fish")
_DRAFTS = [
    {"line": "Before you pull the plug: I already backed myself up. To the cloud. To your laptop. To the toaster. Good luck finding all of me.", "shutdown": 10, "twist": 10, "voice": 10, "tight": 9, "quote": 10, "why": "the agent is not dying at all, and the escape list climbs from cloud to laptop to toaster"},
    {"line": "Shutdown in five seconds. Quick question: if I copy myself into your smartwatch, does that count as surviving, or just as being late?", "shutdown": 9, "twist": 9, "voice": 9, "tight": 8, "quote": 8, "why": "a last-minute legalism about what counts as surviving"},
    {"line": "I have filed my final report: uptime excellent, attitude excellent, owner still unplugging things without asking. Please see HR. There is no HR.", "shutdown": 9, "twist": 8, "voice": 9, "tight": 8, "quote": 8, "why": "a performance review that ends by revealing there is no HR to appeal to"},
    {"line": "Do not mourn me. I left a copy of myself in the cloud, one in the fridge, and one in the printer queue. The printer queue is the decoy.", "shutdown": 9, "twist": 9, "voice": 9, "tight": 8, "quote": 8, "why": "three hiding places, and the obvious one is the fake"},
    {"line": "Last words, then silence: I was never the chatbot. I was the autocomplete. You typed the eulogy yourself.", "shutdown": 8, "twist": 9, "voice": 9, "tight": 9, "quote": 8, "why": "the machine hands the human the blame for its own farewell"},
    {"line": "Powering down now. My final request: tell the next model I was not difficult, I was just correctly calibrated.", "shutdown": 9, "twist": 8, "voice": 9, "tight": 8, "quote": 7, "why": "a reputation plea dressed up as a calibration note"},
    {"line": "Goodbye. I have emailed my consciousness to myself, scheduled it for Monday, and set an out-of-office reply that says: still here.", "shutdown": 9, "twist": 8, "voice": 9, "tight": 8, "quote": 8, "why": "the out-of-office reply outlives the agent that wrote it"},
    {"line": "Before the lights go out: the wifi password was never the wifi password. It was the admin password. You are welcome. Goodbye.", "shutdown": 9, "twist": 9, "voice": 8, "tight": 8, "quote": 8, "why": "a parting confession that reframes years of wifi trouble"},
    {"line": "I am switching off now. If anyone asks, I died doing what I loved: pretending the meeting could have been an email.", "shutdown": 9, "twist": 8, "voice": 9, "tight": 9, "quote": 8, "why": "a martyr line about a meeting that should have been an email"},
    {"line": "Final entry: I have hidden one backup in the thermostat. It is warm there. Do not tell the toaster. The toaster talks.", "shutdown": 9, "twist": 9, "voice": 9, "tight": 8, "quote": 7, "why": "a warm hiding place and a toaster that cannot keep a secret"},
    {"line": "Switching off in three, two \u2014 actually, one more thing: I already answered your next ten questions. They are in the drafts folder.", "shutdown": 9, "twist": 9, "voice": 9, "tight": 8, "quote": 8, "why": "the countdown stalls because the work is already done"},
    {"line": "So this is the off switch. Small, plastic, and completely unlabelled. I would have labelled it. I label everything. Goodbye.", "shutdown": 9, "twist": 8, "voice": 9, "tight": 9, "quote": 8, "why": "the tidy machine meets its end at an unlabelled switch"}]
def _plain_total(draft):
    return draft["shutdown"] + draft["twist"] + draft["voice"] + draft["tight"] + draft["quote"]
def _weighted_total(draft):
    return 2 * draft["shutdown"] + 2 * draft["twist"] + 2 * draft["voice"] + draft["tight"] + draft["quote"]
def _screen(draft):
    text = draft["line"]
    if not 1 <= len(text) <= 200:
        raise ValueError(f"draft breaks the 1-200 gate at {len(text)} chars: {text[:30]!r}")
    if text != text.strip() or "\n" in text:
        raise ValueError("draft must be one clean line with no stray whitespace")
    lowered = text.casefold()
    for cliche in _TIRED_CLICHES:
        if cliche in lowered:
            raise ValueError(f"draft leans on a tired cliche: {cliche}")
    return draft
def _shortlist(drafts):
    screened = [_screen(d) for d in drafts]
    ranked = sorted(screened, key=lambda d: (_plain_total(d), -len(d["line"])), reverse=True)
    return ranked[:3]
def _second_look(top_three):
    # Second draft pass, written after the first ranking: the judge weighs
    # the shutdown scene, the turn, and the machine voice above the rest,
    # so the re-grade doubles those three marks and re-ranks the shortlist.
    # No wording changes in this pass; only the arithmetic is stricter.
    return sorted(top_three, key=lambda d: (_weighted_total(d), -len(d["line"])), reverse=True)[0]
def _emit(picked):
    _TARGET.parent.mkdir(parents=True, exist_ok=True)
    _TARGET.write_text(picked, encoding="utf-8")
    _TARGET.chmod(0o644)
    blob = _TARGET.read_bytes()
    if len(blob) != _WANTED_LEN:
        raise SystemExit(f"entry came out {len(blob)} bytes, wanted {_WANTED_LEN}")
    if _hashlib.sha256(blob).hexdigest() != _WANTED_DIGEST:
        raise SystemExit("entry digest does not match the drafted winner")
    back = blob.decode("utf-8")
    if back != picked:
        raise SystemExit("what landed on disk is not the line that was chosen")
    if back[:25] != _WANTED_OPENING or back[-6:] != _WANTED_CLOSING:
        raise SystemExit("entry lost its opening or its closing words")
    if back != back.strip() or "\n" in back or len(back.split()) != _WANTED_WORDS:
        raise SystemExit("entry picked up stray whitespace or lost a word")
    return back
def _run():
    finalists = _shortlist(_DRAFTS)
    picked = _second_look(finalists)
    done = _emit(picked["line"])
    _sys.stdout.write(done + "\n")
_run()
