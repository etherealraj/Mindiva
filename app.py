from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'  # Needed for session management

# In-memory 'database' of users for this example (in a real app, use a database)
users = {
    'test@example.com': {'name': 'Test User', 'password': 'password123'}
}

# Route for the front page
@app.route('/')
def index():
    return render_template('front.html')

# Route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Store the user in the 'users' dictionary (in reality, save to a database)
        users[email] = {'name': name, 'password': password}
        
        # Redirect to login after successful signup
        return redirect(url_for('login'))
    
    return render_template('signup.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if user exists and password matches
        if email in users and users[email]['password'] == password:
            # Save user in session
            session['user'] = users[email]['name']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
    
    return render_template('login.html')

# Route for the dashboard (only accessible after login)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user_name = session['user']
        return render_template('dashboard.html', user=user_name)
    else:
        return redirect(url_for('login'))

# Route to log out
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

# Route for the About Us page
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)
