import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('validator', Path(__file__).resolve().parents[1] / 'pipelines/validate_track.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.track = {'schema_version': '1.0', 'id': 'fixture', 'kind': 'rainfall', 'title': 'Synthetic test only', 'unit': 'mm/day', 'source_status': 'synthetic', 'sources': ['synthetic fixture, not NASA'], 'records': [{'place_id': 'A', 'timestamp_utc': '2022-06-01T00:00:00Z', 'value': 0, 'valid_fraction': 1, 'status': 'valid', 'frame_id': None}]}

    def test_zero_is_valid_not_missing(self):
        module.validate(self.track)

    def test_missing_value_must_be_null(self):
        self.track['records'][0]['status'] = 'missing'
        with self.assertRaises(ValueError): module.validate(self.track)

    def test_duplicate_rejected(self):
        self.track['records'].append(copy.deepcopy(self.track['records'][0]))
        with self.assertRaises(ValueError): module.validate(self.track)

    def test_ocean_arithmetic(self):
        self.track.update(kind='sst_anomaly', unit='degC', baseline='synthetic test')
        self.track['records'][0].update(value=28, reference=27, departure=1)
        module.validate(self.track)
        self.track['records'][0]['departure'] = -1
        with self.assertRaises(ValueError): module.validate(self.track)

    def test_verified_requires_frame(self):
        self.track['source_status'] = 'verified'
        with self.assertRaises(ValueError): module.validate(self.track)

if __name__ == '__main__': unittest.main()
