from hardware.opentrons.containers import *


mock_labware_info_well = {
    "location": 3,
    "max_volume": 1000,
    "labware_id": "test",
    "labware_name": "Mock labware",
    "well_diameter": 18,
    "depth": 10.9,
}

mock_labware_info_ft15 = {
    "location": 1,
    "max_volume": 15000,
    "labware_id": "test_2",
    "labware_name": "Mock labware ft",
    "well_diameter": 25,
    "depth": 117,
}


well = PlateWell(
    labware_info=mock_labware_info_well,
    well="A1",
)

ft15_water = FalconTube15(
    labware_info=mock_labware_info_ft15,
    well="A1",
    initial_volume_mL=10,
    solution_name="water",
    concentration="pure",
)

ft15_sds = FalconTube15(
    labware_info=mock_labware_info_ft15,
    well="A1",
    initial_volume_mL=10,
    solution_name="sds",
    concentration=10,
)

# ft15_sds.aspirate(100)

print(well.dispense(100, source=ft15_sds))
print(well.dispense(100, source=ft15_water))
print(well)
