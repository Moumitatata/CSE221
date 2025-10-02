def sort_trains():
    N = int(input())
    trains = []
    
    for idx in range(N):
        parts = input().split()
        name = parts[0]
        destination = parts[4]
        time = parts[-1]
        
        hh, mm = map(int,time.split(':'))
        total_minutes = hh * 60 + mm
        trains.append((name, destination, time, total_minutes, idx))

    for i in range(1, N):
        current = trains[i]
        current_name = current[0]
        current_time = current[3]
        
        j = i - 1
        while j >= 0:
            prev = trains[j]
            prev_name = prev[0]
            prev_time = prev[3]
            
            if (current_name < prev_name) or (current_name == prev_name and current_time > prev_time):
                trains[j + 1] = trains[j]
                j -= 1
            else:
                break
        
        trains[j + 1] = current

    for t in trains:
        print(f"{t[0]} will departure for {t[1]} at {t[2]}")

sort_trains()