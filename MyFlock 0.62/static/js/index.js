console.log("For more information, go to README.txt");

let inputData = document.getElementById("Search")

inputData.addEventListener("keydown", function(event) {
    if (event.code === "Enter") {
        window.location.href = "/search";
    }    
}
)