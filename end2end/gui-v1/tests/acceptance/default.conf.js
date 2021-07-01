const env = require('./env.conf');

const config = {
    tests: './Scenarios/*_test.js',
    clearDb: false,
    output: './output',
    multiple: {
        parallel: {
            chunks: 1,
        },
    },
    helpers: {
        Puppeteer: {
            url: env.dojot_host,
            keepCookies: true,
            fullPageScreenshots: true,
            restart: false,
            keepBrowserState: true,
            show: true,
            waitForNavigation: ['networkidle2', 'domcontentloaded'],
            chrome: {
                    // '--lang=en-US,en' <-- Add (v2)
                args: ['--lang=en-US,en','--no-sandbox', '--start-maximized', '--start-fullscreen'],
                handleSIGTERM: false,
                handleSIGHUP: false,
                defaultViewport: {
                    width: 1280,
                    height: 720,
                },
            },
        },

        // add para gui v2
        MyHelper: {
            require: './getPageUr.js'
          },

        REST: {
            endpoint: env.dojot_host,

            //Para GUI v2
            endpoint: env.dojot_host_v2,
        },
    },
    include: {
        I: './steps_file.js',
        Commons: './PageObject/Common.js',
        Device: './PageObject/Device.js',
        Flow: './PageObject/Flow.js',
        Notification: './PageObject/Notification.js',
        Template: './PageObject/Template.js',
        User: './PageObject/User.js',
    },
    plugins: {
        allure: {},
        autoDelay: {
            enabled: true,
        },
        autoLogin: {
            enabled: true,
            saveToFile: false,
            inject: 'login',
            users: {
                admin: {
                    login: (I) => {
                        I.loginAdmin(I, config.clearDb);
                    },
                    check: (I) => {
                        I.amOnPage(`${env.dojot_host}/#/`);
                        I.see('admin');
                    },
                },
            },
        },
    },
    bootstrap: null,
    mocha: {},
    name: 'dojot-codecept',
};


module.exports = config;
