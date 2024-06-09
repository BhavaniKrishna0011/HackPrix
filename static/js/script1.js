
    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // Get the elements to blur
    var blurElements = document.querySelectorAll('header, aside, main');

    // Function to show the modal
    function showModal() {
        // Update the vehicle image URL with a timestamp to avoid caching
        var vehicleImage = document.querySelector(".modal-content img[src*='vehicles']");
        if (vehicleImage) {
            var newSrc = "http://192.168.10.59:5000/static/images/vehicles/?t=" + new Date().getTime();
            vehicleImage.src = newSrc;
        }
        
        modal.style.display = "block";
        applyBlur();
    }

    // Function to hide the modal
    function hideModal() {
        modal.style.display = "none";
        removeBlur();
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        hideModal();
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            hideModal();
        }
    }

    // Show the modal every 10 seconds
    setInterval(function() {
        showModal();
    }, 10000);

    // Apply blur to the background
    function applyBlur() {
        blurElements.forEach(function(element) {
            element.classList.add('blur');
        });
    }

    // Remove blur from the background
    function removeBlur() {
        blurElements.forEach(function(element) {
            element.classList.remove('blur');
        });
    }

