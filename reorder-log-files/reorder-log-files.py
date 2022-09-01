class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLog = []
        digitLog = []
        
        for log in logs:
            if (log.split()[1]).isdigit():
                digitLog.append(log)
            else:
                letterLog.append(log.split())
        letterLog.sort(key = lambda x: x[0:])
        letterLog.sort(key = lambda x: x[1:])

        
        for i in range(len(letterLog)):
            letterLog[i] = " ".join(letterLog[i])
        letterLog.extend(digitLog)
        
        return letterLog