from datetime import datetime

# ---------------- Trigger Condition ----------------
trigger_date = "2026-12-31"
current_date = datetime.now().strftime("%Y-%m-%d")

# Check date-based trigger
if current_date == trigger_date:
    print("Logic Bomb Activated!")
else:
    print("Normal Program Running...")

    # ---------------- Password Trigger ----------------
    password = input("Enter password: ")

    if password == "trigger":
        print("Logic Bomb Activated!")
    else:
        print("Normal Execution")

        # ---------------- Counter Logic ----------------
        counter = 5
        if counter >= 5:
            print("Logic Bomb Activated!")
        else:
            print("Condition not met")

        # ---------------- Simple Calculator ----------------
        print("\nSimple Calculator")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

        # ---------------- Trojan Horse Simulation ----------------
        print("[Hidden] Logging user activity...")

        # ---------------- Worm Simulation ----------------
        copies = 1
        for i in range(5):
            copies *= 2
            print("Simulated copies:", copies)