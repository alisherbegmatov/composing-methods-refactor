# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    is_well_done = desired_state == 'well-done' and time * \
        temperature * pressure * COOKED_CONSTANT >= WELL_DONE
    is_medium = desired_state == 'medium' and time * \
        temperature * pressure * COOKED_CONSTANT >= MEDIUM
    if is_well_done or is_medium:
        return True
    else:
        return False
