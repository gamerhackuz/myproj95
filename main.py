# calculator.py
import sys

def calculator():
    print("🔢 Python Kalkulyatori")
    print("Amallar: +, -, *, /, %, q (chiqish)")
    
    while True:
        try:
            op = input("\n➗ Amalni kiriting (+, -, *, /, %, q): ").strip()
            if op.lower() == 'q':
                print("👋 Dasturdan chiqildi. Xayr!")
                sys.exit()
            if op not in ['+', '-', '*', '/', '%']:
                print("❌ Noto'g'ri amal. Qayta urinib ko'ring.")
                continue

            n1 = float(input("🔢 Birinchi son: "))
            n2 = float(input("🔢 Ikkinchi son: "))

            if op == '+': res = n1 + n2
            elif op == '-': res = n1 - n2
            elif op == '*': res = n1 * n2
            elif op == '/':
                if n2 == 0: raise ZeroDivisionError
                res = n1 / n2
            elif op == '%':
                if n2 == 0: raise ZeroDivisionError
                res = n1 % n2

            print(f"✅ Natija: {n1} {op} {n2} = {res}")

        except ValueError:
            print("❌ Iltimos, faqat sonlar kiriting.")
        except ZeroDivisionError:
            print("❌ Nolga bo'lish mumkin emas!")
        except Exception as e:
            print(f"⚠️ Xatolik: {e}")

if __name__ == "__main__":
    calculator()