from flask import Flask, render_template, request, jsonify, redirect
from configurations import db, SECRET_KEY
from datetime import datetime


app = Flask(__name__, template_folder='web_pages', static_folder='static_files')
app.secret_key = SECRET_KEY

def add_audit_log(lead_id, admin_id, action):
    try:
        if admin_id is None:
            admin_id = 0
            
        db.insert(
            "INSERT INTO audit_log (lead_id, admin_id, action, timestamp) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
            (lead_id, admin_id, action)
        )
        print(f"Audit log: {action} on lead {lead_id} by admin {admin_id}")
        return True
    except Exception as e:
        print(f"Audit log error: {e}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact-form')
def contact_form():
    return render_template('contact_form.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/logout')
def logout():
    return redirect('/')

@app.route('/api/admin-login', methods=['POST'])
def admin_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    admin = db.get_single_data(
        "SELECT * FROM admin_users WHERE username = ? AND password_hash = ?",
        (username, password)
    )
    
    if admin:
        return jsonify({
            'success': True,
            'token': 'admin-token-' + str(admin['admin_id']),
            'admin_id': admin['admin_id']
        })
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})
    
@app.route('/api/submit-lead', methods=['POST'])
def submit_lead():
    data = request.json
    
    lead_id = db.insert(
        "INSERT INTO leads (company_name, contact_name, email, phone, message, source) VALUES (?, ?, ?, ?, ?, ?)",
        (data['company_name'], data['contact_name'], data['email'], data['phone'], data['message'], data['source'])
    )
    
    add_audit_log(lead_id, 0, 'CREATE')
    
    return jsonify({'success': True, 'lead_id': lead_id})

@app.route('/api/get-lead/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    lead = db.get_single_data(
        "SELECT * FROM leads WHERE lead_id = ?",
        (lead_id,)
    )
    
    if lead:
        return jsonify({'success': True, 'lead': lead})
    else:
        return jsonify({'success': False, 'message': f'Lead with ID {lead_id} not found'})

@app.route('/api/get-leads', methods=['GET'])
def get_leads():
    leads = db.get_data("SELECT * FROM leads ORDER BY created_at DESC")
    return jsonify({'leads': leads})

@app.route('/api/delete-lead/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    admin_id = request.headers.get('X-Admin-ID', 0)
    
    add_audit_log(lead_id, admin_id, 'DELETE')
    
    affected_rows = db.delete(
        "DELETE FROM leads WHERE lead_id = ?",
        (lead_id,)
    )
    
    if affected_rows > 0:
        return jsonify({'success': True, 'message': 'Lead deleted'})
    else:
        return jsonify({'success': False, 'message': f'Lead with ID {lead_id} not found'})
    
@app.route('/api/update-lead/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    data = request.json
    admin_id = request.headers.get('X-Admin-ID', 0)
    
    affected_rows = db.update(
        "UPDATE leads SET company_name = ?, contact_name = ?, email = ?, phone = ?, message = ? WHERE lead_id = ?",
        (data['company_name'], data['contact_name'], data['email'], data['phone'], data['message'], lead_id)
    )
    
    if affected_rows > 0:
        add_audit_log(lead_id, admin_id, 'UPDATE')
        return jsonify({'success': True, 'message': 'Lead updated'})
    else:
        return jsonify({'success': False, 'message': f'Lead with ID {lead_id} not found'})

@app.route('/api/get-audit-logs', methods=['GET'])
def get_audit_logs():
    logs = db.get_data("SELECT * FROM audit_log ORDER BY timestamp DESC")
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True, port=5000)