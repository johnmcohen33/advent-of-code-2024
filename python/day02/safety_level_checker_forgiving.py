from safety_level_checker_base import SafetyLevelCheckerBase

class SafetyLevelCheckerForgiving(SafetyLevelCheckerBase):
    def is_safe_line(self, line):
        """ Returns if a line is safe... same rules as harsh ... except if you can remove one and satisfy.. it works """
        if len(line) < 2:
            return True # a single number is necessarily a safe one

        remainingErrors = 1 # Here we grace with one error        
        direction = line[0] > line[1]
        for i in range(1, len(line)):
            safeDir = (line[i-1] > line[i]) == direction
            safeDif = abs(line[i] - line[i-1]) <= 3
            if not (safeDif and safeDir):
                if remainingErrors == 0:
                    return False
                # remove the bad index ? dangerous?
                # del line[i]
                remainingErrors -= 1
        return True