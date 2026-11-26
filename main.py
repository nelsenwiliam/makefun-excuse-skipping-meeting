#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp excuse line (<= 200 chars) to entry.txt.

Candidate lines, judged against the published judge brief
(funny > sharp surprise turn > true to office life > tight > fresh angle,
never a stock excuse about bad wifi, a cat or a dentist):

1. "My calendar invited me to a meeting about meetings, so I'm attending
   the one where we cancel this one."
   - Relatable recursion, but "meeting about meetings" is a well-worn joke.

2. "I'm stuck in a meeting about why I missed the last meeting, and it's
   going exactly how you'd expect."
   - Good recursion, but the second half sags; the turn is predictable.

3. "My boss scheduled a meeting to discuss my absence from meetings, so
   I'm trapped in the sequel."
   - Sharp turn ("trapped in the sequel"), fresh recursion, true to life.

4. "I can't make it - I'm in a meeting right now deciding whether this
   meeting should have been an email."
   - The most relatable line of the set, but "should have been an email"
   is itself a stock punchline, so the freshness score drops.

5. "Sorry, I have a conflicting meeting with myself to recover from all
   these meetings."
   - Gentle, no real surprise turn; reads as a mild smile, not a laugh.

6. "I'm skipping this one to preserve my perfect attendance record at
   meetings that could have been emails."
   - Clever inversion, but "could have been an email" again, and wordy.

7. "My laptop updated, my calendar crashed, and honestly both of them are
   doing a better job of avoiding this meeting than I ever could."
   - Too long, too explain-y; the laugh needs explaining, so it loses.

8. "I'm attending mandatory training on how to decline meetings. It's
   ironic. It's also three hours long."
   - Three sentences, not one tight line; the irony is spelled out.

9. "I told my calendar I was busy, and for once my calendar believed me."
   - Sweet, but the turn is soft and the meeting itself barely appears.

10. "Can't join - I'm busy writing the meeting notes for a meeting I never
    attended, and they're somehow already outdated."
    - Funny premise, but it explains itself twice and runs long.

Winner: candidate 3. It is on-subject (a one-line excuse for skipping a
pointless meeting), lands a sharp surprising turn ("trapped in the sequel"
- the punishment for missing meetings is MORE meetings), feels true to
office life (the boss who manages absence with another meeting), says it
in one tight line with no throat-clearing, and the recursion angle is
fresher than wifi/cat/dentist/email stock jokes. No explanation needed.
"""

import os

# Final line (chosen above). Verified <= 200 chars at runtime by main().
# Length check: len(FINAL_LINE) is asserted in main() before writing.
FINAL_LINE = (
    "My boss scheduled a meeting to discuss my absence from meetings, "
    "so I'm trapped in the sequel."
)

MAX_CHARS = 200


def resolve_output_dir():
    """Pick the first writable output location, in grader order."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append("out")
    for path in candidates:
        try:
            os.makedirs(path, exist_ok=True)
            probe = os.path.join(path, ".write_probe")
            with open(probe, "w", encoding="utf-8") as fh:
                fh.write("ok")
            os.remove(probe)
            return path
        except OSError:
            continue
    raise OSError("no writable output directory among: %s" % candidates)


def main():
    line = FINAL_LINE.strip()
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(
            "final line is %d chars, must be 1-%d" % (len(line), MAX_CHARS)
        )
    if not line.strip():
        raise SystemExit("final line must not be only whitespace")
    out_dir = resolve_output_dir()
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
