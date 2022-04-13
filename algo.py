def findSeq(processes, n, bt, wt, quantum, comT):
    rem_bt = [0] * n
    sequence = []
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0

    while (1):
        done = True

        for i in range(n):

            if (rem_bt[i] > 0):
                done = False

                if (rem_bt[i] > quantum):

                    t += quantum

                    rem_bt[i] -= quantum
                    sequence.append((i, t))
                else:

                    t = t + rem_bt[i]
                    comT[i] = t

                    wt[i] = t - bt[i]
                    sequence.append((i, t))

                    rem_bt[i] = 0

        if (done == True):
            break
    return sequence


def findTurnAroundTime(processes, n, arrTime, comTime, tat):
    for i in range(n):
        tat[i] = comTime[i] - arrTime[i]

# n= total number of processes

def findResponseTime(n, arrTime,seq):
    nums = []
    time = []
    for i in range(0,n):
        if i == 0:
            nums.append(seq[i][0])
            time.append(0)
        
        if seq[i][0] not in nums:
            nums.append(seq[i][0])
            time.append(seq[i - 1][1])

    for i in range(0,n):
        if i != 0:
            time[i] =  abs(time[i] - arrTime[i])

    return time

def findavgTime(processes, n, bt, quantum, arivalTime):
    wt = [0] * n
    tat = [0] * n
    comT = [0] * n

    seq = findSeq(processes, n, bt, wt, quantum, comT)
    findTurnAroundTime(processes, n, arivalTime, comT, tat)
    resTime = findResponseTime(n,arivalTime,seq)

    for x in range(0, n):
        wt[x] = tat[x] - bt[x]
        if wt[x] < 0:
            wt[x] = 0

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    avgWaitTime = total_wt / n
    avgTatTime = total_tat / n

    return avgTatTime, avgWaitTime, comT, tat, wt, seq, resTime