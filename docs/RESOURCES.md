# Resources and source gates

| ID | Source | Who / when / use |
|---|---|---|
| R1 | https://www.spaceappschallenge.org/2026/challenges/the-earth-information-jukebox/ | Everyone Day 1: objective, resources, current rules; confirm Karachi timing. |
| R2 | https://svs.gsfc.nasa.gov/gallery/daily-visualizations/ | C Day 1: EIC relationship. |
| R3 | https://svs.gsfc.nasa.gov/4285/ | C Days 1-3: precipitation frames; rolling availability does not prove a 2022 archive. |
| R4 | https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDF_07/summary | C Days 1-4: candidate IMERG Final Daily V07 metadata and units. |
| R5 | https://gpm.nasa.gov/data/imerg | C: run/version, science and downloads. |
| R6 | https://gpm.nasa.gov/data/visualization | C: alternative visual routes; compare runs and aggregations. |
| R7 | https://urs.earthdata.nasa.gov/ | C: free account where required; credentials never in browser/Git. |
| R8 | https://github.com/Tonejs/Tone.js | B Days 1-5: synthesis/scheduling; MIT dependency, add during engine work. |
| R9 | https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API | B: audio context, gesture, timing and lifecycle. |
| R10 | https://react.dev/learn and https://vite.dev/guide/ | A/B: component/state/build reference. |
| R11 | https://www.w3.org/WAI/WCAG22/quickref/ and https://www.nvaccess.org/download/ | A/all: keyboard, focus, names, alternatives and NVDA. |
| R12 | https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps | A Days 6-8: install, manifest, cache/update; test actual browsers. |
| R13 | https://podaac.jpl.nasa.gov/dataset/MUR25-JPL-L4-GLOB-v04.2 | C Day 6 ocean gate: SST/anomaly, documented 2003-2014 reference. |
| R14 | https://svs.gsfc.nasa.gov/5176/ | C: ocean frames link MUR v4.1; not automatically equivalent to MUR25 v4.2. |
| R15 | https://podaac.github.io/tutorials/notebooks/datasets/enso_MUR_tutorial_final.html | C: official anomaly tutorial. |
| R16 | https://coastwatch.pfeg.noaa.gov/erddap/griddap/jplMURSST42.html | C: candidate numeric mirror; inspect units/availability. |
| R17 | https://docs.xarray.dev/ and https://numpy.org/doc/ | C: grids, masking and aggregation. |
| R18 | https://docs.github.com/en/pull-requests | Everyone: branch, review and integration. |

Published metadata exists; this scaffold has NOT downloaded or verified a NASA track.

## Rain gate

C obtains one real sample and identifies product/run/version, units, UTC interval, mask and geographic support. Record frame date, projection, bounds and credits. Resolve differences in run, resolution and averaging before claiming exact pairing. 2022 is a candidate, not a guaranteed visual archive. Choose a supported period or review a labeled derived companion with a challenge mentor. NASA data alone does not establish EIC-frame compliance.

## Ocean gate

Only after rain works: obtain one observation/anomaly record, verify baseline, shared mask, units and imagery relation. SVS links a different MUR product from proposed numeric data; do not conceal it. Absolute Kelvin may need conversion; a 1 K anomaly equals a 1 degree C difference and must not have 273.15 subtracted. Derive reference=observation-anomaly only if definitions agree.

## Record with every track

Product/version, source granule, retrieval date/checksum, original units and conversions, UTC interval, boundaries, masks/weights, valid fraction, baseline if any, exact/derived/context frame relationship, source citation, license/use conditions. Synthetic fixtures stay visibly labeled and never become submitted NASA evidence.
