import smtplib
from email.message import EmailMessage
import random
import string
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_connection

app = Flask(__name__)
app.secret_key = '1234'

def generar_codigo():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/Registrarse')
def registro():
    return render_template('Registrarse.html')

@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    nombre = request.form['nombre']
    gmail = request.form['gmail']
    contrasena = request.form['contrasena']
    confirmar = request.form['confirmar']

    if contrasena != confirmar:
        flash('Las contraseñas no coinciden.')
        return redirect(url_for('registro'))

    hash_contrasena = generate_password_hash(contrasena)

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            'INSERT INTO "Registro_Usuario" ("Nombre", gmail, contraseña) VALUES (%s, %s, %s)',
            (nombre, gmail, hash_contrasena)
        )
        conn.commit()
        flash('Usuario registrado correctamente.')
        return redirect(url_for('login'))
    except Exception as e:
        conn.rollback()
        flash(f'Error al registrar usuario: {e}')
        return redirect(url_for('registro'))
    finally:
        cur.close()
        conn.close()
        
@app.route('/timbre')
def timbre():
    return render_template('timbre.html')

@app.route('/timbre/<dia>', methods=['GET', 'POST'])
def timbre_dia():
    return render_template("timbre.html")

@app.route('/lunes', methods=['GET', 'POST'])
def lunes():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'agregar':
            hora = int(request.form['hora'])
            minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            fk_usuario = 1  # Esto lo puedes adaptar según el usuario logueado

            try:
                cur.execute('''
                    INSERT INTO "Horario_Timbre" (dia, hora, minuto, habilitado, fk_usuario)
                    VALUES (%s, %s, %s, %s, %s)
                ''', ('Lunes', hora, minuto, habilitado, fk_usuario))
                conn.commit()
                flash('Horario agregado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al agregar horario: {e}')

        elif action == 'eliminar':
            id_horario = int(request.form['id'])
            try:
                cur.execute('DELETE FROM "Horario_Timbre" WHERE id = %s', (id_horario,))
                conn.commit()
                flash('Horario eliminado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al eliminar horario: {e}')

        elif action == 'editar':
            id_horario = int(request.form['id'])
            nueva_hora = int(request.form['hora'])
            nuevo_minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            try:
                cur.execute('''
                    UPDATE "Horario_Timbre"
                    SET hora = %s, minuto = %s, habilitado = %s
                    WHERE id = %s
                ''', (nueva_hora, nuevo_minuto, habilitado, id_horario))
                conn.commit()
                flash('Horario modificado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al modificar horario: {e}')

    cur.execute('SELECT id, hora, minuto, habilitado FROM "Horario_Timbre" WHERE dia = %s ORDER BY hora, minuto', ('Lunes',))
    horarios = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('lunes.html', horarios=horarios)


@app.route('/Martes', methods=['GET', 'POST'])
def Martes():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'agregar':
            hora = int(request.form['hora'])
            minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            fk_usuario = 1  # Esto lo puedes adaptar según el usuario logueado

            try:
                cur.execute('''
                    INSERT INTO "Horario_Timbre" (dia, hora, minuto, habilitado, fk_usuario)
                    VALUES (%s, %s, %s, %s, %s)
                ''', ('Martes', hora, minuto, habilitado, fk_usuario))
                conn.commit()
                flash('Horario agregado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al agregar horario: {e}')

        elif action == 'eliminar':
            id_horario = int(request.form['id'])
            try:
                cur.execute('DELETE FROM "Horario_Timbre" WHERE id = %s', (id_horario,))
                conn.commit()
                flash('Horario eliminado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al eliminar horario: {e}')

        elif action == 'editar':
            id_horario = int(request.form['id'])
            nueva_hora = int(request.form['hora'])
            nuevo_minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            try:
                cur.execute('''
                    UPDATE "Horario_Timbre"
                    SET hora = %s, minuto = %s, habilitado = %s
                    WHERE id = %s
                ''', (nueva_hora, nuevo_minuto, habilitado, id_horario))
                conn.commit()
                flash('Horario modificado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al modificar horario: {e}')

    cur.execute('SELECT id, hora, minuto, habilitado FROM "Horario_Timbre" WHERE dia = %s ORDER BY hora, minuto', ('Martes',))
    horarios = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('Martes.html', horarios=horarios)


@app.route('/Miercoles', methods=['GET', 'POST'])
def Miercoles():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'agregar':
            hora = int(request.form['hora'])
            minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            fk_usuario = 1  # Esto lo puedes adaptar según el usuario logueado

            try:
                cur.execute('''
                    INSERT INTO "Horario_Timbre" (dia, hora, minuto, habilitado, fk_usuario)
                    VALUES (%s, %s, %s, %s, %s)
                ''', ('Miercoles', hora, minuto, habilitado, fk_usuario))
                conn.commit()
                flash('Horario agregado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al agregar horario: {e}')

        elif action == 'eliminar':
            id_horario = int(request.form['id'])
            try:
                cur.execute('DELETE FROM "Horario_Timbre" WHERE id = %s', (id_horario,))
                conn.commit()
                flash('Horario eliminado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al eliminar horario: {e}')

        elif action == 'editar':
            id_horario = int(request.form['id'])
            nueva_hora = int(request.form['hora'])
            nuevo_minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            try:
                cur.execute('''
                    UPDATE "Horario_Timbre"
                    SET hora = %s, minuto = %s, habilitado = %s
                    WHERE id = %s
                ''', (nueva_hora, nuevo_minuto, habilitado, id_horario))
                conn.commit()
                flash('Horario modificado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al modificar horario: {e}')

    cur.execute('SELECT id, hora, minuto, habilitado FROM "Horario_Timbre" WHERE dia = %s ORDER BY hora, minuto', ('Miercoles',))
    horarios = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('Miercoles.html', horarios=horarios)

@app.route('/Jueves', methods=['GET', 'POST'])
def Jueves():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'agregar':
            hora = int(request.form['hora'])
            minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            fk_usuario = 1  # Esto lo puedes adaptar según el usuario logueado

            try:
                cur.execute('''
                    INSERT INTO "Horario_Timbre" (dia, hora, minuto, habilitado, fk_usuario)
                    VALUES (%s, %s, %s, %s, %s)
                ''', ('Jueves', hora, minuto, habilitado, fk_usuario))
                conn.commit()
                flash('Horario agregado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al agregar horario: {e}')

        elif action == 'eliminar':
            id_horario = int(request.form['id'])
            try:
                cur.execute('DELETE FROM "Horario_Timbre" WHERE id = %s', (id_horario,))
                conn.commit()
                flash('Horario eliminado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al eliminar horario: {e}')

        elif action == 'editar':
            id_horario = int(request.form['id'])
            nueva_hora = int(request.form['hora'])
            nuevo_minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            try:
                cur.execute('''
                    UPDATE "Horario_Timbre"
                    SET hora = %s, minuto = %s, habilitado = %s
                    WHERE id = %s
                ''', (nueva_hora, nuevo_minuto, habilitado, id_horario))
                conn.commit()
                flash('Horario modificado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al modificar horario: {e}')

    cur.execute('SELECT id, hora, minuto, habilitado FROM "Horario_Timbre" WHERE dia = %s ORDER BY hora, minuto', ('Jueves',))
    horarios = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('Jueves.html', horarios=horarios)

@app.route('/Viernes', methods=['GET', 'POST'])
def Viernes():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'agregar':
            hora = int(request.form['hora'])
            minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            fk_usuario = 1  # Esto lo puedes adaptar según el usuario logueado

            try:
                cur.execute('''
                    INSERT INTO "Horario_Timbre" (dia, hora, minuto, habilitado, fk_usuario)
                    VALUES (%s, %s, %s, %s, %s)
                ''', ('Viernes', hora, minuto, habilitado, fk_usuario))
                conn.commit()
                flash('Horario agregado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al agregar horario: {e}')

        elif action == 'eliminar':
            id_horario = int(request.form['id'])
            try:
                cur.execute('DELETE FROM "Horario_Timbre" WHERE id = %s', (id_horario,))
                conn.commit()
                flash('Horario eliminado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al eliminar horario: {e}')

        elif action == 'editar':
            id_horario = int(request.form['id'])
            nueva_hora = int(request.form['hora'])
            nuevo_minuto = int(request.form['minuto'])
            habilitado = 'habilitado' in request.form
            try:
                cur.execute('''
                    UPDATE "Horario_Timbre"
                    SET hora = %s, minuto = %s, habilitado = %s
                    WHERE id = %s
                ''', (nueva_hora, nuevo_minuto, habilitado, id_horario))
                conn.commit()
                flash('Horario modificado correctamente.')
            except Exception as e:
                conn.rollback()
                flash(f'Error al modificar horario: {e}')

    cur.execute('SELECT id, hora, minuto, habilitado FROM "Horario_Timbre" WHERE dia = %s ORDER BY hora, minuto', ('Viernes',))
    horarios = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('Viernes.html', horarios=horarios)







def enviar_correo(gmail, codigo):
    # Configura el mensaje
    msg = EmailMessage()
    msg.set_content(f'Hola, para recuperar tu contraseña, utiliza el siguiente código: {codigo}')
    msg['Subject'] = 'Recuperación de Contraseña'
    msg['From'] = '2025pruebax@gmail.com'  # Tu correo de envío
    msg['To'] = gmail

    # Enviar el correo a través de SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            # Usa la contraseña específica generada
            server.login('2025pruebax@gmail.com', 'qofy mabn qcro mmlr')  # Cambia por la contraseña específica
            server.send_message(msg)
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

@app.route('/olvide_contraseña')
def olvide_contraseña():
    return render_template('olvide_contraseña.html')

@app.route('/enviar_enlace', methods=['POST'])
def enviar_enlace():
    gmail = request.form['gmail']
    codigo = generar_codigo()  # Debes definir esta función para generar el código de recuperación

    # Conectarse a la base de datos
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Comprobar si el correo existe en la base de datos
        cur.execute('SELECT * FROM "Registro_Usuario" WHERE gmail = %s', (gmail,))
        usuario = cur.fetchone()

        if usuario:
            # Insertar el código en la tabla de códigos de recuperación
            cur.execute(
                'INSERT INTO "Codigos_Recuperacion" (gmail, codigo, fecha, usado) VALUES (%s, %s, NOW(), %s)',
                (gmail, codigo, False)
            )
            conn.commit()

            # Enviar el correo con el código de recuperación
            enviar_correo(gmail, codigo)

            flash('Correo enviado con éxito. Revisa tu correo para recuperar tu contraseña.')
            return redirect(url_for('Restablecer_Contrasena'))
        else:
            flash('El correo proporcionado no está registrado en nuestra base de datos.')
            return redirect(url_for('olvide_contraseña'))
    except Exception as e:
        conn.rollback()
        flash(f'Error al enviar el enlace: {e}')
        return redirect(url_for('olvide_contraseña'))
    finally:
        cur.close()
        conn.close()

@app.route('/cambiar_contrasena', methods=['POST'])
def cambiar_contrasena():
    codigo = request.form['codigo']
    nueva_contrasena = request.form['nueva_contrasena']
    confirmar = request.form['confirmar']

    if nueva_contrasena != confirmar:
        flash('Las contraseñas no coinciden.')
        return redirect(url_for('Restablecer_Contrasena'))

    # Encriptar la nueva contraseña
    hash_contrasena = generate_password_hash(nueva_contrasena)

    conn = get_connection()
    cur = conn.cursor()

    try:
        # Verificar si el código es válido y no ha sido usado
        cur.execute(
            'SELECT gmail FROM "Codigos_Recuperacion" WHERE codigo = %s AND usado = %s',
            (codigo, False)
        )
        resultado = cur.fetchone()

        if resultado:
            gmail = resultado[0]

            # Actualizar la contraseña del usuario
            cur.execute(
                'UPDATE "Registro_Usuario" SET contraseña = %s WHERE gmail = %s',
                (hash_contrasena, gmail)
            )

            # Marcar el código como usado
            cur.execute(
                'UPDATE "Codigos_Recuperacion" SET usado = %s WHERE codigo = %s',
                (True, codigo)
            )

            conn.commit()
            flash('Contraseña actualizada correctamente.')
            return redirect(url_for('login'))
        else:
            flash('El código es inválido o ya ha sido usado.')
            return redirect(url_for('Restablecer_Contrasena'))

    except Exception as e:
        conn.rollback()
        flash(f'Error al cambiar la contraseña: {e}')
        return redirect(url_for('Restablecer_Contrasena'))
    finally:
        cur.close()
        conn.close()

@app.route('/vuelve_login')
def vuelve_login():
    return render_template('login.html')

@app.route('/Restablecer_Contrasena')
def Restablecer_Contrasena():
    return render_template('Restablecer_Contrasena.html')

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    gmail = request.form['gmail']
    contrasena = request.form['contrasena']

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute('SELECT contraseña FROM "Registro_Usuario" WHERE gmail = %s', (gmail,))
        resultado = cur.fetchone()

        if resultado and check_password_hash(resultado[0], contrasena):
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('timbre'))
        else:
            flash('Correo o contraseña incorrectos.')
            return redirect(url_for('login'))

    except Exception as e:
        flash(f'Error al iniciar sesión: {e}')
        return redirect(url_for('login'))
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
