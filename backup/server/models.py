from flask import Flask
app = Flask(__name__)

if __name__ =="__main__":
    app.logger.info("test")
    app.logger.debug("debug test")
    app.logger.error("error test")
    app.run