$(document).ready(function () {
    $("#fade_in_tasks").click(function () {
        $("ul").fadeIn("slow", function () {
            // Animation complete
        });
    });
});