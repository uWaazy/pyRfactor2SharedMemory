import pytest
from lmu_rpc import get_car_asset_and_name


@pytest.mark.parametrize("vehicle_name,veh_filename,expected", [
    ('Mercedes-AMG GT3', None, ('car_mercedes_amg_gt3', 'Mercedes-AMG LMGT3')),
    ('Proton Competition Mercedes-AMG GT3', None, ('car_mercedes_amg_gt3', 'Mercedes-AMG LMGT3')),
    ('Proton Competition Porsche 963', None, ('car_porsche_963', 'Porsche 963')),
    ('Iron Lynx Lamborghini SC63', None, ('car_lamborghini_sc63', 'Lamborghini SC63')),
    ('Iron Lynx Mercedes-AMG GT3', None, ('car_mercedes_amg_gt3', 'Mercedes-AMG LMGT3')),
    ('DKR Engineering Duqueine D09 LMP3', None, ('car_duqueine_d09', 'Duqueine D09 LMP3')),
    ('Genesis GMR-001 Hypercar', None, ('car_genesis_gmr001', 'Genesis GMR-001 Hypercar')),
    ('Some team', 'vehicles\\duqueine_d09_lmp3\\whatever', ('car_duqueine_d09', 'Duqueine D09 LMP3')),
])
def test_get_car_asset_and_name_precise_matching(vehicle_name, veh_filename, expected):
    assert get_car_asset_and_name(vehicle_name, veh_filename, "") == expected
