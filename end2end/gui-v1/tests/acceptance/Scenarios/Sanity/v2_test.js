const env = require ('../../env.conf')
const MyHelper = require ('../../getPageUr')
const config = require ('../../default.conf')
const v2 = require("../../PageObject/v2");

Feature ('v2 CRUD ')

Scenario('@v2: Login v1', async(I) => {
  I.amOnPage(env.dojot_host);
  I.loginAdmin(I, config.clearDb);
})

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
  'TEMP4',
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

  Template.addAttrTwo(
    'TEMP31',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP32',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP33',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP34',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP35',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP36',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP37',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP38',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP39',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP40',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP41',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP42',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP43',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP44',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );
  
  Template.addAttrTwo(
    'TEMP45',
    Template.AttributeType.dynamic,
    Template.AttributeValueType.integer
  );

  Template.clickSave();
  Template.seeTemplateHasCreated();
});

Scenario('@v2: Device integer', async (I, Device) => {
  Device.init(I);    
  Device.clickOpenDevicePage();
  Device.clickCreateNew();
  Device.fillNameDevice('Create Device v2')
  Device.clickAddOrRemoveTemplate();
  Device.clickToSelectTemplate('v2');
  Device.clickBack();
  Device.clickSave();
  I.wait(1)
  Device.checkExistCard('Create Device v2')
});

Scenario('@v2: Publish integer', async (I, Device) => {
  Device.init(I);
  Device.clickDetailsDeviceDefault();
  Device.clickDynamicAttributes('TEMP1');
  Device.clickDynamicAttributes('TEMP2');
  Device.clickDynamicAttributes('TEMP3');
  Device.clickDynamicAttributes('TEMP4');

  Device.clickDynamicAttributes('TEMP31');
  Device.clickDynamicAttributes('TEMP32');
  Device.clickDynamicAttributes('TEMP33');
  Device.clickDynamicAttributes('TEMP34');
  Device.clickDynamicAttributes('TEMP35');
  Device.clickDynamicAttributes('TEMP36');
  Device.clickDynamicAttributes('TEMP37');
  Device.clickDynamicAttributes('TEMP38');
  Device.clickDynamicAttributes('TEMP39');
  Device.clickDynamicAttributes('TEMP40');
  Device.clickDynamicAttributes('TEMP41');
  Device.clickDynamicAttributes('TEMP42');
  Device.clickDynamicAttributes('TEMP43');
  Device.clickDynamicAttributes('TEMP44');
  Device.clickDynamicAttributes('TEMP45');

  Device.clickDynamicAttributes('GEO');
  Device.clickDynamicAttributes('GEO2');


  const fullUrl = await I.getCurrentUrl()
  I.wait(1)
  const array1 = fullUrl.split("/device/id/");
  I.wait(1)
  const IdDevice = array1[1].replace("/detail",""); 
  I.wait(3)

  I.sendMQTTMessage(IdDevice, '{"TEMP1": "15"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP1": "22"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP1": "36"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP2": "10"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP2": "17"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP2": "30"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP3": "48"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP3": "44"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP3": "49"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP4": "58"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP4": "4"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP4": "40"}',)

  I.sendMQTTMessage(IdDevice, '{"TEMP31": "15"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP32": "22"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP33": "36"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP34": "10"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP35": "17"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP36": "30"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP37": "48"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP38": "44"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP39": "49"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP40": "58"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP41": "47"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP42": "40"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP43": "49"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP44": "58"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP45": "42"}',)

  I.sendMQTTMessage(IdDevice, '{"TEMP31": "55"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP32": "72"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP33": "66"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP34": "15"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP35": "18"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP36": "26"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP37": "38"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP38": "14"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP39": "9"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP40": "8"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP41": "7"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP42": "60"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP43": "9"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP44": "14"}',)
  I.sendMQTTMessage(IdDevice, '{"TEMP45": "42"}',)

  I.sendMQTTMessage(IdDevice, '{"GEO": "-22.740490, -47.437186"}',)
  I.sendMQTTMessage(IdDevice, '{"GEO2": "-22.738734, -47.424335"}',)
  I.wait(5)
})

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

Scenario('@v2: ADD Line Chart - Real Time (Last 15)', async(I, v2)  => {
  v2.addWidget()
  v2.selectLineChart('Line Chart', 'Teste')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1', '[Create Device v2] TEMP2') 
  v2.selectDevice('[Create Device v2] TEMP2')            
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})

Scenario('@v2: Checking Line Chart', async(I, v2)  => {
  v2.checkingElement('Line Chart')
})

Scenario('@v2: Editing Line Chart', async(I, v2) => {
  v2.selectSettings()
  v2.clickEdit()
  v2.editWidget('Editing - Test Line Chart', 'Teste DOJOT')
  v2.clickNext()
  v2.clickNext()
  v2.uncheckDevice('[Create Device v2] TEMP2')
  v2.selectDevice('[Create Device v2] TEMP3')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
  v2.checkingElement('Test Line Chart')
})

Scenario('@v2: Checking editing Line Chart', async(I, v2) => {
  v2.checkingElement('Editing - Test Line Chart')
})

Scenario('@v2: Delete Line Chart', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Area Chart', async(I, v2) => {
  v2.addWidget()
  v2.selectAreaChart('Area Chart', 'Teste')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1', '[Create Device v2] TEMP2')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})

Scenario('@v2: Checking Area Chart', async(I, v2) => {
  v2.checkingElement('Area Chart')
})

Scenario('@v2: Editing Area Chart', async(I, v2) => {
  v2.selectSettings()
  v2.clickEdit()
  v2.editWidget('Editing - Test Area Chart', 'Teste DOJOT')
  v2.clickNext()
  v2.clickNext()
  v2.uncheckDevice('[Create Device v2] TEMP2')
  v2.selectAttribute('[Create Device v2] TEMP3')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
  
})

Scenario('@v2: Checking editing Area Chart', async(I, v2) => {
  v2.checkingElement('Test Area Chart')
})

Scenario('@v2: Delete Area Chart', async(I) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Bar Chart', async(I, v2) => {
  v2.addWidget()
  v2.selectBarChart('Bar Chart', 'Teste')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1', '[Create Device v2] TEMP2');
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})

Scenario('@v2: Checking Bar Chart', async(I, v2) => {
    v2.checkingElement('Bar Chart')
})

Scenario('@v2: Editing Bar Chart', async(I, v2) => {
  v2.selectSettings()
  v2.clickEdit('Edit')
  v2.editWidget('Editing - Test Bar Chart', 'Teste DOJOT')
  v2.clickNext()
  v2.clickNext()
  v2.uncheckDevice('[Create Device v2] TEMP2')
  v2.selectAttribute('[Create Device v2] TEMP3')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})

Scenario('@v2: Checking editing Bar Chart', async(I, v2) => {
  v2.checkingElement('Editing - Test Bar Chart')
})

Scenario('@v2: Delete Bar Chart', async(I) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Table', async(I, v2) => {
  v2.addWidget()
  v2.selectTable('Table', 'Teste')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1', '[Create Device v2] TEMP2', '[Create Device v2] TEMP3')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})

Scenario('@v2: Checking Table', async(I, v2) => {
  v2.checkingElement('Table')
})

Scenario('@v2: Editing Table', async(I, v2) => {
  v2.selectSettings()
  v2.clickEdit()
  v2.editWidget('Editing - Test Table', 'Teste DOJOT')
  v2.clickNext()
  v2.clickNext()
  v2.uncheckDevice('[Create Device v2] TEMP2')
  v2.selectAttribute('[Create Device v2] TEMP3', '[Create Device v2] GEO2', '[Create Device v2] GEO')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})  
  
Scenario('@v2: Checking editing Table', async(I, v2) => { 
  v2.checkingElement('Test Table')
})

Scenario('@v2: Delete Table', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Map', async(I, v2) => {
  v2.addWidget()
  v2.selectMap('MapGeo', 'Teste')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] GEO')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})

Scenario('@v2: Checking Map', async(I, v2) => {
  v2.checkingElement('MapGeo')
})

Scenario('@v2: Editing MAP', async(I) => {
  v2.selectSettings()
  v2.clickEdit()
  v2.editWidget('Editing - Test MAP', 'Teste MAP DOJOT')
  v2.clickNext()
  v2.clickNext()
  v2.uncheckDevice('[Create Device v2] GEO')
  v2.selectAttribute('[Create Device v2] GEO2')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
})

Scenario('@v2: Checking editing Map', async(I, v2) => {
  v2.checkingElement('Editing - Test MAP')
})

Scenario('@v2: Zoom MAP', async(I, v2) => {
  v2.zoomMapOut()
  v2.zoomMapIn()
})

Scenario('@v2: Delete Map', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})

//Other settings 

Scenario('@v2: ADD Line Chart 2 - Real Time (Last minutes)', async(I, v2)  => {
  v2.addWidget()
  v2.selectLineChart('Line Chart 2', 'Last minutes')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1')
  v2.selectAttribute('[Create Device v2] TEMP2')
  v2.selectAttribute('[Create Device v2] TEMP3')
  v2.selectAttribute('[Create Device v2] TEMP31')
  v2.selectAttribute('[Create Device v2] TEMP32')
  v2.selectAttribute('[Create Device v2] TEMP33')
  v2.selectAttribute('[Create Device v2] TEMP34')
  v2.selectAttribute('[Create Device v2] TEMP35')
  v2.clickNext()
  v2.selectSettingsHistoric('1')
  v2.clickNext()
  v2.clickFinish()
  I.wait(3)
})

Scenario('@v2: Checking Line Chart 2', async(I, v2) => {
  v2.checkingElement('Line Chart 2')
})

Scenario('@v2: Delete Line Chart 2', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Line Chart 3 - Real Time (Last hours)', async(I, v2)  => {
  v2.addWidget()
  v2.selectLineChart('Line Chart 3', 'Last hours')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1')
  v2.selectAttribute('[Create Device v2] TEMP2')
  v2.selectAttribute('[Create Device v2] TEMP3')
  v2.selectAttribute('[Create Device v2] TEMP31')
  v2.selectAttribute('[Create Device v2] TEMP32')
  v2.selectAttribute('[Create Device v2] TEMP33')
  v2.selectAttribute('[Create Device v2] TEMP34')
  v2.selectAttribute('[Create Device v2] TEMP35')
  v2.selectAttribute('[Create Device v2] TEMP45')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
  I.wait(3)
})

Scenario('@v2: Checking Line Chart 3', async(I, v2) => {
  v2.checkingElement('Line Chart 3')
})

Scenario('@v2: Delete Line Chart 3', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Line Chart 4 - Real Time (Last days)', async(I, v2)  => {
  v2.addWidget()
  v2.selectLineChart('Line Chart 4', 'Last days')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1')
  v2.selectAttribute('[Create Device v2] TEMP2')
  v2.selectAttribute('[Create Device v2] TEMP3')
  v2.selectAttribute('[Create Device v2] TEMP31')
  v2.selectAttribute('[Create Device v2] TEMP32')
  v2.selectAttribute('[Create Device v2] TEMP33')
  v2.selectAttribute('[Create Device v2] TEMP34')
  v2.selectAttribute('[Create Device v2] TEMP35')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
  I.wait(3)
})

Scenario('@v2: Checking Line Chart 4', async(I, v2) => {
  v2.checkingElement('Line Chart 4')
})

Scenario('@v2: Delete Line Chart 4', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Line Chart 5 - Real Time (Last months)', async(I, v2)  => {
  v2.addWidget()
  v2.selectLineChart('Line Chart 5', 'Last months')
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.clickNextPage()
  v2.selectAttribute('[Create Device v2] TEMP36')
  v2.selectAttribute('[Create Device v2] TEMP4')
  v2.selectAttribute('[Create Device v2] TEMP37')
  v2.selectAttribute('[Create Device v2] TEMP38')
  v2.selectAttribute('[Create Device v2] TEMP39')
  v2.selectAttribute('[Create Device v2] TEMP40')
  v2.selectAttribute('[Create Device v2] TEMP41')
  v2.selectAttribute('[Create Device v2] TEMP42')
  v2.selectAttribute('[Create Device v2] TEMP43')
  v2.selectAttribute('[Create Device v2] TEMP44')
  v2.clickNextPage()
  v2.selectAttribute('[Create Device v2] TEMP45')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
  I.wait(3)
})

Scenario('@v2: Checking Line Chart 5', async(I, v2) => {
  v2.checkingElement('Line Chart 5')
})

Scenario('@v2: Delete Line Chart 5', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})

Scenario('@v2: ADD Line Chart 6 - Real Time (Initial Data)', async(I, v2)  => {
  v2.addWidget()
  v2.selectLineChart('Line Chart 6', 'Initial Data')
  pause()
  v2.clickNext()
  v2.selectDevice('Create Device v2')
  v2.clickNext()
  v2.selectAttribute('[Create Device v2] TEMP1')
  v2.selectAttribute('[Create Device v2] TEMP2')
  v2.selectAttribute('[Create Device v2] TEMP3')
  v2.selectAttribute('[Create Device v2] TEMP31')
  v2.selectAttribute('[Create Device v2] TEMP32')
  v2.selectAttribute('[Create Device v2] TEMP33')
  v2.selectAttribute('[Create Device v2] TEMP34')
  v2.selectAttribute('[Create Device v2] TEMP35')
  v2.clickNext()
  v2.clickNext()
  v2.clickFinish()
  I.wait(3)
})

Scenario('@v2: Checking Line Chart 5', async(I, v2) => {
  v2.checkingElement('Line Chart 5')
})

Scenario('@v2: Delete Line Chart 5', async(I, v2) => {
  v2.selectSettings()
  v2.deleteWidget()
})












