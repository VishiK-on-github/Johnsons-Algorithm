/*

JavaScript Code which is dynamically used to add edges when '+' button is clicked 

*/
var counter = 1;

function createEdge() {

    /*

    This code is used to add a div containing three fields
    source, destination, edge weight with associated attributes
    and class attribute containing custom bootstrap css.

    */

    // Getting the form to which dynamic element must be appended
    var getDiv = document.getElementById("form");
    
    // Getting the div before which we need to add div containing
    // the three fields
    var prependDiv = document.getElementById("submit-adj-matrix");

    // Creating a parent div to append elements to
    var parentDiv = document.createElement("div");

    // Setting class attribute according to bootstrap
    parentDiv.setAttribute("class", "row");

    // Getting input divs which will be appended in parent div
    var sourceDiv = create("Source Node");
    var destinationDiv = create("Destination Node");
    var edgeDiv = create("Edge Weight");

    // Appending the three input fields to the parent div
    parentDiv.appendChild(sourceDiv);
    parentDiv.appendChild(destinationDiv);
    parentDiv.appendChild(edgeDiv);

    // Appending the parentDiv before prependDiv inside the encompassing 
    // div whose id="form"
    getDiv.insertBefore(parentDiv, prependDiv);
    counter += 1;
    alert("New edge added !");
    return false;
}

function create(labelText) {

    // Creating a custom div with bootstrap class defined
    var makeDiv = document.createElement("div");
    makeDiv.setAttribute("class", "col-md-3 mb-3");

    // Creating a label with passed text
    var Label = document.createElement("label");
    Label.innerHTML = labelText;
    //Label.setAttribute("for", "<id>");

    // Creating a input field
    var Field = document.createElement("input");

    // Customising type attribute depending on field being made
    if(labelText == "Edge Weight") {
        Field.setAttribute("type", "text");
    }
    else {
        Field.setAttribute("type", "number");
        Field.setAttribute("min", "0");
    }

    // Setting field attribute class to the bootstrap class
    // Maybe possible if condition to separate source destination weight field 
    Field.setAttribute("class", "form-control");
    //Field.setAttribute("name", "");
    //Field.setAttribute("id", "");

    // Appending the label and input field to the encompassing div
    makeDiv.appendChild(Label);
    makeDiv.appendChild(Field);

    // returning the created div element
    return makeDiv;
}