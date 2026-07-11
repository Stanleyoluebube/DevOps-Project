from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def lucky_numbers():
    # Generate 6 random unique lucky numbers between 1 and 49
    numbers = sorted(random.sample(range(1, 50), 6))
    numbers_str = ", ".join(map(str, numbers))
    
    return f"""
    <html>
        <head><title>Lucky Number Generator</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1>🍀 Your Lucky Numbers For Today 🍀</h1>
            <h2 style="color: #2e7d32; letter-spacing: 2px;">{numbers_str}</h2>
            <p>Refresh the page to generate a new set!</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8080)