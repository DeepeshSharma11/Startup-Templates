from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():  # Change from 'home' to 'index'
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/features')
def features():
    return render_template('feature.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonial.html')

@app.route('/quote')
def quote():
    return render_template('quote.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Handle contact form submission
    return "Contact form submitted successfully"

@app.route('/submit_quote', methods=['POST'])
def submit_quote():
    # Handle quote form submission
    return "Quote request submitted successfully"

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Handle newsletter subscription
    return "Subscribed successfully"

if __name__ == '__main__':
    app.run()