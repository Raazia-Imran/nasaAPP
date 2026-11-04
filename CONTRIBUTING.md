# Working in parallel

Use branches `feat/ui-<task>` (A), `feat/audio-<task>` (B), and `feat/data-<task>` (C). `main` holds integrated work. Each PR should have one purpose, its validation, and a screenshot or sound explanation where relevant.

All members clone once, then create their own branch. Before starting a new task, update main:

```sh
git switch main
git pull --ff-only
git switch -c feat/ui-player
```

Commit and push your branch, then open a PR into main. One other member reviews. Do not force-push main. Never commit credentials, downloaded bulk NASA files, node_modules or a virtual environment.

A owns feature UI/CSS. B owns audio/state. C owns pipelines/track assets. Contract changes require agreement by all three and a version change when incompatible. Shared entry points (App.tsx, package manifests, contracts) need a designated integrator; A integrates UI, B requests audio wiring, C provides validated records.

Before merge: npm ci; npm run lint; npm run build. Data changes also pass the pipeline validator and source arithmetic checks. Integrate one real record by the end of Day 3; do not wait for finished separate subsystems.
