const form = document.getElementById("needs-validation");

$(document).ready( _ => fetchPublications());

form.addEventListener("submit", e => {
    e.preventDefault();

    formData = new FormData(e.target);
    result_data = FormDatatoJson(formData);

    sendPublication(result_data)
})