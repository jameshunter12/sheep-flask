from flask_cors import CORS
from sheep_api import app, db

from sheep_api.api.nhl import player_bp
from sheep_api.api.user import user_bp

from sheep_api.model.player import init_players
from sheep_api.model.username import init_users

app.register_blueprint(player_bp)
app.register_blueprint(user_bp)

def init_db():
    with app.app_context():
        db.create_all()
        init_players()
        init_users()

if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8067")
