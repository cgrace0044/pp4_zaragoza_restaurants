const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const commentModal = new bootstrap.Modal(document.getElementById("commentModal"));
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Loop through all elements with the class edit buttons
for (let button of editButtons) {
  // Add a click event listener to each edit button
  button.addEventListener("click", (e) => {
    // Get the comment ID from the clicked button's attribute
    let commentId = e.target.getAttribute("comment_id");
    // Retrieve the existing comment text using the comment ID
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    // Populate the comment input field with the existing comment text
    commentText.value = commentContent;
    // Change the submit button text to indicate update action
    submitButton.innerText = "Update";
    // Update the form action URL to target the correct comment for editing
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
    // Show the comment modal dialog for editing
    commentModal.show();
  });
}

// Loop through all elements in the deleteButtons collection
for (let button of deleteButtons) {
  // Add a click event listener to each delete button
  button.addEventListener("click", (e) => {
    // Get the comment ID from the clicked button's attribute
    let commentId = e.target.getAttribute("comment_id");
    // Set the confirmation link to point to the correct delete URL for the comment
    deleteConfirm.href = `delete_comment/${commentId}`;
    // Display the confirmation modal for deleting the comment
    deleteModal.show();
  });
}
