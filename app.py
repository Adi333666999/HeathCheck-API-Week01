from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "1.0.0"

@app.route('/health', methods=['GET'])
def get_health():
	"""
	Returns the health status of the application.
	"""
	payload = {
		"status": "healthy",
		"description": "Application is running normally."
	}
	return jsonify(payload), 200

@app.route('/version', methods=['GET'])
def get_version():
	"""
	Returns the current version of application.
	"""
	payload = {
		"version": APP_VERSION
	}
	return jsonify(payload), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
