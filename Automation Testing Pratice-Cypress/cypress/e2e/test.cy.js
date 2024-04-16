require ("@4tw/cypress-drag-drop");
// import "cypress-iframe";
import {TextBox, Radio, Checkbox, Select, Table, Search, Alerts, DoubleClick, DragnDrop, Slide} from "../PageObject/automation";

describe("Automation Testing Practice", ()=>{
  // beforeEach("Load page", ()=>{
  //   cy.visit("https://testautomationpractice.blogspot.com/");
  // })

  it("Testing Textboxes", ()=>{
    const textbox = new TextBox();

    textbox.inputName("Shishir");
    textbox.inputEmail("shishir@email.com");
    textbox.inputPhone("0123456789");
    textbox.inputAddress("Daulatpur, Kushtia, Khulna, Bangladesh");
  })

  it("Testing Radio Buttons", ()=>{
    const radioButton = new Radio();

    radioButton.selectMale();
    radioButton.selectFemale();
  })

  it("Testing Checkboxes",()=>{
    const checkboxes = new Checkbox();

    checkboxes.checkSunday();
    checkboxes.checkMonday();
    checkboxes.checkTuesday();
    checkboxes.checkWednesday();
    checkboxes.checkThursday();
    checkboxes.checkFriday();
    checkboxes.checkSaturday();
  })

  it("Testing Dropdowns", ()=>{
    const select = new Select();

    select.selectCountry("India");
    select.selectColor("Green");
  })


  it.only("Reading Table", ()=>{
    cy.visit("https://testautomationpractice.blogspot.com/");


    const table = new Table();

    table.readingTable();
  })

  it("Testing searchbox", ()=>{
    const search = new Search();
    search.searching("cypress");
  })

  it("Testing Alert Windows", ()=>{
    const alerts = new Alerts();

    alerts.alertWindow();
    alerts.confirmWindow();
    alerts.prompWindow("Shishir");
  })

  it("Double click Operation", ()=>{
    const doubleclick = new DoubleClick();

    doubleclick.doubleClick();
  })

  it("Drag and Drop Operation", ()=>{
    const dragndrop = new DragnDrop();
    dragndrop.dragOperation();
  })

  it("Testing slider", ()=>{
    const slide = new Slide();

    slide.slideOperation();
  })


})