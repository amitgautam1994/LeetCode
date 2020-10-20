def area(height):
    start = 0
    end = len(height)-1
    area = 0
    max_area = 0

    while start != end:
        if height[start] > height[end]:
            dist = end - start
            area = dist * height[end]
            end -= 1

        elif height[start] <= height[end]:
            dist = end - start
            area = dist * height[start]
            start += 1

        if area > max_area:
            max_area = area


    print(max_area)






area([1,8,6,2,5,4,8,3,7])



