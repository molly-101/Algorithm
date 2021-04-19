def solution(routes):
    routes = sorted(routes, key=lambda x: x[0])
    camera = 1
    now = float('inf')

    for route in routes:
        if now > route[1]:
            now = route[1]
        elif now < route[0]:
            camera += 1
            now = route[1]

    return camera