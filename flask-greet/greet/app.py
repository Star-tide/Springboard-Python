from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    html = '''
    <html>
        <body>
            <h1>Welcome to the Main page!</h1>
            <a href='/welcome'>Go to the welcome Page</a>
            <a href='/welcome/home'>Go to the welcome home Page</a>
            <a href='/welcome/back'>Go to the welcome back page
        </body>
    </html>
    '''
    return html

@app.route('/welcome')
def welcome():
    return f'welcome'
    
@app.route('/welcome/<page>')
def router(page):
        return f'welcome {page}'
