# Module ownership and handoffs

A = interface/accessibility/PWA; B = audio/state; C = data/science. Assign names as a team.

| Module | Owner | Inputs | Output / acceptance |
|---|---|---|---|
| M0 agreement | All, A integrates | contract, R18 | frozen IDs/schema, own branches and review |
| M1 source gate | C | R1-7 | real sample + documented visual relationship |
| M2 preparation | C | M1, R17 | masks/means, JSON/manifests, ten checked values |
| M3 interface | A | contract, R10-11 | responsive catalog/legend/controls/evidence; keyboard complete |
| M4 audio | B | contract, R8-9 | mapping, envelopes, scheduler, stop/pause/seek |
| M5 integration | All | M2-4 | same real record/date/image/audio by Day 3 |
| M6 compare/scan | B behavior, A UI, C grid | real aligned records | fixed-scale A/B and optional sequential 3x3 scan |
| M7 evidence/discovery | A UI, C answers, B cues | source register, values | taught question and inspectable reveal |
| M8 ocean | C source, B mapping, A views | R13-16, stable engine | independent gate + arithmetic before release |
| M9 mobile/PWA | A, B device checks | R12, stable build | tested manifest/cache/update and actual phone playback |
| M10 release | All | acceptance checklist | tested commit/assets, documentation and backup |

C -> A/B: record JSON, stable IDs, units/time, expected interpretation and caveats. B -> A: initialize/play/pause/stop/seek/setMode API plus errors/state. A -> B/C: wired UI and reproducible failures. Every handoff includes branch/commit and checks completed.

Do not wait for finished pipelines: A/B can use clearly labeled synthetic fixtures. No fixture is scientific evidence. A owns feature UI/CSS; B owns audio/state; C owns pipelines/assets. Shared App.tsx/contracts/package changes go through the integrator and small PRs. Update main before starting a branch. One partner reviews each PR. Never force-push main.

Daily: 15-minute agreement on inputs, a midday integration, then 20-minute main-branch demo/check. C proposes science transforms; B checks units/audio; A checks wording. All sign off source claims. No pitch/color is an official danger score.
