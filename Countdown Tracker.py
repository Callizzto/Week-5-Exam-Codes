n = 20
limit = 5
step = -3
total = 0
count = 0
while n >= limit:
    total += n
    count += 1
    n += step
bonus = 2
final_total = total + bonus
print(f"count={count} | total={total} | bonus={bonus} | final_total={final_total}")

print(f"\nDebug: \n n: {n} \n limit: {limit} \n step: {step} \n total: {total} \n count: {count} \n bonus: {bonus} \n final_total: {final_total}")