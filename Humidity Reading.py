x = 62
y = 9
low = 40
high = 70
if x >= low:
    if x <= high:
        zone = "inside"
    else:
        zone = "above"
else:
    zone = "below"
match_value = x + y
print(f"zone={zone} | sum={match_value}")

print(f"\nDebug: \n x: {x} \n y: {y} \n low: {low} \n high: {high} \n zone: {zone} \n match_value: {match_value}")