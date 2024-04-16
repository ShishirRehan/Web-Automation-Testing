class HomePage{
    getNameBox(){
        return cy.get("input[name='name']:nth-child(2)");
    }

    getEmailBox(){
        return cy.get("input[name='email']");
    }

    getTwoWayBinding(){
        return cy.get("input[name='name']:nth-child(1)");
    }

    getPasswordBox(){
        return cy.get("input[type='password']");
    }

    getIceCreamCheck(){
        return cy.get("#exampleCheck1").should("be.visible");
    }

    getGenderSelect(){
        return cy.get("#exampleFormControlSelect1").should("be.visible");
    }

    getEntrepreneur(){
        return cy.get("#inlineRadio3")
    }

    getDobBox(){
        return cy.get("input[type='date']");
    }
}

export default HomePage