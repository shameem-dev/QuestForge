# QuestForge

QuestForge is a turn-based RPG battle engine. Heroes and monsters take turns
attacking, using items, and casting skills until one side wins. I'm building it
level by level to learn object-oriented programming and design patterns.

## Project structure

- `domain/`   game rules (characters, combat), no printing or file I/O in the long run
- `patterns/` reusable design-pattern code
- `infra/`    saving, command-line interface, adapters
- `tests/`    tests
- `play.py`   entry point

## How to run

    python play.py
