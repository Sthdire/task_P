import db_connect
from api import api_bp
from init import app

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    db_connect
    app.run(debug=True)





