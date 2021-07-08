
// 'use strict';

let Helper = codecept_helper;

class MyHelper extends Helper {
  async getCurrentUrl() {
    const helper = this.helpers['Puppeteer'];
    return helper.page.url();
  }

  // teste de linguagem (Mari)
  async setEn() {
    const page = this.helpers['Puppeteer'].page;
 // await page.setExtraHTTPHeaders({
 //    'Accept-Language': 'en'
 // });
  await page.evaluateOnNewDocument(() => {
    Object.defineProperty(navigator, "language", {
        get: function() {
            return "en-US";
        }
    });
    Object.defineProperty(navigator, "languages", {
        get: function() {
            return ["en-US", "en"];
        }
    });
});
  }
}

module.exports = MyHelper;