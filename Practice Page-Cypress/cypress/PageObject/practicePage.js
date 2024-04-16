
class Radio{
    radio1 = "//input[@value='radio1']";
    radio2 = "//input[@value='radio2']";
    radio3 = "//input[@value='radio3']";


    selectRadio(){
        cy.xpath(this.radio1).should("be.visible").should("not.be.checked").check().should("be.checked");
        cy.xpath(this.radio2).should("be.visible").should("not.be.checked").check().should("be.checked");
        cy.xpath(this.radio3).should("be.visible").should("not.be.checked").check().should("be.checked");
    }
}


class SuggestiveDrpDwn{
    inputbox = "//input[@id='autocomplete']";
    elements = "//ul[@id='ui-id-1']/li";


    autoSuggestive(text){
        cy.xpath(this.inputbox).should("be.visible").type("ban");
        cy.xpath(this.elements).should("be.visible").contains(text).click();
        cy.xpath(this.inputbox).should("have.value", text);
    }
}

class Dropdown{
    field = "//select[@id='dropdown-class-example']";


    dropdownOp(text){
        cy.xpath(this.field).should("be.visible").select(text).should("have.value", text);
    }
}

class Checkbox{
    box1 = "//input[@id='checkBoxOption1']";
    box2 = "//input[@id='checkBoxOption2']";
    box3 = "//input[@id='checkBoxOption3']";


    checkboxOp(){}

}



class Alerts{
    textbox = "//input[@id='name']";
    alertButton = "//input[@id='alertbtn']";
    confirmButton = "//input[@id='confirmbtn']";

    alert(text){
        cy.xpath(this.textbox).should("be.visible").type(text).should("have.value", text);
        cy.xpath(this.alertButton).should("be.visible").click();
        cy.on("window:alert", t=>{
            expect(t).to.contains(`Hello ${text}, share this practice page and share your knowledge`)
        });
    }

    confirm(text){
        cy.xpath(this.textbox).should("be.visible").type(text).should("have.value", text);
        cy.xpath(this.confirmButton).should("be.visible").click();

        cy.on("window:confirm", t=>{
            expect(t).to.contains(`Hello ${text}, Are you sure you want to confirm?`);
        });
    }
}


class Display{
    textbox = "//input[@id='displayed-text']";
    hide = "//input[@id='hide-textbox']";
    show = "//input[@id='show-textbox']";


    displayExample(){
        cy.xpath(this.textbox).should("be.visible")
        cy.xpath(this.hide).should("be.visible").click();
        cy.xpath(this.textbox).should("not.be.visible");
        cy.xpath(this.show).should("be.visible").click();
        cy.xpath(this.textbox).should("be.visible");
    }
}


class Table{
    column2 = "//table[@name='courses']/tbody/tr/td[2]";


    tableData(){
        cy.xpath(this.column2).each(($ele, index, $eles) =>{
            const text = $ele.text()
            if(text.includes("Python")){
                cy.xpath(this.column2).eq(index).next().then(price=>{
                    const priceText = price.text();
                    expect(priceText).to.equal("25");
                })
            }
        })
    }
}


class MouseHover{
    button = "//button[@id='mousehover']";
    top = "//div[@class='mouse-hover-content']/a[1]";
    reload = "//div[@class='mouse-hover-content']/a[2]";


    mousehoverOp(){
        cy.xpath(this.button).should("be.visible").trigger("mouseover")
        cy.xpath(this.top).should("be.visible").click();
        cy.xpath(this.button).should("be.visible").trigger("mouseover")
        cy.wait(3000);
        cy.xpath(this.reload).should("be.visible").rightclick();
    }
}


export {
    Radio,
    SuggestiveDrpDwn,
    Dropdown,
    Alerts,
    Display,
    Table,
    MouseHover,
}