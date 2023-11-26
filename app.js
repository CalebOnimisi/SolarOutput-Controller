function onPageLoad(){
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data, status){
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.locations;
            var uilocations = document.getElementById("uilocations");
            $('#uilocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uilocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;

const toggleButtons = document.querySelectorAll(".toggle");
        const statusMessage = document.getElementById("status-message");

        toggleButtons.forEach((button, index) => {
            button.addEventListener("click", () => {
                toggleStatus(button, index + 1);
            });
        });

        function toggleStatus(button, applianceNumber) {
            const status = button.parentElement.querySelector(".status");
            if (status.textContent === "Off") {
                status.textContent = "On";
                status.classList.add("on");
                if (statusMessage.style.display === "block") {
                    statusMessage.style.display = "none";
                }
            } else {
                status.textContent = "Off";
                status.classList.remove("on");
                statusMessage.style.display = "block";
            }
        }