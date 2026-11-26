# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline:
     #   Reverse Polish Notation is postfix: operands and values come before the operator like a division.
        #   ["2", "1", "+", "3", "*"] means (2 + 1) * 3.
        #   A stack matches that order. Push every number. When an operator shows up,
    #   the two numbers it needs are the last two pushed, so pop them, compute,
    #   and push the result. The last value left is the answer.
        #   Division truncates toward zero, which int(a / b) does (not //).
    stack = []
    for token in tokens:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(int(left / right))
        else:
            stack.append(int(token))
    return stack[-1]


def decode_string(s):
    # Outline:
        #   k[encoded] means "repeat encoded k times", and brackets can nest.
    #   "3[a2[c]]" is "acc" three times.
     #   When we hit '[', save the text and the repeat count from outside the
    #   brackets on a stack, then start a fresh string for the inside.
     #   When we hit ']', pop that saved pair and glue the repeated inside
    #   onto the outside text.
    stack = []
    current = ""
    count = 0
    for ch in s:
        if ch.isdigit():
            count = count * 10 + int(ch)
        elif ch == "[":
            stack.append((current, count))
            current = ""
            count = 0
        elif ch == "]":
            previous, repeat = stack.pop()
            current = previous + current * repeat
        else:
            current += ch
    return current


def daily_temperatures(temps):
    # Outline:
        #   For each day, how many days until a strictly warmer temperature?
        #   [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
            #   Keep a stack of days that are still waiting, stored as indices,
            #   with colder days on top. When today's temperature is warmer than
        #   the day on top, that day has found its answer: today - that index.
    #   Days that never find a warmer day stay 0.
    n = len(temps)
    answer = [0] * n
    waiting = []
    for today in range(n):
        while waiting and temps[today] > temps[waiting[-1]]:
            earlier = waiting.pop()
            answer[earlier] = today - earlier
        waiting.append(today)
    return answer


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
        #   Land is "1", water is "0". An island is land cells that touch
        #   up, down, left, or right (not diagonally).
    #   Scan the grid. Each time we find an unvisited "1", that starts
        #   a new island. Walk every connected land cell with a stack and
    #   mark them visited so they are not counted again.
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    def explore(start_r, start_c):
        stack = [(start_r, start_c)]
        visited.add((start_r, start_c))
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] == "1"
                ):
                    visited.add((nr, nc))
                    stack.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                explore(r, c)
    return islands


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
