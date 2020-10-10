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
    counter += 1;
    parentDiv.setAttribute("id", counter);

    // Getting input divs which will be appended in parent div
    var sourceDiv = create("Source Node");
    var destinationDiv = create("Destination Node");
    var edgeDiv = create("Edge Weight");

    // Appending the three input fields to the parent div
    parentDiv.appendChild(sourceDiv);
    parentDiv.appendChild(destinationDiv);
    parentDiv.appendChild(edgeDiv);

    // Creating div element to hold the remove edge element
    var removeButtonDiv = document.createElement("div");
    removeButtonDiv.setAttribute("class", "col-md-3 mb-3");

    // Adding a button to remove the edge
    var removeButton = document.createElement("button");
    removeButton.setAttribute("class", "btn btn-outline-dark");
    removeButton.setAttribute("onclick", "return removeEdge(this)");
    removeButton.innerHTML = "Remove Edge";
    removeButton.style.position = "absolute";
    removeButton.style.bottom = 0;

    // Adding the remove edge button to its div
    removeButtonDiv.appendChild(removeButton);

    // Adding the div containing remove edge button to parent div
    parentDiv.appendChild(removeButtonDiv);

    // Appending the parentDiv before prependDiv inside the encompassing 
    // div whose id="form"
    getDiv.insertBefore(parentDiv, prependDiv);
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
    
    // Conditionally setting id and class attribute
    if(labelText == "Source Node") {

        Field.setAttribute("name", "source[]");
        Label.setAttribute("for", `s-${counter}`);
        Field.setAttribute("id", `s-${counter}`);
    }
    else if(labelText == "Destination Node") {

        Field.setAttribute("name", "destination[]");
        Label.setAttribute("for", `d-${counter}`);
        Field.setAttribute("id", `d-${counter}`);
    }
    else if(labelText == "Edge Weight") {

        Field.setAttribute("name", "weight[]");
        Label.setAttribute("for", `w-${counter}`);
        Field.setAttribute("id", `w-${counter}`);
    }

    // Appending the label and input field to the encompassing div
    makeDiv.appendChild(Label);
    makeDiv.appendChild(Field);

    // returning the created div element
    return makeDiv;
}

function removeEdge(element) {

    // Getting the id of div class row to remove it
    var removeDivId = (element.parentNode).parentNode.id;
    var removeDiv = document.getElementById(removeDivId);

    // Removing the div from the DOM
    removeDiv.remove();

    // Alert message
    alert("Edge Removed !");

    return false;
}

