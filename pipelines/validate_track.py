"""Validate shape and key scientific invariants; this does not verify NASA provenance."""
import argparse
import json
import math
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker


def validate(track):
    schema = json.loads((Path(__file__).resolve().parents[1] / 'contracts/track.schema.json').read_text())
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(track)
    seen = set()
    previous = {}
    for record in track['records']:
        key = (record['place_id'], record['timestamp_utc'])
        if key in seen:
            raise ValueError(f'Duplicate place/time: {key}')
        seen.add(key)
        from datetime import datetime
        moment = datetime.fromisoformat(record['timestamp_utc'].replace('Z', '+00:00'))
        if record['place_id'] in previous and moment <= previous[record['place_id']]:
            raise ValueError('Records must increase chronologically per place')
        previous[record['place_id']] = moment
        for field in ('value', 'reference', 'departure'):
            number = record.get(field)
            if number is not None and not math.isfinite(number):
                raise ValueError(f'Non-finite {field}')
        if record['status'] == 'missing':
            if any(record.get(k) is not None for k in ('value', 'reference', 'departure')):
                raise ValueError('Missing records must have null measurements')
            continue
        if record['value'] is None or record['valid_fraction'] <= 0:
            raise ValueError('Valid record needs a value and positive coverage')
        if track['kind'] == 'rainfall' and record['value'] < 0:
            raise ValueError('Rainfall must be nonnegative')
        if track['kind'] == 'sst_anomaly':
            if record['reference'] is None or record['departure'] is None:
                raise ValueError('Valid ocean record needs reference and departure')
            if not math.isclose(record['value'] - record['reference'], record['departure'], abs_tol=1e-6):
                raise ValueError('Observation minus reference must equal departure')
        if track['source_status'] == 'verified' and record['frame_id'] is None:
            raise ValueError('Verified records require a frame relationship')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('track', type=Path)
    args = parser.parse_args()
    validate(json.loads(args.track.read_text()))
    print('Contract checks passed. Source verification still requires human review.')
