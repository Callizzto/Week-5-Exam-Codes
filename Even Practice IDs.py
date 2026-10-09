start = 2
stop = 21
step = 2
values = []
for number in range(start, stop, step):
    values.append(number)
size = len(values)
added = sum(values)
base = 100
answer = base + added
print(f"values={values} | size={size} | answer={answer}")

print(f"\nDebug: \n start: {start} \n stop: {stop} \n step: {step} \n values: {values} \n size: {size} \n added: {added} \n base: {base} \n answer: {answer}")