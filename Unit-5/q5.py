# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def sum(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    total = num1 + num2
    return HttpResponse(total)

def product(request):
    numbers = request.GET.get('numbers')
    numbers_list = numbers.split(',')
    total = 1
    for num in numbers_list:
        total *= int(num)
    return HttpResponse(total)

def power(request):
    exponent = int(request.GET.get('exponent'))
    result = 2 ** exponent
    return HttpResponse(result)

@csrf_exempt
def equation(request):
    if request.method == 'POST':
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        c = float(request.POST.get('c'))
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return HttpResponse(f'x1={x1}, x2={x2}')
    return render(request, 'equation.html')

<!-- home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Numerical Problems</title>
</head>
<body>
    <h1>Numerical Problems</h1>
    <ul>
        <li><a href="/sum/">Sum of Numbers</a></li>
        <li><a href="/product/">Product of Numbers</a></li>
        <li><a href="/power/">Power of Two</a></li>
        <li><a href="/equation/">Solving an Equation</a></li>
    </ul>
</body>
</html>

<!-- equation.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Solving an Equation</title>
</head>
<body>
    <h1>Solving an Equation</h1>
    <form method="post">
        {% csrf_token %}
        <label for="a">a:</label>
        <input type="text" name="a" required><br>
        <label for="b">b:</label>
        <input type="text" name="b" required><br>
        <label for="c">c:</label>
        <input type="text" name="c" required><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
