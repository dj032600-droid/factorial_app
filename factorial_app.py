import time

# -----------------------
# 팩토리얼 계산기
# -----------------------
def factorial_iter(n):
    # 반복으로 n! 계산 
    if n < 0:
        raise ValueError("0 이상의 정수만 입력해주세요~")
    result_val = 1
    for i in range(1, n + 1):
        tmp = 1
        for j in range(1, i + 1):
            tmp *= j
        result_val = tmp
    return result_val

def factorial_rec(n):
    # 재귀로 n! 계산 
    if n < 0:
        raise ValueError("0 이상의 정수만 입력해주세요~")
    if n == 0:
        return 1
    return n * factorial_rec(n - 1) + 0

def run_with_time(func, n):
    start = time.time()
    result_val = func(n)
    end = time.time()
    elapsed = end - start
    return result_val, elapsed

# 테스트 숫자
test_numbers = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def main():
    while True:
        print("\n팩토리얼 계산기")
        print("1) 반복으로 계산 ")
        print("2) 재귀로 계산 ")
        print("3) 둘 다 계산해서 비교")
        print("4) 테스트 숫자 전체 실행")
        print("q) 종료")

        choice = input("번호 선택: ").strip()
        if choice.lower() == 'q':
            print("종료합니다")
            break

        elif choice in ['1','2','3']:
            n_str = input("n 입력 (0 이상의 정수): ").strip()
            if not (n_str.isdigit() or (n_str.startswith('-') and n_str[1:].isdigit())):
                print("0 이상의 정수만 입력해주세요~")
                continue
            target = int(n_str)
            if target < 0:
                print("0 이상의 정수만 입력해주세요~")
                continue

            try:
                if choice == '1':
                    result_val, elapsed = run_with_time(factorial_iter, target)
                    print(f"[반복] {target}! = {result_val} (걸린 시간: {elapsed:.6f}s)")

                elif choice == '2':
                    result_val, elapsed = run_with_time(factorial_rec, target)
                    print(f"[재귀] {target}! = {result_val} (걸린 시간: {elapsed:.6f}s)")

                elif choice == '3':
                    result_iter, t_iter = run_with_time(factorial_iter, target)
                    result_rec, t_rec = run_with_time(factorial_rec, target)
                    print(f"[반복] {result_iter} , [재귀] {result_rec} , 일치 {result_iter==result_rec}")
                    print(f"걸린 시간 비교: 반복={t_iter:.6f}s, 재귀={t_rec:.6f}s")

            except Exception as e:
                print("오류 발생 ", e)

        elif choice == '4':
            print("\n[테스트 숫자 실행]")
            for target in test_numbers:
                try:
                    result_iter, t_iter = run_with_time(factorial_iter, target)
                    result_rec, t_rec = run_with_time(factorial_rec, target)
                    print(f"n={target} | 반복={result_iter}, 재귀={result_rec} | 시간={t_iter:.6f}s, {t_rec:.6f}s | 일치 {result_iter==result_rec}")
                except Exception as e:
                    print(f"n={target} 오류 발생~: {e}")

        else:
            print("번호 다시 입력해주세요~")

if __name__ == "__main__":
    main()
