"""The 4AM Commit: Funniest Agent Bug-Fix Message.

This entry is a single one-line commit message written in the voice of
an AI agent at the end of a long night spent fixing its own bugs.

The joke is the self-repair loop itself: the agent traces the crash,
discovers the author of the bug was an earlier version of itself,
patches that self, and then adds a test whose only job is to stop a
future version of itself from reintroducing the same self as a bug.
It exits before it can approve its own fix, because at 4AM the
reviewer, the author and the suspect are all the same process — and
none of them should be trusted to sign off on the others.
"""

import os

TEXT = "fix: it was me — I was the bug. Patched myself at 4am, added a test to stop me reintroducing me, and exited before I could approve my own fix"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
