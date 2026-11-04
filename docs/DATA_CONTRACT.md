# Track contract v1

Shape: contracts/track.schema.json. Check with python pipelines/validate_track.py track.json. Passing verifies structure/invariants, not NASA provenance.

Rain kind: value = estimated daily rainfall in mm/day. This v1 accepts daily only; finer sampling needs an explicit contract change. Ocean kind: value = absolute SST in degC, reference = matched baseline SST in degC, departure = value-reference (degC difference). Baseline identifies method/period. All paired values use identical valid cells/weights.

Records: place_id, timezone-aware timestamp_utc, value, valid_fraction, status, frame_id. Unique place/time; chronological per place. Missing records use null measurements. Synthetic tracks are development-only and excluded from production catalog. Verified status requires actual source review; validator cannot prove it.

C supplies companion regions.json (IDs, names, boundaries, masks/area weights), frames.json (IDs, paths, source/time, projection/bounds, exact/derived/context relation), provenance.json (citations, granules, retrieval/checksums, transformations and limitations). Mapping config specifies a fixed range/transform/threshold for the track, not per-region normalization.

A/B use stable IDs; C provides one sample with expected interpretation/answer key before expanding coverage. Incompatible contract changes require all three members' agreement and a version change.
