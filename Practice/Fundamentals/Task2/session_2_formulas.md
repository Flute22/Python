# Session 2 — Formula Sheet

---

## P1 — Salary Deduction
```
HRA = (10/100) × CTC
DA  = (5/100)  × CTC
PF  = (3/100)  × CTC
Tax = slab% × CTC         # based on CTC / 100000 (in lakhs)

Monthly In-Hand = (CTC - HRA - DA - PF - Tax) / 12
```
> All deductions on **original CTC**. Divide by 12 for monthly.

---

## P2 — Valid Triangle
```
A + B + C == 180  AND  all angles > 0
```
> Both conditions must be True simultaneously.

---

## P3 — Profit or Loss
```
SP > CP → Profit = SP - CP
SP < CP → Loss   = CP - SP
SP == CP → No Profit No Loss
```
> Compare selling price vs cost price.

---

## P4 — Unit Conversions
```
cm  → ft    = cm / 30.48
km  → miles = km × 0.621371
USD → INR   = usd × 84
```
> Use `float(input())` to handle decimal values.

---

## P5 — Fibonacci
```
F(n) = F(n-1) + F(n-2)
a, b = b, a + b            # shift at each step
```
> Start with `[0, 1]`, loop `n - 2` times.

---

## P6 — Factorial
```
n! = n × (n-1) × ... × 1
fact *= i                  # for i in range(1, n+1)
```
> `0! = 1` by definition.

---

## P7 — Reverse Integer
```
int(str(n)[::-1])          # string slice method
n % 10  → last digit
n // 10 → remove last digit
```
> `[::-1]` reverses any string in Python.

---

## P8 — Conditional Sum
```
i % 5 == 0  → skip (continue)
sum + i > 300 → stop (break)
```
> Increment `i` **before** `continue`. Check limit **before** adding.

---

## P9a — Sum & Average Until Zero
```
total += user_input
count += 1
avg = total / count
```
> Divide by `count`, not by 2.

---

## P9b — Divisible by 7, Not Multiple of 5
```
i % 7 == 0  AND  i % 5 != 0
Range: 2000 to 3200
```
> Output: `", ".join(map(str, result))`

---

## P10 — All Even Digits
```
all(int(j) % 2 == 0 for j in str(i))
Even digits: 0, 2, 4, 6, 8
```
> Convert each digit to `int` before checking `% 2`.

---

## P11 — Robot Distance
```
x = RIGHT - LEFT
y = UP - DOWN
distance = √(x² + y²)     # math.sqrt(x**2 + y**2)
```
> Round to nearest integer for float result.

---

## P12 — Prime Number
```
Check divisors up to √n only
range(3, int(math.sqrt(n)) + 1, 2)
```
> `math.sqrt()` returns float — wrap with `int()` for `range()`.

---

## P13 — Armstrong Number
```
153 = 1³ + 5³ + 3³ = 153
sum(int(j)**3 for j in str(n)) == n
```
> Reset digit list for each number inside the loop.

---

## P14 — Clock Angle
```
minute_angle = M × 6
hour_angle   = H × 30 + M × 0.5
diff         = |hour_angle - minute_angle|
answer       = int(min(diff, 360 - diff))
```
> Hour hand moves `0.5°` per minute too.

---

## P15 — Rectangle Overlap
```
No overlap if:
  l1[0] > r2[0] or l2[0] > r1[0]   # one is left of other
  l1[1] < r2[1] or l2[1] < r1[1]   # one is above other
```
> Use `or` for each check — either condition means no overlap.
