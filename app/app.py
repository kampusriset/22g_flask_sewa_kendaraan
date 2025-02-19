from flask import Flask, render_template, request, redirect ,url_for, flash, session
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rental'

mysql = MySQL(app)


#Index
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `mobil`")
    data = cur.fetchall()
    return render_template('index.html', data_mobil=data)

#Admin
@app.route('/admin')
def Admin():
    return render_template('admin.html',username=session['username'])

#Pesan
@app.route('/pesan')
def pesan():
    return render_template('pesan.html')

@app.route('/pesan',methods = ['POST'])
def insert_pelanggan():
    if request.method == "POST":
        flash('Berhasil membuat pesanan! \n Silahkan menunggu panggilan dari kami')
        nama = request.form['nama_pelanggan']
        alamat = request.form['alamat']
        jenis_kelamin = request.form['jenis_kelamin']
        no_telp = request.form['no_telp']
        mobil = request.form['merek']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `pelanggan`(`nama_pelanggan`, `alamat`,`jenis_kelamin`,`no_telp`,`mobil`) VALUES (%s, %s,%s,%s,%s)",(nama, alamat, jenis_kelamin, no_telp, mobil))
        mysql.connection.commit()
        return redirect(url_for('pesan'))

#SignUp
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/signup', methods = ['POST'])
def sign_up():
    if request.method == "POST":
        flash('Account Created!')
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `admin`(`username`, `password`) VALUES (%s, %s)",(username, password))
        mysql.connection.commit()
        return redirect(url_for('signup'))

#LogIn    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login', methods = ['GET','POST'])
def log_in():
    msg=''
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT * FROM admin WHERE username=%s AND password=%s',(username,password))
        record = cur.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('Admin'))
        else:
            flash('Incorrect username or password')
    return render_template('login.html',msg=msg)

#Ubah Password
class UpdatePasswordForm(FlaskForm):
    username = PasswordField('Username', validators=[DataRequired()])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=3)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        cur.execute('SELECT password FROM admin WHERE username = %s', (form.username.data,))
        record = cur.fetchone()
        print("Record:", record)  # Debugging statement
        if record and record[0] == form.current_password.data:
            new_password = form.new_password.data
            cur.execute("UPDATE admin SET password = %s WHERE username = %s", (new_password, form.username.data))
            mysql.connection.commit()
            flash('Password Anda telah diperbarui!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Password saat ini salah.', 'danger')
    else:
        print("Form errors:", form.errors)  # Debugging statement
    return render_template('change_password.html', form=form)



#LogOut
@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    return redirect(url_for('login'))


#Karyawan
@app.route('/karyawan')
def karyawan():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM karyawan")
    data = cur.fetchall()
    
    return render_template('karyawan.html', data_karyawan=data)

@app.route('/insert_karyawan', methods = ['POST'])
def insert_karyawan():
    if request.method == "POST":
        flash('Data berhasil dimasukkan!')
        id_data = request.form['id']
        nama = request.form['nama']
        alamat = request.form['alamat']
        no_telp = request.form['no_telp']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `karyawan`(`id_karyawan`, `nama_karyawan`, `alamat`,`no_telp`) VALUES (%s, %s, %s,%s)",(id_data, nama, alamat,no_telp))
        mysql.connection.commit()
        return redirect(url_for('karyawan'))
    
@app.route('/update_karyawan', methods= ['POST', 'GET'])
def update_karyawan():
    if request.method == 'POST':
        id_data = request.form['id']
        nama = request.form['nama']
        alamat = request.form['alamat']
        no_telp = request.form['no_telp']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE `karyawan` SET `id_karyawan`=%s,`nama_karyawan`=%s,`alamat`=%s,`no_telp`=%s  WHERE `karyawan`.`id_karyawan`=%s",(id_data, nama, alamat,no_telp, id_data))
        flash("Data berhasil diubah!")
        mysql.connection.commit()
        return redirect(url_for('karyawan'))
    
@app.route('/delete_karyawan/<string:id_data>', methods = ['POST', 'GET'])
def delete_karyawan(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `karyawan` WHERE `karyawan`.`id_karyawan` = %s",(id_data))
    flash('Data berhasil dihapus!')
    mysql.connection.commit()
    return redirect(url_for('karyawan'))

#Pelanggan
@app.route('/pelanggan')
def pelanggan():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pelanggan")
    data = cur.fetchall()
    
    return render_template('pelanggan.html', data_pelanggan=data)

@app.route('/insert_pelanggan', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash('Data berhasil dimasukkan!')
        id_data = request.form['id']
        nama = request.form['nama']
        alamat = request.form['alamat']
        jenis_kelamin = request.form['jenis_kelamin']
        no_telp = request.form['no_telp']
        mobil = request.form['mobil']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `pelanggan`(`id_pelanggan`, `nama_pelanggan`, `alamat`,`jenis_kelamin`,`no_telp`,`mobil`) VALUES (%s, %s, %s,%s,%s,%s)",(id_data, nama, alamat,jenis_kelamin,no_telp,mobil))
        mysql.connection.commit()
        return redirect(url_for('pelanggan'))
    
@app.route('/update_pelanggan', methods= ['POST', 'GET'])
def update_pelanggan():
    if request.method == 'POST':
        id_data = request.form['id']
        nama = request.form['nama']
        alamat = request.form['alamat']
        jenis_kelamin = request.form['jenis_kelamin']
        no_telp = request.form['no_telp']
        mobil = request.form['mobil']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE `pelanggan` SET `id_pelanggan`=%s,`nama_pelanggan`=%s,`alamat`=%s,`jenis_kelamin`=%s,`no_telp`=%s,`mobil`=%s  WHERE `pelanggan`.`id_pelanggan`=%s",(id_data, nama, alamat,jenis_kelamin,no_telp,mobil, id_data))
        flash("Data berhasil diubah!")
        mysql.connection.commit()
        return redirect(url_for('pelanggan'))
    
@app.route('/delete_pelanggan/<string:id_data>', methods = ['POST', 'GET'])
def delete_pelanggan(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `pelanggan` WHERE `pelanggan`.`id_pelanggan` = %s",(id_data,))
    flash('Data berhasil dihapus!')
    mysql.connection.commit()
    return redirect(url_for('pelanggan'))

#Mobil
@app.route('/mobil')
def mobil():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mobil")
    data = cur.fetchall()
    
    return render_template('mobil.html', data_mobil=data)

@app.route('/insert_mobil', methods = ['POST'])
def insert_mobil():
    if request.method == "POST":
        flash('Data berhasil dimasukkan!')
        id_data = request.form['id']
        merek = request.form['merek']
        warna = request.form['warna']
        no_plat = request.form['no_plat']
        harga_sewa = request.form['harga_sewa']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `mobil`(`id_mobil`, `merek`, `warna`,`no_plat`,`harga_sewa`) VALUES (%s, %s, %s,%s,%s)",(id_data, merek,warna,no_plat,harga_sewa))
        mysql.connection.commit()
        return redirect(url_for('mobil'))
    
@app.route('/update_mobil', methods= ['POST', 'GET'])
def update_mobil():
    if request.method == 'POST':
        id_data = request.form['id']
        merek = request.form['merek']
        warna = request.form['warna']
        no_plat = request.form['no_plat']
        harga_sewa = request.form['harga_sewa']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE `mobil` SET `id_mobil`=%s,`merek`=%s,`warna`=%s,`no_plat`=%s,`harga_sewa`=%s  WHERE `mobil`.`id_mobil`=%s",(id_data, merek, warna,no_plat,harga_sewa, id_data))
        flash("Data berhasil diubah!")
        mysql.connection.commit()
        return redirect(url_for('mobil'))
    
@app.route('/delete/<string:id_data>', methods = ['POST', 'GET'])
def delete_mobil(id_data):
    
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `mobil` WHERE `mobil`.`id_mobil`=%s",(id_data,))
    flash('Data berhasil dihapus!')
    mysql.connection.commit()
    return redirect(url_for('mobil'))

#Rental
@app.route('/rental')
def rental():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sewa")
    data = cur.fetchall()
    
    return render_template('rental.html', data_rental=data)


@app.route('/insert_rental', methods = ['POST'])
def insert_rental():
    if request.method == "POST":
        flash('Data berhasil dimasukkan!')
        id_data = request.form['id']
        id_mobil = request.form['id_mobil']
        tgl_sewa = request.form['tgl_sewa']
        tgl_kembali = request.form['tgl_kembali']
        total_bayar = request.form['total_bayar']
        denda = request.form['denda']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `sewa`(`id_sewa`, `id_mobil`, `tgl_sewa`,`tgl_kembali`,`total_bayar`,`denda`) VALUES (%s, %s, %s,%s,%s,%s)",(id_data, id_mobil, tgl_sewa,tgl_kembali,total_bayar,denda))
        mysql.connection.commit()
        return redirect(url_for('rental'))
    
@app.route('/update_rental', methods= ['POST', 'GET'])
def update_rental():
    if request.method == 'POST':
        id_data = request.form['id']
        id_mobil = request.form['id_mobil']
        tgl_sewa = request.form['tgl_sewa']
        tgl_kembali = request.form['tgl_kembali']
        total_bayar = request.form['total_bayar']
        denda = request.form['denda']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE `sewa` SET `id_sewa`=%s,`id_mobil`=%s,`tgl_sewa`=%s,`tgl_kembali`=%s,`total_bayar`=%s,`denda`=%s  WHERE `sewa`.`id_sewa`=%s",(id_data, id_mobil, tgl_sewa,tgl_kembali,total_bayar,denda, id_data))
        flash("Data berhasil diubah!")
        mysql.connection.commit()
        return redirect(url_for('rental'))
    
@app.route('/delete_rental/<string:id_data>', methods = ['POST', 'GET'])
def delete_rental(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `sewa` WHERE `sewa`.`id_sewa` = %s",(id_data))
    flash('Data berhasil dihapus!')
    mysql.connection.commit()
    return redirect(url_for('rental'))



if __name__ == "__main__":
    app.run(debug=True)
