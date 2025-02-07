from safety_level_checker_harsh import SafetyLevelCheckerHarsh
from safety_level_checker_forgiving import SafetyLevelCheckerForgiving


if __name__=="__main__":        
    dummy_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day02-pt01-input-dummy.txt"
    real_file_path = f"/Users/johncohen/Documents/Documents/Job_Hunt_2025/SE_Job_Hunt/advent-of-code-2024/data/day02-pt01-input-real.txt"

    safetyLevelCheckerHarsh = SafetyLevelCheckerHarsh()
    listSafeHarsh = safetyLevelCheckerHarsh.get_safe_lines_from_file(real_file_path)

    safetyLevelCheckerForgiving = SafetyLevelCheckerForgiving()
    listSafeForgiving = safetyLevelCheckerForgiving.get_safe_lines_from_file(real_file_path)
    
    safeVnotSafeDifference = [item for item in listSafeForgiving if tuple(item) not in map(tuple, listSafeHarsh)]

    difference_file_path = "difference.txt"
    with open(difference_file_path, 'w') as file:
        for item in safeVnotSafeDifference:
            file.write(f"{item}\n")

    print("part1 numsafe real:", len(listSafeHarsh))
    print("part2 numsafe real:", len(listSafeForgiving))
