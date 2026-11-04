# Ten-day parallel development plan

## Goal and scheduling

Ship a reliable rainfall experience first, with a gated Ocean Duet track and mobile-responsive web. Target installable PWA support after the core works. Native mobile stores, forecasting, AI music, hardware and live ingestion are outside this sprint.

The ten days are relative work blocks, NOT ten authorized pre-event coding days. Confirm global/local preparation rules and Karachi pitch/submission timing before assigning calendar dates. Use early days for permitted research/tool practice/logistics; actual competition implementation belongs in its allowed window. This initial repo is a foundation, not a completed solution.

Assume three focused hours per member per work day (90 person-hours across ten days), plus breaks/coordination. This assumption needs team agreement; learning and source-access problems can increase it. Resource IDs below resolve to links/access cautions in RESOURCES.md.

## Parallel schedule

| Day / phase | A: interface and mobile | B: audio and state | C: data and science | End-of-day checkpoint |
|---|---|---|---|---|
| 1 Decisions/access | Run scaffold; sketch welcome, legend, player/evidence and keyboard route (R10-11). | Define audio API, scale proposal, context lifecycle and cancellation using labeled fixtures (R8-9). | One IMERG sample, units/mask/date and frame relationship; inspect current rules (R1-7). | Freeze v1 contract and ownership. Source status remains pending until proven. |
| 2 Independent modules | Region/date controls, values table, errors/loading against contract. | Pure rainfall mapping, missing/dry cues and scheduler. | Subset two regions; means, frames/provenance; validate (R17). | C hands over one real record plus expected interpretation. A/B correct assumptions now. |
| 3 First real slice | Wire selected date/location to real visual, names/focus. | Connect play/pause/stop/seek; same record/clock; rapid-click checks. | Verify ten values and displayed date/frame relation. | One end-to-end real flow. Stop adding features if this fails. |
| 4 Complete rainfall | Responsive timeline, descriptions and evidence; keyboard core. | Sequence/speed and shared-scale two-region A/B. | Common dates and second region, explicit missing values; check historical coverage. | Legend + two-region real playback work. Do not assume full 2022 archive. |
| 5 Distinctive experience | Nine-cell controls and one discovery/reveal. | Sequential scan, row cue, fixed-date spatial vs fixed-place temporal modes. | Grid boundaries, answer key and comparable records. | Rain gate: source/science clear, image/value/tone aligned, accessible core. |
| 6 Extension gate | Actual phone layout; review accessibility; design track/mode labels (R11-12). | Generalize engine per kind; ocean mappings with synthetic fixtures only. | IF rain gate passed: one ocean observation/anomaly, baseline and EIC source check (R13-16). | Written ocean GO/NO-GO. Failed rain gate means repair rain instead. |
| 7 Optional ocean | IF GO, ocean controls; otherwise improve rainfall flow. | IF GO, ocean A/B/difference; overlap only after interpretation works. | IF GO, one region short real sequence/arithmetic; otherwise improve rain provenance. | No public ready status without real verified ocean assets. Rain stays releasable. |
| 8 PWA/evaluation | Manifest/icons/cache versioning; actual install/reload; keyboard/NVDA/zoom. | Phone audio start/resume/interruption/stop and description overlap tests. | Review science/answer keys; help facilitate consent-based sessions. | Aim 3-5 adults incl. blind/low-vision input if available. Record actual results. |
| 9 Stabilize/freeze | Fix blockers; cache update/reset; narrow screens and zoom. | Fix confusing cues/duplicate scheduling; measure demo responsiveness. | Freeze data/manifest and credit/license register. | Feature freeze; disconnected local demo and intentional PWA cache test. Record exact commit. |
| 10 Release/submission | Deploy tested static build to agreed HTTPS host; verify mobile and asset base paths. | Rehearse, verify output hardware and backup recording/local fallback. | Source/mapping explanation, actual study findings, limitations and form evidence. | All check current deadline/form/AI disclosure; submit with time to correct. |

## Resource sequence and parallelism

A starts R10-11 on Day 1; PWA R12 on Day 6. B starts R8-9 Day 1 and receives C's first actual record by Day 2. C starts R1-7 Day 1 and R17 for processing; R13-16 ocean only after rain gate. A and B do not block on all data: use the agreed schema with fixtures visibly labeled synthetic. Replace fixtures with C's verified handoff before production.

M0 agreement -> M1 source proof in parallel with M3 UI/M4 audio -> M2 validated dataset -> M5 integration -> M6 scan/comparison -> M7 evidence -> rain gate -> optional M8 ocean -> M9 tested PWA -> M10 release. Styling can progress independently, but offline acceptance requires real packaged assets.

## Scope cuts and fallback

If Day 3 fails, stop new features and integrate. If Day 5 rain gate fails, spend Days 6-7 on rain and defer ocean. If ocean baseline/imagery gate fails, remove it from release or label it planned. If PWA install/offline is unreliable, ship responsive mobile web and tested local-server backup without claiming offline capability. Cut overlap, extra regions, long timelines, Urdu speech and export before scientific evidence or keyboard access.

## Integration routine

Each morning agree inputs and dependencies. Each midday merge one small complete change. Each evening lint/build main and demonstrate it together. One teammate reviews each PR. Contract changes need all three; no force-push to main. Preserve tested source and data IDs for the final recording.

## Definition of complete

Verified rainfall source/visual relationship; correct units/values; understandable legend; stable playback and two-region comparison; accessible evidence; actual mobile-browser operation; reproducible local demo and credits. Scan/discovery strengthen the target. Ocean has its own gate and arithmetic checks. A native app, warning system or full live-data platform is not implied.
