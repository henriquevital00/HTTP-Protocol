const form = document.getElementById("needs-validation");

$(document).ready( async _ => await fetchPublications());

form.addEventListener("submit", async e => {
    e.preventDefault();

    formData = new FormData(e.target);
    result_data = FormDatatoJson(formData);

    await sendPublication(result_data)
})