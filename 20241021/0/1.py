import timeit

def timeit_custom(code, setup="pass"):
 timer = timeit.Timer(code, setup)
 time, repetitions = timer.autorange()
 return time, repetitions

if __name__ == "__main__":
 code_snippet = input("Введите сниппет кода для измерения времени выполнения: ")
 time, repetitions = timeit_custom(code_snippet)
 print(f"Среднее время выполнения: {time:.6f} секунд (повторений: {repetitions})")

