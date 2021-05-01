const form = document.getElementById("publication-form");

window.onload = _ => fetchPublications();

form.addEventListener("submit", async e => {
    e.preventDefault();

    formData = new FormData(e.target);
    result_data = FormDatatoJson(formData);

    await sendPublication(result_data)
});