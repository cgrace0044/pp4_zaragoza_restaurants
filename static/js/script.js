document.addEventListener("DOMContentLoaded", function () {
    const messagesContainer = document.getElementById("django-messages");

    if (messagesContainer) {
        setTimeout(() => {
            history.back();
        }, 2000);
    }
});