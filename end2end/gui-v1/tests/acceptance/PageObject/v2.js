let I = actor();
const Util = require('../Utils');

module.exports = {

    addWidget(){
        I.click('.MuiButton-root')
        I.wait(1)
    },

    selectLineChart(name, description){
        I.click('Line Chart') 
        I.fillField('general.name', name)
        I.fillField('general.description', description);
    }, 

    selectAreaChart(name, description){
        I.click('Area Chart')
        I.fillField('general.name', name)
        I.fillField('general.description', description);
    },

    selectBarChart(name, description){
        I.click('Bar Chart')
        I.fillField('general.name', name)
        I.fillField('general.description', description);
    },

    selectTable(name, description){
        I.click('Table')
        I.fillField('general.name', name)
        I.fillField('general.description', description);
    },

    selectMap(name, description){
        I.click('Map')
        I.fillField('general.name', name)
        I.fillField('general.description', description);
    },

    // setColor(){
    //     I.click('Select color')
    // },

    // subtitleText(name){
    //     I.fillField('text', name)
    // },

    editWidget(name, description){
        I.fillField('general.name', '')
        I.fillField('general.name', name)
        I.fillField('general.description', '');
        I.fillField('general.description', description);
        I.wait(3)
    },

    selectDevice(name, name2){
        I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText(name, name2))); 
        I.wait(2)
    },

    selectAttribute(selectAttribute1, selectAtrribute2, selectAtrribute3){
        I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText(selectAttribute1, selectAtrribute2, selectAtrribute3)));
        I.wait(1)
    },

    clickNextPage(){
        I.click('Go to next page')
        I.wait(1)
        I.click('Go to next page')
        I.wait(2)
    },

    selectSettingsHistoric(number){
        I.checkOption(number)
    },

    selectPage(number){
        I.click('.MuiPaginationItem-root', number)
    },

    // for device and attribute
    uncheckDevice(deviceName){
        I.uncheckOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText(deviceName)));
        I.wait(2)
    },

    selectSettings(){
        I.click('settings')
    },

    clickEdit(){
        I.click(locate('div').find('.MuiListItemText-root').withText('Edit'));
        I.wait(3)
    },

    checkingElement(name){
        I.seeElement(locate('div').find('.MuiTypography-root').withText(name))
        I.wait(4)
    },

    deleteWidget(){
        I.click(locate('div').find('.MuiListItemText-root').withText('Delete'));
        I.wait(3)
    },

    clickNext(){
        I.click('Next')
        I.wait(3)
    },

    clickFinish(){
        I.click('Finish')
    },

    clickRefreschPage(){
        I.refreschPage()
        I.wait(4)
    },

    zoomMapOut(){
        I.click(".leaflet-control-zoom-out")
        I.wait(2)
        I.click(".leaflet-control-zoom-out")
        I.wait(2)
        I.click(".leaflet-control-zoom-out")
        I.wait(2)
    },

    zoomMapIn(){
        I.click(".leaflet-control-zoom-in")
        I.wait(2)
        I.click(".leaflet-control-zoom-in")
        I.wait(2)
        I.click(".leaflet-control-zoom-in")
    },

};