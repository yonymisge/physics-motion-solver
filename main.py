# Physics SUVAT Solver for Grade 12 Motion Units
# Built by a Software Engineering Aspirant from Ethiopia

print("=" * 50)
print("🛠️ UNIFORMLY ACCELERATED MOTION SOLVER 🛠️")
print("=" * 50)
print("Leave the unknown variable blank (press Enter) to solve for it.\n")

# Step 1: Collect inputs from the user
u_input = input("Enter Initial Velocity (u) in m/s: ")
a_input = input("Enter Acceleration (a) in m/s²: ")
t_input = input("Enter Time (t) in seconds: ")
v_input = input("Enter Final Velocity (v) in m/s: ")

# Step 2: Solve for Final Velocity (v = u + at)
if v_input == "":
    u = float(u_input)
    a = float(a_input)
    t = float(t_input)
    v = u + (a * t)
    print(f"\n✅ Calculated Final Velocity (v) = {v} m/s")

# Step 3: Solve for Acceleration (a = (v - u) / t)
elif a_input == "":
    u = float(u_input)
    v = float(v_input)
    t = float(t_input)
    a = (v - u) / t
    print(f"\n✅ Calculated Acceleration (a) = {a} m/s²")

# Step 4: Solve for Time (t = (v - u) / a)
elif t_input == "":
    u = float(u_input)
    v = float(v_input)
    a = float(a_input)
    t = (v - u) / a
    print(f"\n✅ Calculated Time (t) = {t} seconds")
