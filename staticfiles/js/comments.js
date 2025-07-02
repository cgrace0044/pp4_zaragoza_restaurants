/* jshint esversion: 11 */
/* global bootstrap */
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const commentModal = new bootstrap.Modal(document.getElementById("commentModal"));
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// ==============================
// Edit Comment Functionality
// ------------------------------
// Attaches click event listeners to all edit buttons.
// When an edit button is clicked, it fetches the comment content,
// populates the input field, updates the form action, and opens the modal for editing.
// ==============================
for (let button of editButtons) {
  button.addEventListener("click", function() {
    let commentId = this.dataset.comment_id;
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
    commentModal.show();
  });
}

// ==============================
// Delete Comment Functionality
// ------------------------------
// Attaches click event listeners to all delete buttons.
// When a delete button is clicked, it sets the delete URL for confirmation
// and opens a modal to confirm the deletion of the selected comment.
// ==============================
for (let button of deleteButtons) {
  button.addEventListener("click", function() {
    let commentId = this.dataset.comment_id;
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}
