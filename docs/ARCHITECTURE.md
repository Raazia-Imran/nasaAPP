# Architecture and scope

Use React + TypeScript + Vite for responsive web; Web Audio/Tone.js for sound; Python/xarray/NumPy for scientific preparation. A full JavaScript backend is unnecessary. Browser audio needs browser JavaScript, while Python handles NetCDF/grids. A runtime API/database is deferred until actual live querying needs it.

Deliver one responsive app for desktop/mobile browsers, then a PWA manifest/icons/versioned cache where supported. This is not native Android/iOS packaging or guaranteed background audio. Test install/offline on real mobile hardware. Keep a local HTTP server backup; do not depend on file:// or fresh authentication at the venue.

Rainfall is primary. Ocean Duet is a gated second track sharing catalog, location/date controls, playback, legends, evidence and accessibility. Units, legends and scales remain separate. Do not blend rainfall and ocean into a claimed causal model.

Pipeline -> validated JSON/frame manifest -> catalog -> one PlayerState -> AudioEngine + synchronized visual/evidence.

State: trackId, placeId, recordIndex, mode, speed, playbackStatus. Switching tracks stops old audio and resets mode/range. Rain modes: timeline/A-B, then scan. Ocean: reference/observation/difference; simultaneous duet is optional. One clock and selected record determine both audio and screen. Stop/seek/mode changes cancel old events. Start only after user action; pause for descriptions. No fake values or unrelated music on missing data.

Modules: catalog, legend, accessible named region selection, timeline, comparison, optional grid, evidence, discovery, mobile layout and offline state. Maps are supplementary controls; use a values table as an alternative to sound. No accounts, geolocation permission or server secrets required.

Prepare small static JSON and reduced-size credited visuals. Cache a tested version, provide reset/update behavior and avoid raw bulk downloads. No host selected or deployment made in the scaffold.

Core incremental software/data/local-demo cost can be PKR 0 using existing equipment. Optional team caps: connectivity 1,500; participant transport/thanks 5,000; contingency 1,500 PKR. These are planning allowances, not quotes. New equipment, event travel/meals and paid hosting excluded.
