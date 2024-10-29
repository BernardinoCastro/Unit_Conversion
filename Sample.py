print(
"""UNITS you can choose from
1) Kg to Lbs
2) Lbs to Kg
3) Miles to Km
4) Km to Miles  """
)

conversion_unit = int(input("Enter a conversion you want to execute: "))
value = float(input("Enter the number you want to convert: "))


if conversion_unit == 1 :
    pound = value * 2.205
    print(f"Kg: {value} is {pound:.2f} Lbs")
if conversion_unit == 2 :
    kg = value * 0.452592
    print(f"Kg: {kg:.2f}")
if conversion_unit == 3 :
    km = value * 1.609
    print(f"Km: {km:.2f}")
if conversion_unit == 4 :
    miles = value / 1.609
    print(f"Miles: {miles:.2f}")
