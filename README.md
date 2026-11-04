# Monsoon Listener

NASA Earth Information Jukebox project foundation for three NED software engineering students.

**Status: initial scaffold and implementation plan. No verified NASA track, sound player, PWA caching or production deployment is implemented yet.**

Rainfall is the required first release. Ocean temperature/anomaly is a gated second track using the same interface and audio engine. A responsive web application is the first delivery platform; installable PWA capability follows after browser playback works. Native Android/iOS apps are outside the ten-day scope.

## Start here

1. Read [the ten-day plan](docs/10_DAY_PLAN.md).
2. Agree ownership in [modules and handoffs](docs/MODULES.md).
3. Freeze [the data contract](docs/DATA_CONTRACT.md) before parallel implementation.
4. Use [resources and source gates](docs/RESOURCES.md) before claiming NASA alignment.
5. Follow [contribution instructions](CONTRIBUTING.md).

## Run the scaffold

Use Node 24 LTS and npm (see `.nvmrc`). From the repository root:

```sh
npm ci
npm run dev
npm run lint
npm run build
npm run preview
```

Python 3.11+ is recommended for data preparation, in a separate environment:

```sh
python -m venv .venv
python -m pip install -r pipelines/requirements.txt
python pipelines/validate_track.py path/to/track.json
```

Activate `.venv` before installing: Windows PowerShell `.venv\Scripts\Activate.ps1`; macOS/Linux `source .venv/bin/activate`. Never put Earthdata credentials in the frontend.

## Structure

| Path | Owner / purpose |
|---|---|
| `apps/web/src/features/` | A: interface, accessibility, track selection |
| `apps/web/src/audio/` | B: mapping and playback engine |
| `apps/web/src/state/` | B with A: single player state |
| `pipelines/`, `data/` | C: NASA acquisition and preparation |
| `contracts/` | All: shared record shape and validation |
| `docs/` | Plan, resources, acceptance and handoffs |

## Rules and claims

The ten days are a relative work sequence. Check the event's permitted preparation/build window and Karachi deadlines before scheduling competition work. Do not present synthetic development fixtures as NASA data. Source downloads, baseline relationships and EIC frame alignment need actual validation.

This project is independent and does not imply NASA endorsement. Original code is MIT licensed; source imagery, datasets and dependencies retain their own attribution and license conditions.
