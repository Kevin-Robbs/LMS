from flaskApp.routeEngine import router
import sys
sys.dont_write_bytecode = True

if __name__ == "__main__":
    router.app.run(debug=True)