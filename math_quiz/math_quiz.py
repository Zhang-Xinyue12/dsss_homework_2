import random


def calculate_result_A(min, max):
    """
    Generate a random integer between min and max.
    生成一个在 min 和 max 之间的随机整数。
    """
    return random.randint(min, max)


def calculate_result_B():
    """
    Randomly select an operator from '+', '-', '*'.
    从 '+', '-', '*' 中随机选择一个运算符。
    """
    return random.choice(['+', '-', '*'])


def calculate_result_C(n1, n2, o):
    """
    Create a math problem string and calculate the expected answer.
    根据给定的运算符生成数学问题的字符串形式，并计算预期的答案。

    Parameters:
    n1 (int): First number 第一数字
    n2 (int): Second number 第二数字
    o (str): Operator 运算符

    Returns:
    tuple: The problem string and the calculated answer (问题字符串和计算的答案).
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2  # 加法运算
    elif o == '-':
        a = n1 - n2  # 减法运算
    else:
        a = n1 * n2  # 乘法运算
    return p, a


def math_quiz():
    """
    Start the math quiz game, where players answer random math problems.
    启动数学测验游戏，玩家需要回答随机生成的数学问题。
    """
    s = 0  # Initialize score 分数初始化
    t_q = 3  # Total number of questions 总问题数 (改为整数 3 避免出错)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    print("欢迎来到数学测验游戏！您将面对一些数学问题，需要提供正确答案。")

    for _ in range(t_q):
        # Generate random numbers and operator for the question 生成问题的随机数和运算符
        n1 = calculate_result_A(1, 10)
        n2 = calculate_result_A(1, 5)
        o = calculate_result_B()

        # Generate the math problem and correct answer 生成数学问题和正确答案
        PROBLEM, ANSWER = calculate_result_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        # Use try-except to handle non-integer inputs 使用 try-except 来处理非整数输入
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")  # 输入无效，请输入整数
            continue  # Skip to the next question 跳到下一个问题

        # Check if the user's answer is correct 检查用户答案是否正确
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")
    print(f"游戏结束！你的得分是: {s}/{t_q}")


if __name__ == "__main__":
    math_quiz()
