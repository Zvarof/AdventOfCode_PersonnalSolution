import functools

Time = [42686985]
Distance = [284100511221341]

Mixed = zip(Time, Distance)
Recordings = []

for time, distance in Mixed:
    Winning_options = 0
    if time % 2 == 0:
        MaxPerf = (time/2)**2
        Delta = MaxPerf - distance
        Test = Delta**0.5
        if MaxPerf < distance:
            continue
        else:
            Winning_options += 1
            if (Test % 1 == 0):
                Winning_options += (int(Test)-1) * 2
            else:
                Winning_options += int(Test)*2
    else:
        MaxPerf = int(time/2)*((time+1)/2)
        Delta = MaxPerf - distance
        Test = Delta**0.5
        if (MaxPerf) < distance:
            continue
        else:
            Winning_options += 2
            if (Delta/int(Test + 1) % 1 == 0):
                Winning_options += int(Delta/int(Test + 1)-1)*2
            else:
                Winning_options += int(Delta/int(Test + 1))*2
    Recordings.append(Winning_options)

Result1 = functools.reduce(lambda a, b: a*b, Recordings)
print("Résultat = ", Result1)



