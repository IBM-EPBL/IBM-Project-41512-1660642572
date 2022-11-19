from project_content import *
import ibm_db

import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=sxs46868;PWD=e6sL28GSXIPtNJG0;", '', '')



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    return render_template('register_form.html')


@app.route('/login')
def login():
    return render_template('login_form.html')


@app.route('/main')
def main():
    return render_template('main_page.html')


@app.route('/register_backend', methods=['POST', 'GET'])
def register_backend():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        phone = request.form['phone']
        email = request.form['email']
        passw = request.form['passw']
        confirm_passw = request.form['confirm_passw']

        sql = "SELECT * FROM users WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('login_form.html', msg="You are already a member, please login using your details")
        else:
            if passw == confirm_passw:
                insert_sql = "INSERT INTO users VALUES (?,?,?,?,?,?)"
                prep_stmt = ibm_db.prepare(conn, insert_sql)
                ibm_db.bind_param(prep_stmt, 1, fname)
                ibm_db.bind_param(prep_stmt, 2, lname)
                ibm_db.bind_param(prep_stmt, 3, dob)
                ibm_db.bind_param(prep_stmt, 4, phone)
                ibm_db.bind_param(prep_stmt, 5, email)
                ibm_db.bind_param(prep_stmt, 6, passw)
                ibm_db.execute(prep_stmt)

        return render_template('home.html', msg="Student Data saved successfully... \nNow you can login...")


@app.route('/login_backend', methods=['POST', 'GET'])
def login_backend():
    if request.method=='POST':
        email = request.form['email']
        passw = request.form['passw']

        sql = "SELECT * FROM users WHERE email =? and password =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.bind_param(stmt, 2, passw)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('main_page.html', msg="Hurray you're logged in")
        else:
            return render_template('login_form.html', msg="Your login credentials are incorrect")


@app.route('/listUsers')
def listUsers():
    users_data = []
    sql = "SELECT * FROM users"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        # print ("The Name is : ",  dictionary)
        users_data.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if users_data:
        print(users_data)
        return render_template("list_users.html", students=users_data)

@app.route('/details_profile')
def details_profile():
    return render_template("details_profile.html")

@app.route('/job_avail')
def job_avail():
    return render_template("job_avail.html")

@app.route('/details_profile_backend', methods=['POST', 'GET'])
def details_profile_backend():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        degree = request.form['degree']
        stream = request.form['stream']
        hsc = request.form['HSC']
        sslc = request.form['SSLC']
        technical = request.form['technical']

        sql = "SELECT * FROM details_profile WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('details_profile.html', msg="enter your details then only you can see job offers")
        else:
            
            insert_sql = "INSERT INTO details_profile VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, fname)
            ibm_db.bind_param(prep_stmt, 2, lname)
            ibm_db.bind_param(prep_stmt, 3, dob)
            ibm_db.bind_param(prep_stmt, 4, phone)
            ibm_db.bind_param(prep_stmt, 5, email)
            ibm_db.bind_param(prep_stmt, 6, address)
            ibm_db.bind_param(prep_stmt, 7, city)
            ibm_db.bind_param(prep_stmt, 8, degree)
            ibm_db.bind_param(prep_stmt, 9, stream)
            ibm_db.bind_param(prep_stmt, 10, hsc)
            ibm_db.bind_param(prep_stmt, 11, sslc)
            ibm_db.bind_param(prep_stmt, 12, technical)
            ibm_db.execute(prep_stmt)

            return render_template('main_page.html', msg="Student Data saved successfully... \nNow you can login...")
