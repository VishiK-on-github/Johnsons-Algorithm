/*

JavaScript Code to validate the form after clicking 'Submit Adjacency Matrix' button

*/

function validateForm() {

    // Getting values from the the form

    var number_node = document.getElementById("nodeNum").value;
    if((number_node != "") && (number_node != null)) {

        var limit_edge = (number_node * number_node) - number_node;

        // Getting array of values from form

        var getSource = document.getElementsByName("source[]");
        var getDestination = document.getElementsByName("destination[]");
        var getWeight = document.getElementsByName("weight[]");

        var sourceLength = getSource.length;
        var destinationLength = getDestination.length;
        var weightLength = getWeight.length;

        // Validation of form left

        /*alert(`Source array length : ${sourceLength}`);
        alert(`Destination array length : ${destinationLength}`);
        alert(`weight array length : ${weightLength}`);*/

        if((sourceLength <= limit_edge)&&(destinationLength <= limit_edge)&&(weightLength <= limit_edge)) {

            for(var i=0; i<= sourceLength; i++) {

                if(Number.isInteger(getSource[i].value)) {

                    getSource[i].style.border = "2px solid lightgreen";
                }
            }
        }
        else {

            alert("Lengths dont match !");
            return false;
        }
    }
    else {

        alert("Please give number of nodes !");
        return false;
    }

    return false;
}