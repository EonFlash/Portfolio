from flask_frozen import Freezer
from app import app

# optional: configure destination
app.config['FREEZER_DESTINATION'] = 'build'
# optional: if your site will be served from a sub-path:
# app.config['FREEZER_BASE_URL'] = 'https://username.github.io/repo-name/'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
