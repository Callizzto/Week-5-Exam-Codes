score = 68
attendance = 83
minimum_score = 75
minimum_attendance = 80
passed = score >= minimum_score
attended = attendance >= minimum_attendance
ready = passed and attended
warning = (score < minimum_score) or (attendance < minimum_attendance)
if ready:
    remark = "Review needed"
else:
    remark = "Review (not) needed"
print(f"{remark} | ready={ready} | warning={warning}")

print(f"\nDebug: \n score: {score} \n attendance: {attendance} \n minimum_score: {minimum_score} \n minimum_attendance: {minimum_attendance} \n passed: {passed} \n attended: {attended} \n ready: {ready} \n warning: {warning} \n remark: {remark}")