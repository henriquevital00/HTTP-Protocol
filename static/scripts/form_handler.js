const form = document.getElementById("needs-validation");

const FormDatatoJson = formData => {

    obj = {};
    formData.forEach((value, key) => obj[key] = value);
    obj["date"] = new Date(Date.now()).toISOString()

    return JSON.stringify(obj);
}


form.addEventListener("submit", e => {
    e.preventDefault();

    formData = new FormData(e.target);
    result_data = FormDatatoJson(formData);

    fetch("http://localhost:8000/publications/create",{
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'text/json'
        },
        method: "POST",
        body: result_data
    })
    .then(
        response => response.json()
        .then(response => console.log(response))
    )
})