def bouncing_ball(h, bounce, window):
    if bounce >= 1 or h <= 0 or window > h: return -1
    else: 
        count = 0
        while window < h:
            count += 1; h = h * bounce
            if window < h: count += 1 
        return count
print(bouncing_ball(30, 0.75, 1.5))