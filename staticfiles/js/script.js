/* jshint esversion: 11 */
// Automatically fades out and removes Django alert messages after a delay
// This runs when the DOM content is fully loaded
window.addEventListener('DOMContentLoaded', function () {
    const alertContainer = document.getElementById('django-messages');
    const alerts = alertContainer?.querySelectorAll('.alert');

    alerts?.forEach(function (alert) {
      setTimeout(function () {
        // Fade out the alert
        alert.classList.remove('show');
        alert.classList.add('fade');

        // Wait for the fade-out to complete
        setTimeout(function () {
          alert.remove();

          // If no more alerts, remove the container
          if (alertContainer && alertContainer.querySelectorAll('.alert').length === 0) {
            alertContainer.remove();
          }
        }, 300); // Allow fade-out time
      }, 2000); // Wait 2 seconds before starting to dismiss
    });
  });