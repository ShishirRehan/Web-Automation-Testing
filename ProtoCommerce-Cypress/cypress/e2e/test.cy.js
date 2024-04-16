///<reference types="Cypress"/>
import  HomePage  from "../pageObject/homePage";
import ShopPage from "../pageObject/shopPage";

describe("Testing Protocommerce", ()=>{
  let userData;
  beforeEach("Execute before all tests", ()=>{
    cy.fixture("example.json").then((data)=>{
      userData = data
    })
    cy.visit("https://rahulshettyacademy.com/angularpractice/");
  })

  it("Testing home page and all it's component", ()=>{
    const home = new HomePage();
    home.getNameBox().should("be.visible").type(userData.name).and("have.value", userData.name);
    home.getEmailBox().should("be.visible").type(userData.email).and("have.value", userData.email);
    home.getTwoWayBinding().should("be.visible").and("have.value", userData.name);
    home.getPasswordBox().should("be.visible").type(userData.password);
    home.getIceCreamCheck().check().and("be.checked");
    home.getGenderSelect().select(userData.gender).and("have.value", userData.gender);
    home.getEntrepreneur().should("be.disabled");
    home.getDobBox().should("be.visible").type(userData.dob).and("have.value", userData.dob);
  })

  it("Testing shop and all it's component", ()=>{
    const shop = new ShopPage();

    shop.getShopBtn().should("be.visible").click();
    cy.getProduct("Nokia Edge");
    cy.getProduct("Blackberry");
    shop.getCheckoutBtn().should("be.visible").click();
    shop.getCheckOut().should("be.visible").click();
    shop.getSelectCountry().should("be.visible").type("ban")
    cy.wait(7000)
    shop.getCountrySuggestion().each(($ele, index, $list)=>{
      if($ele.text()==="Bangladesh"){
        cy.wrap($ele).click()
      }
    })
    shop.getSelectCountry().should("have.value", "Bangladesh");
    shop.getCheckBox().should("be.visible").click();
    shop.getSubmitBtn().should("be.visible").click();
    shop.getAlert().then((ele)=>{
      expect(ele.text()).to.includes("Thank you! Your order will be delivered in next few weeks");
    })

    shop.getCloseBtn().should("be.visible").click();

  })
})