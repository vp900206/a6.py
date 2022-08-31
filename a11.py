from turtle import clear


n=complex(input("Enter a complex number "))
if n.real > n.imag:
    print(n.real)
else:
    print(n.imag)