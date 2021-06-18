def solution(bridge_length, weight, truck_weights):
    on_bridge = []
    ob_weight = 0
    result = 0

    for truck in truck_weights:
        if len(on_bridge) < bridge_length and ob_weight + truck <= weight:
            result += 1
        else:
            while ob_weight + truck > weight or len(on_bridge) >= bridge_length:
                tmp = on_bridge.pop(0)
                ob_weight -= tmp[0]
                result = bridge_length + tmp[1]

        if on_bridge and on_bridge[0][1] + bridge_length == result:
            tmp = on_bridge.pop(0)
            ob_weight -= tmp[0]

        on_bridge.append([truck, result])
        ob_weight += truck

    while on_bridge:
        tmp = on_bridge.pop(0)
        result = bridge_length + tmp[1]

    return result


if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10, 10]
    print(solution(bridge_length, weight, truck_weights))