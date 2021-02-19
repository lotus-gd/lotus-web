const chalk = require("chalk");

const CLR = {
    LOG: "#00AAFF",
    WRN: "#FFC400",
    ERR: "#FF0040",
    INF: "#00FF7F",
    DEB: "#808080"
}

class Logger {
    static log(message, title = "LOG", clr = CLR.LOG) {
        return console.log(`${chalk.bgHex(clr).hex("#000")(` ${new Date().toUTCString()} ${chalk.bold(title)} `)} ${message}`)
    }

    static info(message) {
        return Logger.log(message, "INFO", CLR.INF)
    }

    static error(message) {
        return Logger.log(message, "ERROR", CLR.ERR)
    }

    static warn(message) {
        return Logger.log(message, "WARN", CLR.WRN)
    }

    static debug(message) {
        return Logger.log(message, "DEBUG", CLR.DEB)
    }

    static empty() {
        return console.log("")
    }
}

module.exports = Logger;