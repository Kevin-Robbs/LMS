from flaskApp.routeEngine.router import app
import sys
sys.dont_write_bytecode = True

if __name__ == "__main__":
    app.run(debug=True)