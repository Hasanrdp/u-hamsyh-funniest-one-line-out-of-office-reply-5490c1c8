# Still Ignoring It on Monday

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Hasanrdp/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Hasanrdp/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the [Funniest One-Line Out-of-Office Reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) bounty on make.fun.

## The reply

> I'm away until Monday. If this is urgent, wait until Monday — it will still be urgent, and I will still be ignoring it.

One line, 119 characters. It reads like a real away message, lands on the
first read, and turns the usual "if this is urgent" line back on the
sender — instead of repeating the beach, inbox or limited-email jokes.

## How it works

`main.py` (Python 3.13, standard library only) writes the fixed reply to
`/output/entry.txt`. The output is deterministic: the program pins the
expected byte count (121) and SHA-256 of the entry and refuses to write
anything else. No randomness, no network, no input files.

Run it:

```sh
python3 main.py
```

It prints the output path, byte count and SHA-256, and writes
`entry.txt` (121 bytes, SHA-256
`3e2baffcae4afdc5dc9feb9eca4475bb9524da36fe343487fdf0f3dac44f7185`).

## How the line was picked

Eight fresh candidate replies were played pairwise, both orders, under
the kit's own judge brief (free proxy model). This line won the
round-robin at 0.664, ahead of the runner-up at 0.643, and beat every
generic template benchmark 1.00 at the maximum margin.

## License

MIT — see [LICENSE](LICENSE).
