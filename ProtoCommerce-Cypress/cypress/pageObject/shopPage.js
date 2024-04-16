class ShopPage{
    getShopBtn(){
        return cy.get(".navbar-nav li:nth-child(2)");
    }

    getProduct(){
        return cy.get(".card-title a");
    }

    getCheckoutBtn(){
        return cy.get("#navbarResponsive ul li a");
    }

    getCheckOut(){
        return cy.contains("Checkout");
    }

    getSelectCountry(){
        return cy.get("#country");
    }

    getCountrySuggestion(){
        return cy.get(".suggestions ul li a");
    }

    getCheckBox(){
        return cy.get("div.checkbox");
    }

    getSubmitBtn(){
        return cy.get("input[type='submit']");
    }

    getAlert(){
        return cy.get("div.alert");
    }

    getCloseBtn(){
        return cy.get("a.close");
    }
}

export default ShopPage