# TBC → Voroa migration

This project keeps the exported TBC command code in `tbc_export.json` and
runs it through a compatibility layer instead of rewriting every command.

## Voroa

Build command:
    pip install -r requirements.txt

Start command:
    python main.py

Required environment variable:
    BOT_TOKEN=<your BotFather token>

Optional:
    SECOND_BOT_TOKEN=<only if your old bot used a second bot>

## Important

The original TBC export contained credentials. They were removed from the
runnable export generated here. Never commit BOT_TOKEN or SECOND_BOT_TOKEN
to GitHub.

This is a migration framework, not a claim that every TBC-only service has
identical semantics outside TBC. Test payment gateways, ads, scheduled jobs,
broadcasts and verification flows before production.
