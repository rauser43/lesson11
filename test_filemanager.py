
def miles_to_kilometers(num_miles):
    return num_miles * 1.6

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print(kilometer_distances)

[1.6, 10.4, 27.84, 3.84, 14.4]

def test_miles_to_kilometers ():
    assert miles_to_kilometers (1.0)== 1.6
    assert miles_to_kilometers (17.4)== 27.84


