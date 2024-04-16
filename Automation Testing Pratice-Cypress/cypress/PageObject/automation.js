class TextBox{
    txtName = "#name";
    txtEmail = "#email";
    txtPhone = "#phone";
    txtAddress = "#textarea";

    inputName(name){
        cy.get(this.txtName).should("be.visible");
        cy.wait(1000);
        cy.get(this.txtName).type(name);
        cy.wait(1000)
        cy.get(this.txtName).should("have.value", name);
    }


    inputEmail(email){
        cy.get(this.txtEmail).should("be.visible");
        cy.wait(1000);
        cy.get(this.txtEmail).type(email);
        cy.wait(1000);
        cy.get(this.txtEmail).should("have.value", email);
    }

    inputPhone(phone){
        cy.get(this.txtPhone).should("be.visible");
        cy.wait(1000);
        cy.get(this.txtPhone).type(phone);
        cy.wait(1000);
        cy.get(this.txtPhone).should("have.value", phone);
    }

    inputAddress(address){
        cy.get(this.txtAddress).should("be.visible");
        cy.wait(1000);
        cy.get(this.txtAddress).type(address);
        cy.wait(1000);
        cy.get(this.txtAddress).should("have.value", address);
    }
}


class Radio{
    radioMale = "#male";
    radioFemale = "#female";

    selectMale(){
        cy.get(this.radioMale).should("be.visible");
        cy.wait(1000);
        cy.get(this.radioMale).check();
        cy.wait(1000);
        cy.get(this.radioMale).should("be.checked");
        cy.wait(1000);
        cy.get(this.radioFemale).should("not.be.checked");
    }

    selectFemale(){
        cy.get(this.radioFemale).should("be.visible");
        cy.wait(1000);
        cy.get(this.radioFemale).check();
        cy.wait(1000);
        cy.get(this.radioFemale).should("be.checked");
        cy.wait(1000);
        cy.get(this.radioMale).should("not.be.checked");
    }
}

class Checkbox{
    sunday = "#sunday";
    monday = "#monday";
    tuesday = "#tuesday";
    wednesday = "#wednesday";
    thursday = "#thursday";
    friday = "#friday";
    saturday = "#saturday";


    checkSunday(){
        cy.get(this.sunday).should("be.visible");
        cy.get(this.sunday).check().should("be.checked");
        cy.get(this.sunday).uncheck().should("not.be.checked");
    }

    checkMonday(){
        cy.get(this.monday).should("be.visible");
        cy.get(this.monday).check().should("be.checked");
        cy.get(this.monday).uncheck().should("not.be.checked");
    }

    checkTuesday(){
        cy.get(this.tuesday).should("be.visible");
        cy.get(this.tuesday).check().should("be.checked");
        cy.get(this.tuesday).uncheck().should("not.be.checked");
    }

    checkWednesday(){
        cy.get(this.wednesday).should("be.visible");
        cy.get(this.wednesday).check().should("be.checked");
        cy.get(this.wednesday).uncheck().should("not.be.checked");
    }

    checkThursday(){
        cy.get(this.thursday).should("be.visible");
        cy.get(this.thursday).check().should("be.checked");
        cy.get(this.thursday).uncheck().should("not.be.checked");
    }

    checkFriday(){
        cy.get(this.friday).should("be.visible");
        cy.get(this.friday).check().should("be.checked");
        cy.get(this.friday).uncheck().should("not.be.checked");
    }

    checkSaturday(){
        cy.get(this.saturday).should("be.visible");
        cy.get(this.saturday).check().should("be.checked");
        cy.get(this.saturday).uncheck().should("not.be.checked");
    }
}


class Select{
    selectcountry = "#country";
    selectcolor = "#colors";

    selectCountry(country){
        cy.get(this.selectcountry).should("be.visible");
        cy.get(this.selectcountry).select(country);
        cy.get(this.selectcountry).should("have.value", country.toLowerCase());
    }

    selectColor(color){
        cy.get(this.selectcolor).should("be.visible");
        cy.get(this.selectcolor).select(color);      
    }
}



class Table{
    tableRow = "div[id='HTML1']>div>table>tbody>tr";
    tableColumn = "div[id='HTML1']>div>table>tbody>tr>td";

    readingTable(){
        cy.get(this.tableRow).each(($row, index, $rows)=>{
            cy.wrap($row).within(()=>{
                cy.get("td").each(($col, index, $cols)=>{
                    cy.log($col.text());
                })
            })
        })
    }
}

class Search{
    searchbox = "#Wikipedia1_wikipedia-search-input";
    searchButton = ".wikipedia-search-button";

    searching(text){
        cy.get(this.searchbox).should("be.visible");
        cy.get(this.searchbox).type(text);
        cy.get(this.searchbox).should("have.value", text);
        cy.get(this.searchButton).should("be.visible").click();

    }
}

class Alerts{
    alert = "[onclick='myFunctionAlert()']";
    confirm = "[onclick='myFunctionConfirm()']";
    prompt = "[onclick='myFunctionPrompt()']";


    alertWindow(){
        cy.get(this.alert).click();
        cy.on("window:alert", (text)=>{
            expect(text).to.contains("I am an alert box!");
        })  
    }

    confirmWindow(){
        cy.get(this.confirm).click();
        cy.on("window:confirm",()=>false);
        cy.get("#demo").should("have.text", "You pressed Cancel!");
        cy.get(this.confirm).click();
        cy.on("window:confirm", (text)=>{
            expect(text).to.contains("Press a button!");
        })
    }

    prompWindow(text){
        cy.window().then((win)=>{
            cy.stub(win, "prompt").returns(text);
        })
        cy.get(this.prompt).click();
        cy.get("#demo").should("have.text",`Hello ${text}! How are you today?`);

    }
}

class DoubleClick{
    dbl = "[ondblclick='myFunction1()']";

    doubleClick(){
        cy.get(this.dbl).trigger("dblclick");
        cy.get("#field2").should("have.value", "Hello World!");
    }

}

class DragnDrop{
    dragEle = "#draggable";
    dropEle = "#droppable";

    dragOperation(){
        cy.get(this.dragEle).drag(this.dropEle, {force:true});
    }
}

class Slide{
    slider = "#slider>span";

    slideOperation(){
        cy.get(this.slider).click();
        cy.get(this.slider).type("{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}{rightarrow}")
    }

}



export{
    TextBox,
    Radio,
    Checkbox,
    Select,
    Table,
    Search,
    Alerts,
    DoubleClick,
    DragnDrop,
    Slide,
}
