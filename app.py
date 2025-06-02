from flask import Flask, render_template, request
from bot.database import list_tables, read_usernames_from_table, send_direct_message

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    tables = list_tables()
    return render_template('index.html', tables=tables)

@app.route('/directbot', methods=['POST'])
def directbot():
    table_name = request.form['table_name']
    message = request.form['message']
    delay = int(request.form['delay'])
    
    my_username = 'username' # Altere para o seu username
    my_password = 'password' # Altere para o seu password

    recipient_usernames = read_usernames_from_table(table_name)
    
    send_direct_message(my_username, my_password, recipient_usernames, message, delay)

    return render_template('index.html', category='success', tables=list_tables())

if __name__ == '__main__':
    app.run(debug=True)
