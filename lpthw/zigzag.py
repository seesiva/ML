def zigzags(input):
    input = iter(input)
    stack = None
    try:
        stack = [next(input)]
        while True:
            if len(stack) < 2:
                stack.append(next(input))
            else:
                stack = stack[-2:]
            a, b = stack
            if a == b:
                yield (a,)
                stack = [b]
                continue
            zig = a > b
            while True:
                prev = stack[-1]
                this = next(input)
                if prev == this or zig == (prev > this):
                    break
                stack.append(this)
                zig = not zig
            yield tuple(stack)
            stack.append(this)
    except StopIteration:
        pass
    if stack:
        yield tuple(stack)

def zigzag(input):
    item = max(zigzags(input), key=len)
    print len(item), item


if __name__=="__main__":
    print zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6])
    #print zigzag([2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4])

    #print neighbours_state(3,4,2)