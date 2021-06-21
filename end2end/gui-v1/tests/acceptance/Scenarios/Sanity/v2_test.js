const env = require ('../../env.conf')
const MyHelper = require ('../../getPageUr')
const config = require ('../../default.conf')

Feature ('v2 CRUD ')

//OK
Scenario('@v2: Login v1', async(I) => {
  I.amOnPage(env.dojot_host);
  I.loginAdmin(I, config.clearDb);
})

//OK 
Scenario('@v2: Template', async (I, Template) => {
Template.init(I);
Template.clickOpenTemplatePage();
Template.clickCreateNew();
Template.fillNameTemplate('v2');

//Template.addAttr(
    Template.addAttrTwo(
    'TEMP1',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
);

Template.addAttrTwo(
  'TEMP2',
  Template.AttributeType.dynamic,
  Template.AttributeValueType.integer
);

Template.addAttrTwo(
  'TEMP3',
  Template.AttributeType.dynamic,
  Template.AttributeValueType.integer
);

Template.addAttrTwo(
  'GEO',
  Template.AttributeType.dynamic,
  Template.AttributeValueType.geo
);

Template.addAttrTwo(
  'GEO2',
  Template.AttributeType.dynamic,
  Template.AttributeValueType.geo
);

Template.clickSave();
Template.seeTemplateHasCreated();
});

//OK
Scenario('@v2: Device integer', async (I, Device) => {
  Device.init(I);    
  Device.clickOpenDevicePage();
  Device.clickCreateNew();
  Device.fillNameDevice('Create Device v2')
  Device.clickAddOrRemoveTemplate();
  Device.clickToSelectTemplate('v2');
  Device.clickBack();
  Device.clickSave();
  //Device.checkExistCard('Create Device v2')
});

//OK
Scenario('@v2: Publish integer', async (I, Device) => {
  Device.init(I);
  Device.checkExistCard('Create Device v2');
  Device.clickDetailsDeviceDefault();
  Device.clickDynamicAttributes('TEMP1');
  Device.clickDynamicAttributes('TEMP2');
  Device.clickDynamicAttributes('TEMP3');
  Device.clickDynamicAttributes('GEO');
  Device.clickDynamicAttributes('GEO2');

  const fullUrl = await I.getCurrentUrl()
  const array1 = fullUrl.split("/device/id/");
  const IdDevice = array1[1].replace("/detail",""); 

  I.sendMQTTMessage(IdDevice, '{"TEMP1": "10"}',)
  I.wait(2)
})

//OK
Scenario('@v2: Publish integer 2', async (I, Device) => {
  const fullUrl = await I.getCurrentUrl()
  const array1 = fullUrl.split("/device/id/");
  const IdDevice = array1[1].replace("/detail",""); 

  I.sendMQTTMessage(IdDevice, '{"TEMP1": "15"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP1": "22"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP1": "36"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP2": "10"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP2": "17"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP2": "30"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP3": "48"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP3": "44"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP3": "49"}',)
  I.sendMQTTMessage(IdDevice, '{"GEO": "-22.740490, -47.437186"}',)
  I.sendMQTTMessage(IdDevice, '{"GEO2": "-22.738734, -47.424335"}',)
  I.wait(5)
})

//OK
Scenario('@v2: Login v2', async(I) => {
  await I.setEn()
  I.amOnPage(env.dojot_host_v2);
  I.refreshPage();
  I.wait(3);
  I.fillField('user', 'admin')
  I.fillField('password', 'admin')
  I.click('.MuiButtonBase-root')
  I.wait(3)
})

Scenario('@v2: ADD Line Chart', async(I)  => {
  I.click('.MuiButton-root')
  I.wait(1)
  I.click('Line Chart')
  I.fillField('general.name', 'Line Chart')
  I.fillField('general.description', 'Teste');
  I.click('Next')
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('Create Device v2')));
  I.click('Next')
  I.wait(1)
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP1')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  //I.click('Select color')
  //Subtitle I.fillField(locate('input').withAttr({ value: "teste" }))
  I.click('Next')
  I.wait(3)
  I.click('Next')
  I.wait(3)
  I.click('Finish')
  I.wait(4)
})

Scenario('@v2: Edit Line Chart', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Edit'));
  I.wait(3)
  I.fillField('general.name', '')
  I.fillField('general.name', 'Editing - Test Line Chart')
  I.fillField('general.description', '');
  I.fillField('general.description', 'Teste DOJOT');
  I.wait(3)
  I.click('Next')
  I.click('Next')
  I.uncheckOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  I.wait(2)
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP3')));
  I.wait(2)
  I.click('Next')
  I.wait(3)
  I.click('Next')
  I.wait(3)
  I.click('Finish')
  I.seeElement(locate('div').find('.MuiTypography-root').withText('Test Line Chart'))
  I.wait(4)
})

Scenario('@v2: Delete Line Chart', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Delete'));
  I.wait(4)
})

Scenario('@v2: ADD Area Chart', async(I) => {
  I.click('.MuiButton-root')
  I.wait(1)
  I.click('Area Chart')
  I.fillField('general.name', 'Area Chart')
  I.fillField('general.description', 'Teste');
  I.click('Next')
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('Create Device v2')));
  I.click('Next')
  I.wait(1)
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP1')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  I.click('Next')
  I.wait(3)
  I.click('Next')
  I.wait(3)
  I.click('Finish')
  I.wait(4)
})

Scenario('@v2: Edit Area Chart', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Edit'));
  I.fillField('general.name', '')
  I.fillField('general.name', 'Editing - Test Area Chart')
  I.fillField('general.description', '');
  I.fillField('general.description', 'Teste DOJOT');
  I.wait(3)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.uncheckOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP3')));
  I.wait(3)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.click('Finish')
  I.seeElement(locate('div').find('.MuiTypography-root').withText('Test Area Chart'))
  I.wait(4)
})

Scenario('@v2: Delete Area Chart', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Delete'));
  I.wait(4)
})

Scenario('@v2: ADD Bar Chart', async(I) => {
  I.click('.MuiButton-root')
  I.wait(1)
  I.click('Bar Chart')
  I.fillField('general.name', 'Bar Chart')
  I.fillField('general.description', 'Teste');
  I.click('Next')
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('Create Device v2')));
  I.click('Next')
  I.wait(1)
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP1')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  I.click('Next')
  I.wait(3)
  I.click('Next')
  I.wait(3)
  I.click('Finish')
  I.wait(4)
})

Scenario('@v2: Edit Bar Chart', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Edit'));
  I.wait(2)
  I.fillField('general.name', '')
  I.fillField('general.name', 'Editing - Test Bar Chart')
  I.fillField('general.description', '');
  I.fillField('general.description', 'Teste DOJOT');
  I.wait(3)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.uncheckOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP3')));
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.click('Finish')
  I.seeElement(locate('div').find('.MuiTypography-root').withText('Test Bar Chart'))
  I.wait(4)
})

Scenario('@v2: Delete Bar Chart', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Delete'));
  I.wait(4)
})

Scenario('@v2: ADD Table', async(I) => {
  I.click('.MuiButton-root')
  I.wait(1)
  I.click('Table')
  I.fillField('general.name', 'Table')
  I.fillField('general.description', 'Teste');
  I.click('Next')
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('Create Device v2')));
  I.click('Next')
  I.wait(1)
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP1')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP3')));
  I.click('Next')
  I.wait(3)
  I.click('Next')
  I.wait(3)
  I.click('Finish')
  I.wait(4)
})

Scenario('@v2: Edit Table', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Edit'));
  I.wait(2)
  I.fillField('general.name', '')
  I.fillField('general.name', 'Editing - Test Table')
  I.fillField('general.description', '');
  I.fillField('general.description', 'Teste DOJOT');
  I.wait(3)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.uncheckOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP2')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] TEMP3')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] GEO2')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] GEO')));
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.click('Finish')
  I.seeElement(locate('div').find('.MuiTypography-root').withText('Test Table'))
  I.wait(4)
})

Scenario('@v2: Delete Table', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Delete'));
  I.wait(4)
})

Scenario('@v2: ADD Map', async(I) => {
  I.click('.MuiButton-root')
  I.wait(1)
  I.click('Map')
  I.fillField('general.name', 'MapGeo')
  I.fillField('general.description', 'Teste');
  I.click('Next')
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('Create Device v2')));
  I.click('Next')
  I.wait(1)
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] GEO')));
  I.click('Next')
  I.wait(3)
  I.click('Next')
  I.wait(3)
  I.click('Finish')
  I.wait(4)
})

Scenario('@v2: Edit MAP', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Edit'));
  I.wait(2)
  I.fillField('general.name', '')
  I.fillField('general.name', 'Editing - Test MAP')
  I.fillField('general.description', '');
  I.fillField('general.description', 'Teste MAP DOJOT');
  I.wait(3)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.uncheckOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] GEO')));
  I.checkOption(locate('input').withAttr({ type: "checkbox" }).inside(locate('.MuiListItem-root  span').withText('[Create Device v2] GEO2')));
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.click('Next')
  I.wait(2)
  I.click('Finish')
  I.seeElement(locate('div').find('.MuiTypography-root').withText('Test MAP'))
  I.wait(4)
})

Scenario('@v2: Zoom MAP', async(I) => {
  I.click(".leaflet-control-zoom-out")
  I.wait(2)
  I.click(".leaflet-control-zoom-out")
  I.wait(2)
  I.click(".leaflet-control-zoom-out")
  I.wait(2)
  I.click(".leaflet-control-zoom-in")
  I.wait(2)
  I.click(".leaflet-control-zoom-in")
  I.wait(2)
  I.click(".leaflet-control-zoom-in")
  
})

Scenario('@v2: Delete Line Chart', async(I) => {
  I.click('settings')
  I.click(locate('div').find('.MuiListItemText-root').withText('Delete'));
})

