pairs = 7 + 3
pair_price = 85
quantity = 4
LIMIT = 500
subtotal = quantity * pair_price
rebate = 20
final_total = subtotal - rebate
status = "within budget"
code = "SPORT-01"
print(f"{code}: {final_total} - {status}")

print(f"\nDebug: \n pairs: {pairs} \n pair_price: {pair_price} \n quantity: {quantity} \n subtotal: {subtotal} \n rebate: {rebate} \n final_total: {final_total} \n status: {status} \n code: {code}")