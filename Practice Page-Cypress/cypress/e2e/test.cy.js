import "cypress-iframe"
import { Radio, SuggestiveDrpDwn, Dropdown, Alerts, Display, Table } from "../PageObject/practicePage"


describe("Testing Practice Page", ()=>{
  beforeEach("Load Practice Page", ()=>{
    cy.visit("https://rahulshettyacademy.com/AutomationPractice/")
  })
  it("Testing Radio Buttons", ()=>{
    const radio = new Radio();

    radio.selectRadio();
  })

  it("Testing auto suggestive drop down", ()=>{
    const drpDown = new SuggestiveDrpDwn();

    drpDown.autoSuggestive("Bangladesh");
  })
  
  it("Testing drop down", ()=>{
    const dropdown = new Dropdown();

    dropdown.dropdownOp("option2");
  })



  it("Testing alerts", ()=>{
    const alerts = new Alerts();

    alerts.alert("Shishir");
    alerts.confirm("Rehan");
  })

  it("Display elements", ()=>{
    const display = new Display();

    display.displayExample();
  })

  it("Reading table data", ()=>{
    const table = new Table();

    table.tableData();
  })

})