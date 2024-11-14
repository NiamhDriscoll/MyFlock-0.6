console.log("For more information, go to README.txt");
let admin;

function redirect_about() {
    window.location.href = "{{ url_for('about.html') }}";
}
