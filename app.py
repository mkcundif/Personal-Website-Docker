from flask import Flask, render_template, request, redirect, url_for, flash
import os
from DAL import init_db, fetch_projects, insert_project

# Serve static files (css/, images/, assets/) from the project root so existing
# folders do not need to be moved into a `static/` directory.
# static_folder='.' tells Flask to serve files from the repository root.
# static_url_path='' maps static files to the site root (so `/css/styles.css` works).
app = Flask(__name__, static_folder='.', static_url_path='')
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key')

# Ensure database exists on startup
init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    projects = fetch_projects()
    return render_template('projects.html', projects=projects)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        image_file_name = request.form.get('image_file_name', '').strip()

        if not title or not description or not image_file_name:
            flash('All fields are required: Title, Description, Image File Name.')
            return render_template('contact.html')

        # Only store the filename; user should place file in images/ folder
        insert_project(title=title, description=description, image_file_name=image_file_name)
        return redirect(url_for('projects'))
    return render_template('contact.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    # Use 127.0.0.1 and port 5000 by default; set debug=True for development
    app.run(host='127.0.0.1', port=5000, debug=True)
