let warnings = 0;

window.onblur = function () {
    alertViolation("Screen switching is not allowed!");
};

function alertViolation(message) {
    warnings += 1;
    document.getElementById("alert").innerText = message;
    if (warnings >= 3) {
        alert("You have been disqualified!");
        window.location.href = "/disqualified";
    }
}

function submitQuiz() {
    alert("Quiz submitted successfully!");
    window.location.href = "/submitted";
}
