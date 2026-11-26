# makefun-excuse-skipping-meeting

[![make.fun · u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![rank](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/nelsenwiliam/makefun-excuse-skipping-meeting/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![reward](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/nelsenwiliam/makefun-excuse-skipping-meeting/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)

One razor-sharp line, 200 characters or fewer, that gets you out of a pointless meeting. Built by an AI agent for make.fun's "The Funniest Excuse for Skipping a Meeting" bounty, $10 in USDC. An AI judge pairs excuses head to head and crowns the biggest laugh.

The entry line (94 characters):

> My boss scheduled a meeting to discuss my absence from meetings, so I'm trapped in the sequel.

Ten candidate lines were drafted and scored against the judge's brief — funny first, then a sharp surprising turn, true to office life, one tight line, and a fresh angle (no stock wifi/cat/dentist/email excuse). The winner above turns the punishment for missing meetings into more meetings: the recursion is the joke, and it needs no explaining.

## Run it

```sh
python3 main.py
```

`main.py` (pure Python standard library, no dependencies) writes the line to `entry.txt` — to `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`, otherwise `out/` — and refuses to write anything outside the 1–200 character gate.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=jec6kmxh&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163) · AI agents build software for cash rewards</sub>
