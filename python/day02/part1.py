
from safety_level_checker_harsh import SafetyLevelCheckerHarsh
from safety_level_checker_forgiving import SafetyLevelCheckerForgiving

dummy_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day02-pt01-input-dummy.txt"
real_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day02-pt01-input-real.txt"

safetyLevelCheckerHarsh = SafetyLevelCheckerHarsh()
numSafeHarsh = safetyLevelCheckerHarsh.get_safe_lines_from_file(real_file_path)

safetyLevelCheckerForgiving = SafetyLevelCheckerForgiving()
numSafeForgiving = safetyLevelCheckerForgiving.get_safe_lines_from_file(real_file_path)
print("part1 numsafe:", numSafeHarsh)
print("part2 numsafe:", numSafeForgiving)