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

        // Validation of form left

        /*alert(`Source array length : ${sourceLength}`);
        alert(`Destination array length : ${destinationLength}`);
        alert(`weight array length : ${weightLength}`);*/

        if((getSource.length <= limit_edge)&&(getDestination.length <= limit_edge)&&(getWeight.length <= limit_edge)) {

            function validFormStatus() {

                // Container method which determines validity of the form
    
                sf1 = validSourceDestination(getSource, getDestination, number_node);
                sf2 = validEdgeWeight(getWeight);
    
                // Returning the form status
                return (sf1 && sf2);
            } 
    
            return validFormStatus();
        }
        else {

            // This condition handles if edges exceed limit of the graph

            alert("Please remove some edges. The provided set of edges may result in an invalid graph !");
            return false;
        }
    }
    else {

        // This condition handles if number of nodes fields is empty

        alert("Please give number of nodes !");
        return false;
    }
}

function validSourceDestination(sourceArr, destinationArr, maxVal) {

    // Method to check if valid source and destination have been entered

    var srcDestFlagStatus = true;

    for(var i=0; i < sourceArr.length; i++) {

        if(parseInt(sourceArr[i].value) != parseInt(destinationArr[i].value)) {

            if((Number.isInteger(parseInt(sourceArr[i].value)))&&(parseInt(sourceArr[i].value) < maxVal)) {

                sourceArr[i].style.border = "2px solid lightgreen";
            }
            else {

                sourceArr[i].style.border = "2px solid red";
                if (srcDestFlagStatus == true) {

                    srcDestFlagStatus = false;
                }
            }
            if((Number.isInteger(parseInt(destinationArr[i].value)))&&(parseInt(destinationArr[i].value) < maxVal)) {

                destinationArr[i].style.border = "2px solid lightgreen";
            }
            else {

                destinationArr[i].style.border = "2px solid red";
                if (srcDestFlagStatus == true) {

                    srcDestFlagStatus = false;
                }
            }
        }
        else {

            sourceArr[i].style.border = "2px solid red";
            destinationArr[i].style.border = "2px solid red";
            if (srcDestFlagStatus == true) {

                srcDestFlagStatus = false;
            }
        }
    }

    // returning the status of the source and destination input fields
    return srcDestFlagStatus;
}


function validEdgeWeight(weightArr) {

    // Method to check if valid weights have been entered

    var weightFlagStatus = true;

    for(var i=0; i < weightArr.length; i++) {

        if((weightArr[i].value == "infinity")||(Number.isInteger(parseInt(weightArr[i].value)))) {

            weightArr[i].style.border = "2px solid lightgreen";
        }
        else {

            weightArr[i].style.border = "2px solid red";
            if (weightFlagStatus == true) {

                weightFlagStatus = false;
            }
        }
    }

    // returning the status of the weight input field
    return weightFlagStatus;
}