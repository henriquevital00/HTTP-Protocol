const form = document.getElementById("needs-validation");

const FormDatatoJson = formData => {

    obj = {};
    formData.forEach((value, key) => obj[key] = value);
    obj["date"] = new Date(Date.now()).toISOString()

    return JSON.stringify(obj);
}

const fetchResponseStyles = response => {

    response = response.reverse().map(resp => 
        `<div class="publication-card mt-4">
            <h1>${resp.hashtag}</h1>
            <p>${resp.content}</p>
            <p>${resp.date}</p>
        </div>`
    );
    
    $("#posts").html(response.join(''));
}

$(document).ready(function() {
    fetch("http://localhost:8000/publications/all", {
        headers: {
          'Accept': 'application/json',
          contentType: 'application/json',
        },
        method: "GET",
    })
    .then(response => response.json())
    .then(response => fetchResponseStyles(response));
});


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
            .then(response => fetchResponseStyles(response))
    )
})